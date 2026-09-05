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
