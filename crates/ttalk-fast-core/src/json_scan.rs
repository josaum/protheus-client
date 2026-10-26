//! Byte-level helpers for the decode hot path: locate the collection inside a
//! TTALK page and turn a JSON array of objects into the whitespace-separated
//! record stream `arrow-json` consumes — without building a DOM.

/// Where the rows live in a page body.
pub struct PageShape<'a> {
    /// Raw bytes of the JSON array holding the rows (including `[` `]`).
    pub rows: &'a [u8],
    pub has_next: Option<bool>,
}

fn skip_ws(bytes: &[u8], mut i: usize) -> usize {
    while i < bytes.len() && matches!(bytes[i], b' ' | b'\n' | b'\r' | b'\t') {
        i += 1;
    }
    i
}

/// End index (exclusive) of the JSON value starting at `start`.
fn value_end(bytes: &[u8], start: usize) -> Option<usize> {
    let mut i = start;
    match bytes.get(i)? {
        b'"' => {
            i += 1;
            while i < bytes.len() {
                match bytes[i] {
                    b'\\' => i += 2,
                    b'"' => return Some(i + 1),
                    _ => i += 1,
                }
            }
            None
        }
        b'{' | b'[' => {
            let mut depth = 0usize;
            let mut in_str = false;
            while i < bytes.len() {
                let b = bytes[i];
                if in_str {
                    match b {
                        b'\\' => i += 1,
                        b'"' => in_str = false,
                        _ => {}
                    }
                } else {
                    match b {
                        b'"' => in_str = true,
                        b'{' | b'[' => depth += 1,
                        b'}' | b']' => {
                            depth -= 1;
                            if depth == 0 {
                                return Some(i + 1);
                            }
                        }
                        _ => {}
                    }
                }
                i += 1;
            }
            None
        }
        _ => {
            while i < bytes.len()
                && !matches!(bytes[i], b',' | b'}' | b']' | b' ' | b'\n' | b'\r' | b'\t')
            {
                i += 1;
            }
            Some(i)
        }
    }
}

/// Find the rows of a page: `{"hasNext": …, "<items_key>": [ … ]}` yields the
/// array and the flag; a bare array is the rows themselves.
pub fn locate_rows<'a>(body: &'a [u8], items_key: &str) -> Option<PageShape<'a>> {
    let i = skip_ws(body, 0);
    match body.get(i)? {
        b'[' => Some(PageShape {
            rows: &body[i..value_end(body, i)?],
            has_next: None,
        }),
        b'{' => {
            let mut rows = None;
            let mut has_next = None;
            let mut pos = i + 1;
            loop {
                pos = skip_ws(body, pos);
                match body.get(pos)? {
                    b'}' => break,
                    b',' => {
                        pos += 1;
                        continue;
                    }
                    b'"' => {}
                    _ => return None,
                }
                let key_end = value_end(body, pos)?;
                let key = &body[pos + 1..key_end - 1];
                pos = skip_ws(body, key_end);
                if body.get(pos)? != &b':' {
                    return None;
                }
                pos = skip_ws(body, pos + 1);
                let val_end = value_end(body, pos)?;
                let value = &body[pos..val_end];
                if key == items_key.as_bytes() && value.first() == Some(&b'[') {
                    rows = Some(value);
                } else if key == b"hasNext" {
                    has_next = match value {
                        b"true" => Some(true),
                        b"false" => Some(false),
                        _ => None,
                    };
                }
                pos = val_end;
            }
            rows.map(|rows| PageShape { rows, has_next })
        }
        _ => None,
    }
}

/// `[ {…}, {…} ]` -> `{…} {…}` (brackets and top-level commas blanked), which is
/// what `arrow_json::reader::Decoder::decode` accepts.
pub fn array_to_record_stream(array: &[u8]) -> Vec<u8> {
    let mut out = array.to_vec();
    let mut depth = 0usize;
    let mut in_str = false;
    let mut i = 0;
    while i < out.len() {
        let b = out[i];
        if in_str {
            match b {
                b'\\' => i += 1,
                b'"' => in_str = false,
                _ => {}
            }
        } else {
            match b {
                b'"' => in_str = true,
                b'[' | b'{' => {
                    if depth == 0 {
                        out[i] = b' ';
                    }
                    depth += 1;
                }
                b']' | b'}' => {
                    depth -= 1;
                    if depth == 0 {
                        out[i] = b' ';
                    }
                }
                b',' if depth == 1 => out[i] = b' ',
                _ => {}
            }
        }
        i += 1;
    }
    out
}

/// Number of top-level elements in a JSON array (for empty-page handling).
pub fn array_is_empty(array: &[u8]) -> bool {
    let inner = &array[1..array.len().saturating_sub(1)];
    inner
        .iter()
        .all(|b| matches!(b, b' ' | b'\n' | b'\r' | b'\t'))
}

/// Structural budgets enforced without constructing a JSON DOM.
#[derive(Debug, Clone, Copy)]
pub struct ScanLimits {
    pub max_rows: usize,
    pub max_columns: usize,
    pub max_nesting_depth: usize,
    pub max_string_length: usize,
    pub max_array_length: usize,
}

#[derive(Debug)]
pub enum ScanError {
    Malformed(String),
    Limit {
        limit: &'static str,
        actual: usize,
        maximum: usize,
    },
}

struct Parser<'a> {
    bytes: &'a [u8],
    pos: usize,
    limits: ScanLimits,
    items_key: &'a str,
    rows: usize,
}

impl<'a> Parser<'a> {
    fn malformed<T>(&self, message: impl Into<String>) -> Result<T, ScanError> {
        Err(ScanError::Malformed(format!(
            "{} at byte {}",
            message.into(),
            self.pos
        )))
    }

    fn limit<T>(&self, limit: &'static str, actual: usize, maximum: usize) -> Result<T, ScanError> {
        Err(ScanError::Limit {
            limit,
            actual,
            maximum,
        })
    }

    fn ws(&mut self) {
        self.pos = skip_ws(self.bytes, self.pos);
    }

    fn parse(mut self) -> Result<usize, ScanError> {
        self.ws();
        self.value(0, true)?;
        self.ws();
        if self.pos != self.bytes.len() {
            return self.malformed("trailing data");
        }
        Ok(self.rows)
    }

    fn value(&mut self, depth: usize, root: bool) -> Result<(), ScanError> {
        self.ws();
        match self.bytes.get(self.pos).copied() {
            Some(b'{') => self.object(depth + 1, root),
            Some(b'[') => self.array(depth + 1, root),
            Some(b'"') => self.string(),
            Some(b't') => self.literal(b"true"),
            Some(b'f') => self.literal(b"false"),
            Some(b'n') => self.literal(b"null"),
            Some(b'-' | b'0'..=b'9') => self.number(),
            Some(_) => self.malformed("expected a JSON value"),
            None => self.malformed("unexpected end of input"),
        }
    }

    fn literal(&mut self, literal: &[u8]) -> Result<(), ScanError> {
        if self.bytes.get(self.pos..self.pos + literal.len()) == Some(literal) {
            self.pos += literal.len();
            Ok(())
        } else {
            self.malformed("invalid literal")
        }
    }

    fn number(&mut self) -> Result<(), ScanError> {
        let start = self.pos;
        while let Some(b) = self.bytes.get(self.pos) {
            if matches!(b, b',' | b'}' | b']' | b' ' | b'\n' | b'\r' | b'\t') {
                break;
            }
            self.pos += 1;
        }
        let token = &self.bytes[start..self.pos];
        if token.is_empty()
            || std::str::from_utf8(token)
                .ok()
                .and_then(|s| s.parse::<f64>().ok())
                .is_none()
        {
            return self.malformed("invalid number");
        }
        Ok(())
    }

    fn string(&mut self) -> Result<(), ScanError> {
        self.pos += 1;
        let start = self.pos;
        while let Some(b) = self.bytes.get(self.pos).copied() {
            match b {
                b'"' => {
                    let length = self.pos - start;
                    if length > self.limits.max_string_length {
                        return self.limit("string_length", length, self.limits.max_string_length);
                    }
                    self.pos += 1;
                    return Ok(());
                }
                b'\\' => {
                    self.pos += 1;
                    let Some(escaped) = self.bytes.get(self.pos).copied() else {
                        return self.malformed("unterminated escape");
                    };
                    if escaped == b'u' {
                        for _ in 0..4 {
                            self.pos += 1;
                            if !self.bytes.get(self.pos).is_some_and(u8::is_ascii_hexdigit) {
                                return self.malformed("invalid Unicode escape");
                            }
                        }
                    } else if !matches!(
                        escaped,
                        b'"' | b'\\' | b'/' | b'b' | b'f' | b'n' | b'r' | b't'
                    ) {
                        return self.malformed("invalid escape");
                    }
                }
                0..=0x1f => return self.malformed("control character in string"),
                _ => {}
            }
            self.pos += 1;
        }
        self.malformed("unterminated string")
    }

    fn array(&mut self, depth: usize, rows: bool) -> Result<(), ScanError> {
        if depth > self.limits.max_nesting_depth {
            return self.limit("nesting_depth", depth, self.limits.max_nesting_depth);
        }
        self.pos += 1;
        self.ws();
        if self.bytes.get(self.pos) == Some(&b']') {
            self.pos += 1;
            return Ok(());
        }
        let mut count = 0usize;
        loop {
            count += 1;
            if count > self.limits.max_array_length {
                return self.limit("array_length", count, self.limits.max_array_length);
            }
            if rows {
                self.rows = count;
                if count > self.limits.max_rows {
                    return self.limit("rows", count, self.limits.max_rows);
                }
            }
            self.value(depth, false)?;
            self.ws();
            match self.bytes.get(self.pos) {
                Some(b',') => self.pos += 1,
                Some(b']') => {
                    self.pos += 1;
                    return Ok(());
                }
                _ => return self.malformed("expected ',' or ']'"),
            }
        }
    }

    fn object(&mut self, depth: usize, root: bool) -> Result<(), ScanError> {
        if depth > self.limits.max_nesting_depth {
            return self.limit("nesting_depth", depth, self.limits.max_nesting_depth);
        }
        self.pos += 1;
        self.ws();
        if self.bytes.get(self.pos) == Some(&b'}') {
            self.pos += 1;
            return Ok(());
        }
        let mut count = 0usize;
        loop {
            self.ws();
            if self.bytes.get(self.pos) != Some(&b'"') {
                return self.malformed("expected an object key");
            }
            let key_start = self.pos + 1;
            self.string()?;
            count += 1;
            if count > self.limits.max_columns {
                return self.limit("columns", count, self.limits.max_columns);
            }
            let is_items = root
                && self
                    .bytes
                    .get(key_start..self.pos - 1)
                    .and_then(|k| std::str::from_utf8(k).ok())
                    == Some(self.items_key);
            self.ws();
            if self.bytes.get(self.pos) != Some(&b':') {
                return self.malformed("expected ':'");
            }
            self.pos += 1;
            self.ws();
            if is_items && self.bytes.get(self.pos) == Some(&b'[') {
                self.array(depth + 1, true)?;
            } else {
                self.value(depth, false)?;
            }
            self.ws();
            match self.bytes.get(self.pos) {
                Some(b',') => self.pos += 1,
                Some(b'}') => {
                    self.pos += 1;
                    return Ok(());
                }
                _ => return self.malformed("expected ',' or '}'"),
            }
        }
    }
}

/// Validate JSON structure and enforce allocation-related limits. Returns the
/// number of rows in a root array or in the root object's `items_key` array.
pub fn inspect(body: &[u8], items_key: &str, limits: ScanLimits) -> Result<usize, ScanError> {
    Parser {
        bytes: body,
        pos: 0,
        limits,
        items_key,
        rows: 0,
    }
    .parse()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn locates_rows_and_flag() {
        let body = br#" {"hasNext" : true , "items": [{"a":"x,]}"},{"a":2}], "n": 1}"#;
        let shape = locate_rows(body, "items").unwrap();
        assert_eq!(shape.has_next, Some(true));
        assert_eq!(shape.rows, br#"[{"a":"x,]}"},{"a":2}]"#);
        assert_eq!(
            String::from_utf8(array_to_record_stream(shape.rows)).unwrap(),
            r#" {"a":"x,]}"} {"a":2} "#
        );
        assert!(locate_rows(br#"{"items": {}}"#, "items").is_none());
        let bare = locate_rows(b"[1, 2]", "items").unwrap();
        assert_eq!((bare.rows, bare.has_next), (&b"[1, 2]"[..], None));
        assert!(array_is_empty(b"[ ]"));
        assert!(!array_is_empty(b"[{}]"));
    }
}
