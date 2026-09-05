"""Generated API accessors (ttalk ca5e26a). Do not edit by hand."""
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from protheus.apis.accounting_calendar_v1 import AccountingCalendarV1, AsyncAccountingCalendarV1
    from protheus.apis.accounting_items_v1 import AccountingItemsV1, AsyncAccountingItemsV1
    from protheus.apis.address_stock_v1 import AddressStockV1, AsyncAddressStockV1
    from protheus.apis.annotation_v1 import AnnotationV1, AsyncAnnotationV1
    from protheus.apis.approval_profile_v1 import ApprovalProfileV1, AsyncApprovalProfileV1
    from protheus.apis.approval_profile_v2 import ApprovalProfileV2, AsyncApprovalProfileV2
    from protheus.apis.approvers_v1 import ApproversV1, AsyncApproversV1
    from protheus.apis.audit_checklist_v1 import AuditChecklistV1, AsyncAuditChecklistV1
    from protheus.apis.audit_panel_v1 import AuditPanelV1, AsyncAuditPanelV1
    from protheus.apis.audit_questionnaire_v1 import AuditQuestionnaireV1, AsyncAuditQuestionnaireV1
    from protheus.apis.audit_topic_v1 import AuditTopicV1, AsyncAuditTopicV1
    from protheus.apis.beneficiaries_coparticipation_v1 import BeneficiariesCoparticipationV1, AsyncBeneficiariesCoparticipationV1
    from protheus.apis.beneficiaries_data_content_v1 import BeneficiariesDataContentV1, AsyncBeneficiariesDataContentV1
    from protheus.apis.budget_balance_type_v1 import BudgetBalanceTypeV1, AsyncBudgetBalanceTypeV1
    from protheus.apis.buyers_v1 import BuyersV1, AsyncBuyersV1
    from protheus.apis.campaigns_v1 import CampaignsV1, AsyncCampaignsV1
    from protheus.apis.candidates_v2 import CandidatesV2, AsyncCandidatesV2
    from protheus.apis.carrier_v1 import CarrierV1, AsyncCarrierV1
    from protheus.apis.cashier_operator_v1 import CashierOperatorV1, AsyncCashierOperatorV1
    from protheus.apis.cat_report_v1 import CatReportV1, AsyncCatReportV1
    from protheus.apis.class_value_v1 import ClassValueV1, AsyncClassValueV1
    from protheus.apis.commercial_proposal_v1 import CommercialProposalV1, AsyncCommercialProposalV1
    from protheus.apis.contact_relationship_v1 import ContactRelationshipV1, AsyncContactRelationshipV1
    from protheus.apis.contact_v1 import ContactV1, AsyncContactV1
    from protheus.apis.contaminants_v1 import ContaminantsV1, AsyncContaminantsV1
    from protheus.apis.cost_center_v1 import CostCenterV1, AsyncCostCenterV1
    from protheus.apis.cotton_bales_on_treadmills_v1 import CottonBalesOnTreadmillsV1, AsyncCottonBalesOnTreadmillsV1
    from protheus.apis.cotton_bales_v1 import CottonBalesV1, AsyncCottonBalesV1
    from protheus.apis.cotton_color_grades_v1 import CottonColorGradesV1, AsyncCottonColorGradesV1
    from protheus.apis.cotton_gin_break_pointings_v1 import CottonGinBreakPointingsV1, AsyncCottonGinBreakPointingsV1
    from protheus.apis.cotton_gin_breaks_v1 import CottonGinBreaksV1, AsyncCottonGinBreaksV1
    from protheus.apis.cotton_gin_machines_v1 import CottonGinMachinesV1, AsyncCottonGinMachinesV1
    from protheus.apis.cotton_gins_v1 import CottonGinsV1, AsyncCottonGinsV1
    from protheus.apis.cotton_poisoning_pointings_v1 import CottonPoisoningPointingsV1, AsyncCottonPoisoningPointingsV1
    from protheus.apis.currency_quote_v1 import CurrencyQuoteV1, AsyncCurrencyQuoteV1
    from protheus.apis.customer_credit_limit_v1 import CustomerCreditLimitV1, AsyncCustomerCreditLimitV1
    from protheus.apis.customer_shipping_address_v1 import CustomerShippingAddressV1, AsyncCustomerShippingAddressV1
    from protheus.apis.customer_vendor_v1 import CustomerVendorV1, AsyncCustomerVendorV1
    from protheus.apis.discovery_environments_v1 import DiscoveryEnvironmentsV1, AsyncDiscoveryEnvironmentsV1
    from protheus.apis.discovery_keys_v1 import DiscoveryKeysV1, AsyncDiscoveryKeysV1
    from protheus.apis.discovery_stages_v1 import DiscoveryStagesV1, AsyncDiscoveryStagesV1
    from protheus.apis.documents_v1 import DocumentsV1, AsyncDocumentsV1
    from protheus.apis.employee_data_content_v1 import EmployeeDataContentV1, AsyncEmployeeDataContentV1
    from protheus.apis.employees_manager_data_content_v1 import EmployeesManagerDataContentV1, AsyncEmployeesManagerDataContentV1
    from protheus.apis.entities_v1 import EntitiesV1, AsyncEntitiesV1
    from protheus.apis.esocial_audit_v1 import EsocialAuditV1, AsyncEsocialAuditV1
    from protheus.apis.esocial_branches_v1 import EsocialBranchesV1, AsyncEsocialBranchesV1
    from protheus.apis.esocial_establishment_v1 import EsocialEstablishmentV1, AsyncEsocialEstablishmentV1
    from protheus.apis.esocial_events_v1 import EsocialEventsV1, AsyncEsocialEventsV1
    from protheus.apis.events_v1 import EventsV1, AsyncEventsV1
    from protheus.apis.fgts_per_worker_in_labor_process_v1 import FgtsPerWorkerInLaborProcessV1, AsyncFgtsPerWorkerInLaborProcessV1
    from protheus.apis.freight_accounting_batches_v1 import FreightAccountingBatchesV1, AsyncFreightAccountingBatchesV1
    from protheus.apis.freight_components_v1 import FreightComponentsV1, AsyncFreightComponentsV1
    from protheus.apis.freight_documents_v1 import FreightDocumentsV1, AsyncFreightDocumentsV1
    from protheus.apis.freight_invoices_v1 import FreightInvoicesV1, AsyncFreightInvoicesV1
    from protheus.apis.gpe_esocial_motives_v1 import GpeEsocialMotivesV1, AsyncGpeEsocialMotivesV1
    from protheus.apis.grain_quality_test_kinds_v1 import GrainQualityTestKindsV1, AsyncGrainQualityTestKindsV1
    from protheus.apis.item_reserve_v1 import ItemReserveV1, AsyncItemReserveV1
    from protheus.apis.job_scheduler_v1_001 import JobSchedulerV1001, AsyncJobSchedulerV1001
    from protheus.apis.job_scheduler_v1_100 import JobSchedulerV1100, AsyncJobSchedulerV1100
    from protheus.apis.manifest_v1 import ManifestV1, AsyncManifestV1
    from protheus.apis.market_segment_v2 import MarketSegmentV2, AsyncMarketSegmentV2
    from protheus.apis.menus_v1 import MenusV1, AsyncMenusV1
    from protheus.apis.mrp_allocations_v1 import MrpAllocationsV1, AsyncMrpAllocationsV1
    from protheus.apis.mrp_bill_of_material_v1 import MrpBillOfMaterialV1, AsyncMrpBillOfMaterialV1
    from protheus.apis.mrp_calendar_v1 import MrpCalendarV1, AsyncMrpCalendarV1
    from protheus.apis.mrp_demands_v1 import MrpDemandsV1, AsyncMrpDemandsV1
    from protheus.apis.mrp_prod_version_v1 import MrpProdVersionV1, AsyncMrpProdVersionV1
    from protheus.apis.mrp_product_indicator_v1 import MrpProductIndicatorV1, AsyncMrpProductIndicatorV1
    from protheus.apis.mrp_product_v1 import MrpProductV1, AsyncMrpProductV1
    from protheus.apis.mrp_production_orders_v1 import MrpProductionOrdersV1, AsyncMrpProductionOrdersV1
    from protheus.apis.mrp_purchase_order_v1 import MrpPurchaseOrderV1, AsyncMrpPurchaseOrderV1
    from protheus.apis.mrp_purchase_request_v1 import MrpPurchaseRequestV1, AsyncMrpPurchaseRequestV1
    from protheus.apis.mrp_rejected_inventory_v1 import MrpRejectedInventoryV1, AsyncMrpRejectedInventoryV1
    from protheus.apis.mrp_routing_v1 import MrpRoutingV1, AsyncMrpRoutingV1
    from protheus.apis.mrp_stock_balance_v1 import MrpStockBalanceV1, AsyncMrpStockBalanceV1
    from protheus.apis.mrp_transporting_lanes_v1 import MrpTransportingLanesV1, AsyncMrpTransportingLanesV1
    from protheus.apis.mrp_ware_house_inventory_policies_v1 import MrpWareHouseInventoryPoliciesV1, AsyncMrpWareHouseInventoryPoliciesV1
    from protheus.apis.mrp_warehouse_group_v1 import MrpWarehouseGroupV1, AsyncMrpWarehouseGroupV1
    from protheus.apis.mrp_warehouse_v1 import MrpWarehouseV1, AsyncMrpWarehouseV1
    from protheus.apis.mrp_work_center_v1 import MrpWorkCenterV1, AsyncMrpWorkCenterV1
    from protheus.apis.mrpbom_routing_v1 import MrpbomRoutingV1, AsyncMrpbomRoutingV1
    from protheus.apis.notes_v1 import NotesV1, AsyncNotesV1
    from protheus.apis.opportunity_v1 import OpportunityV1, AsyncOpportunityV1
    from protheus.apis.payment_condition_v1 import PaymentConditionV1, AsyncPaymentConditionV1
    from protheus.apis.payroll_control_v1 import PayrollControlV1, AsyncPayrollControlV1
    from protheus.apis.price_list_header_item_v2 import PriceListHeaderItemV2, AsyncPriceListHeaderItemV2
    from protheus.apis.prospects_v1 import ProspectsV1, AsyncProspectsV1
    from protheus.apis.purchase_groups_v1 import PurchaseGroupsV1, AsyncPurchaseGroupsV1
    from protheus.apis.region_groups_v1 import RegionGroupsV1, AsyncRegionGroupsV1
    from protheus.apis.requesters_v1 import RequestersV1, AsyncRequestersV1
    from protheus.apis.resource_v1 import ResourceV1, AsyncResourceV1
    from protheus.apis.retail_item_v1 import RetailItemV1, AsyncRetailItemV1
    from protheus.apis.retail_price_list_v1 import RetailPriceListV1, AsyncRetailPriceListV1
    from protheus.apis.retail_sales_orders_v1 import RetailSalesOrdersV1, AsyncRetailSalesOrdersV1
    from protheus.apis.retail_sales_v1 import RetailSalesV1, AsyncRetailSalesV1
    from protheus.apis.retail_stock_level_v1 import RetailStockLevelV1, AsyncRetailStockLevelV1
    from protheus.apis.roles_v1 import RolesV1, AsyncRolesV1
    from protheus.apis.sales_charge_v1 import SalesChargeV1, AsyncSalesChargeV1
    from protheus.apis.sales_process_v1 import SalesProcessV1, AsyncSalesProcessV1
    from protheus.apis.sales_targets_v1 import SalesTargetsV1, AsyncSalesTargetsV1
    from protheus.apis.sales_taxes_v1 import SalesTaxesV1, AsyncSalesTaxesV1
    from protheus.apis.seller_activity_v1 import SellerActivityV1, AsyncSellerActivityV1
    from protheus.apis.sellers_v2 import SellersV2, AsyncSellersV2
    from protheus.apis.stop_reason_v1 import StopReasonV1, AsyncStopReasonV1
    from protheus.apis.stop_report_v1 import StopReportV1, AsyncStopReportV1
    from protheus.apis.suspects_v1 import SuspectsV1, AsyncSuspectsV1
    from protheus.apis.system_modules_v1 import SystemModulesV1, AsyncSystemModulesV1
    from protheus.apis.system_parameter_v1 import SystemParameterV1, AsyncSystemParameterV1
    from protheus.apis.taf_esocial_remove_company_v1 import TafEsocialRemoveCompanyV1, AsyncTafEsocialRemoveCompanyV1
    from protheus.apis.token_v1 import TokenV1, AsyncTokenV1
    from protheus.apis.total_input_document_v1 import TotalInputDocumentV1, AsyncTotalInputDocumentV1
    from protheus.apis.total_output_document_v1 import TotalOutputDocumentV1, AsyncTotalOutputDocumentV1
    from protheus.apis.treadmills_v1 import TreadmillsV1, AsyncTreadmillsV1
    from protheus.apis.tsi_branches_v1 import TsiBranchesV1, AsyncTsiBranchesV1
    from protheus.apis.tsi_integration_errors_v1 import TsiIntegrationErrorsV1, AsyncTsiIntegrationErrorsV1
    from protheus.apis.tsi_service_status_v1 import TsiServiceStatusV1, AsyncTsiServiceStatusV1
    from protheus.apis.unit_of_measure_v1 import UnitOfMeasureV1, AsyncUnitOfMeasureV1
    from protheus.apis.unit_of_measure_v2 import UnitOfMeasureV2, AsyncUnitOfMeasureV2
    from protheus.apis.urbano_coletor_v1 import UrbanoColetorV1, AsyncUrbanoColetorV1
    from protheus.apis.user_v1 import UserV1, AsyncUserV1
    from protheus.apis.waste_reason_v1 import WasteReasonV1, AsyncWasteReasonV1


API_IDS: tuple[str, ...] = (
    "accounting_calendar_v1",
    "accounting_items_v1",
    "address_stock_v1",
    "annotation_v1",
    "approval_profile_v1",
    "approval_profile_v2",
    "approvers_v1",
    "audit_checklist_v1",
    "audit_panel_v1",
    "audit_questionnaire_v1",
    "audit_topic_v1",
    "beneficiaries_coparticipation_v1",
    "beneficiaries_data_content_v1",
    "budget_balance_type_v1",
    "buyers_v1",
    "campaigns_v1",
    "candidates_v2",
    "carrier_v1",
    "cashier_operator_v1",
    "cat_report_v1",
    "class_value_v1",
    "commercial_proposal_v1",
    "contact_relationship_v1",
    "contact_v1",
    "contaminants_v1",
    "cost_center_v1",
    "cotton_bales_on_treadmills_v1",
    "cotton_bales_v1",
    "cotton_color_grades_v1",
    "cotton_gin_break_pointings_v1",
    "cotton_gin_breaks_v1",
    "cotton_gin_machines_v1",
    "cotton_gins_v1",
    "cotton_poisoning_pointings_v1",
    "currency_quote_v1",
    "customer_credit_limit_v1",
    "customer_shipping_address_v1",
    "customer_vendor_v1",
    "discovery_environments_v1",
    "discovery_keys_v1",
    "discovery_stages_v1",
    "documents_v1",
    "employee_data_content_v1",
    "employees_manager_data_content_v1",
    "entities_v1",
    "esocial_audit_v1",
    "esocial_branches_v1",
    "esocial_establishment_v1",
    "esocial_events_v1",
    "events_v1",
    "fgts_per_worker_in_labor_process_v1",
    "freight_accounting_batches_v1",
    "freight_components_v1",
    "freight_documents_v1",
    "freight_invoices_v1",
    "gpe_esocial_motives_v1",
    "grain_quality_test_kinds_v1",
    "item_reserve_v1",
    "job_scheduler_v1_001",
    "job_scheduler_v1_100",
    "manifest_v1",
    "market_segment_v2",
    "menus_v1",
    "mrp_allocations_v1",
    "mrp_bill_of_material_v1",
    "mrp_calendar_v1",
    "mrp_demands_v1",
    "mrp_prod_version_v1",
    "mrp_product_indicator_v1",
    "mrp_product_v1",
    "mrp_production_orders_v1",
    "mrp_purchase_order_v1",
    "mrp_purchase_request_v1",
    "mrp_rejected_inventory_v1",
    "mrp_routing_v1",
    "mrp_stock_balance_v1",
    "mrp_transporting_lanes_v1",
    "mrp_ware_house_inventory_policies_v1",
    "mrp_warehouse_group_v1",
    "mrp_warehouse_v1",
    "mrp_work_center_v1",
    "mrpbom_routing_v1",
    "notes_v1",
    "opportunity_v1",
    "payment_condition_v1",
    "payroll_control_v1",
    "price_list_header_item_v2",
    "prospects_v1",
    "purchase_groups_v1",
    "region_groups_v1",
    "requesters_v1",
    "resource_v1",
    "retail_item_v1",
    "retail_price_list_v1",
    "retail_sales_orders_v1",
    "retail_sales_v1",
    "retail_stock_level_v1",
    "roles_v1",
    "sales_charge_v1",
    "sales_process_v1",
    "sales_targets_v1",
    "sales_taxes_v1",
    "seller_activity_v1",
    "sellers_v2",
    "stop_reason_v1",
    "stop_report_v1",
    "suspects_v1",
    "system_modules_v1",
    "system_parameter_v1",
    "taf_esocial_remove_company_v1",
    "token_v1",
    "total_input_document_v1",
    "total_output_document_v1",
    "treadmills_v1",
    "tsi_branches_v1",
    "tsi_integration_errors_v1",
    "tsi_service_status_v1",
    "unit_of_measure_v1",
    "unit_of_measure_v2",
    "urbano_coletor_v1",
    "user_v1",
    "waste_reason_v1",
)


class SyncApis:
    """Lazy per-API accessors; mixed into the sync client."""

    @cached_property
    def accounting_calendar_v1(self) -> AccountingCalendarV1:
        """Calendário Contábil (/api/ctb/v1)."""
        from protheus.apis.accounting_calendar_v1 import AccountingCalendarV1

        return AccountingCalendarV1(self)  # type: ignore[arg-type]

    @cached_property
    def accounting_items_v1(self) -> AccountingItemsV1:
        """Item Contábil (/api/ctb/v1)."""
        from protheus.apis.accounting_items_v1 import AccountingItemsV1

        return AccountingItemsV1(self)  # type: ignore[arg-type]

    @cached_property
    def address_stock_v1(self) -> AddressStockV1:
        """Endereços (/api/entradas/v1)."""
        from protheus.apis.address_stock_v1 import AddressStockV1

        return AddressStockV1(self)  # type: ignore[arg-type]

    @cached_property
    def annotation_v1(self) -> AnnotationV1:
        """Apontamento de Visita (/api/crm/v1)."""
        from protheus.apis.annotation_v1 import AnnotationV1

        return AnnotationV1(self)  # type: ignore[arg-type]

    @cached_property
    def approval_profile_v1(self) -> ApprovalProfileV1:
        """Perfil de Aprovação (/api/framework/v1)."""
        from protheus.apis.approval_profile_v1 import ApprovalProfileV1

        return ApprovalProfileV1(self)  # type: ignore[arg-type]

    @cached_property
    def approval_profile_v2(self) -> ApprovalProfileV2:
        """Perfil/Grade de Aprovação (/api/supply/v2)."""
        from protheus.apis.approval_profile_v2 import ApprovalProfileV2

        return ApprovalProfileV2(self)  # type: ignore[arg-type]

    @cached_property
    def approvers_v1(self) -> ApproversV1:
        """Aprovadores (/api/supply/v1)."""
        from protheus.apis.approvers_v1 import ApproversV1

        return ApproversV1(self)  # type: ignore[arg-type]

    @cached_property
    def audit_checklist_v1(self) -> AuditChecklistV1:
        """Checklist de Auditoria (/api/quality/v1)."""
        from protheus.apis.audit_checklist_v1 import AuditChecklistV1

        return AuditChecklistV1(self)  # type: ignore[arg-type]

    @cached_property
    def audit_panel_v1(self) -> AuditPanelV1:
        """Painel de Auditoria (/api/rh/v1)."""
        from protheus.apis.audit_panel_v1 import AuditPanelV1

        return AuditPanelV1(self)  # type: ignore[arg-type]

    @cached_property
    def audit_questionnaire_v1(self) -> AuditQuestionnaireV1:
        """Questionário de Auditoria (/api/quality/v1)."""
        from protheus.apis.audit_questionnaire_v1 import AuditQuestionnaireV1

        return AuditQuestionnaireV1(self)  # type: ignore[arg-type]

    @cached_property
    def audit_topic_v1(self) -> AuditTopicV1:
        """Tópico de Auditorias (/api/quality/v1)."""
        from protheus.apis.audit_topic_v1 import AuditTopicV1

        return AuditTopicV1(self)  # type: ignore[arg-type]

    @cached_property
    def beneficiaries_coparticipation_v1(self) -> BeneficiariesCoparticipationV1:
        """Relação de Coparticipações dos Beneficiários e seus dependentes - Global (/api/rh/v1)."""
        from protheus.apis.beneficiaries_coparticipation_v1 import BeneficiariesCoparticipationV1

        return BeneficiariesCoparticipationV1(self)  # type: ignore[arg-type]

    @cached_property
    def beneficiaries_data_content_v1(self) -> BeneficiariesDataContentV1:
        """Relação de Benficiários - Global (/api/rh/v1)."""
        from protheus.apis.beneficiaries_data_content_v1 import BeneficiariesDataContentV1

        return BeneficiariesDataContentV1(self)  # type: ignore[arg-type]

    @cached_property
    def budget_balance_type_v1(self) -> BudgetBalanceTypeV1:
        """Tipo de Saldo Orçamentário (/api/pco/v1)."""
        from protheus.apis.budget_balance_type_v1 import BudgetBalanceTypeV1

        return BudgetBalanceTypeV1(self)  # type: ignore[arg-type]

    @cached_property
    def buyers_v1(self) -> BuyersV1:
        """Compradores (/api/supply/v1)."""
        from protheus.apis.buyers_v1 import BuyersV1

        return BuyersV1(self)  # type: ignore[arg-type]

    @cached_property
    def campaigns_v1(self) -> CampaignsV1:
        """Campanhas (/api/crm/v1)."""
        from protheus.apis.campaigns_v1 import CampaignsV1

        return CampaignsV1(self)  # type: ignore[arg-type]

    @cached_property
    def candidates_v2(self) -> CandidatesV2:
        """Candidato (/api/rh/v2)."""
        from protheus.apis.candidates_v2 import CandidatesV2

        return CandidatesV2(self)  # type: ignore[arg-type]

    @cached_property
    def carrier_v1(self) -> CarrierV1:
        """Transportadora (/api/fat/v1)."""
        from protheus.apis.carrier_v1 import CarrierV1

        return CarrierV1(self)  # type: ignore[arg-type]

    @cached_property
    def cashier_operator_v1(self) -> CashierOperatorV1:
        """Operador de Caixa (/api/retail/v1)."""
        from protheus.apis.cashier_operator_v1 import CashierOperatorV1

        return CashierOperatorV1(self)  # type: ignore[arg-type]

    @cached_property
    def cat_report_v1(self) -> CatReportV1:
        """Painel de Impressão da CAT (/api/rh/esocial/v1)."""
        from protheus.apis.cat_report_v1 import CatReportV1

        return CatReportV1(self)  # type: ignore[arg-type]

    @cached_property
    def class_value_v1(self) -> ClassValueV1:
        """Classe de Valor (/api/ctb/v1)."""
        from protheus.apis.class_value_v1 import ClassValueV1

        return ClassValueV1(self)  # type: ignore[arg-type]

    @cached_property
    def commercial_proposal_v1(self) -> CommercialProposalV1:
        """Proposta Comercial (/api/crm/v1)."""
        from protheus.apis.commercial_proposal_v1 import CommercialProposalV1

        return CommercialProposalV1(self)  # type: ignore[arg-type]

    @cached_property
    def contact_relationship_v1(self) -> ContactRelationshipV1:
        """Relacionamento de Contatos x Entidade (/api/crm/v1)."""
        from protheus.apis.contact_relationship_v1 import ContactRelationshipV1

        return ContactRelationshipV1(self)  # type: ignore[arg-type]

    @cached_property
    def contact_v1(self) -> ContactV1:
        """Contatos (/api/crm/contact/v1)."""
        from protheus.apis.contact_v1 import ContactV1

        return ContactV1(self)  # type: ignore[arg-type]

    @cached_property
    def contaminants_v1(self) -> ContaminantsV1:
        """Contaminants (/api/agr/v1)."""
        from protheus.apis.contaminants_v1 import ContaminantsV1

        return ContaminantsV1(self)  # type: ignore[arg-type]

    @cached_property
    def cost_center_v1(self) -> CostCenterV1:
        """Centro de Custo (/api/ctb/v1)."""
        from protheus.apis.cost_center_v1 import CostCenterV1

        return CostCenterV1(self)  # type: ignore[arg-type]

    @cached_property
    def cotton_bales_on_treadmills_v1(self) -> CottonBalesOnTreadmillsV1:
        """CottonBalesOnTreadmills (/api/agr/v1)."""
        from protheus.apis.cotton_bales_on_treadmills_v1 import CottonBalesOnTreadmillsV1

        return CottonBalesOnTreadmillsV1(self)  # type: ignore[arg-type]

    @cached_property
    def cotton_bales_v1(self) -> CottonBalesV1:
        """CottonBales (/api/agr/v1)."""
        from protheus.apis.cotton_bales_v1 import CottonBalesV1

        return CottonBalesV1(self)  # type: ignore[arg-type]

    @cached_property
    def cotton_color_grades_v1(self) -> CottonColorGradesV1:
        """CottonColorGrades (/api/agr/v1)."""
        from protheus.apis.cotton_color_grades_v1 import CottonColorGradesV1

        return CottonColorGradesV1(self)  # type: ignore[arg-type]

    @cached_property
    def cotton_gin_break_pointings_v1(self) -> CottonGinBreakPointingsV1:
        """CottonGinBreakPointings (/api/agr/v1)."""
        from protheus.apis.cotton_gin_break_pointings_v1 import CottonGinBreakPointingsV1

        return CottonGinBreakPointingsV1(self)  # type: ignore[arg-type]

    @cached_property
    def cotton_gin_breaks_v1(self) -> CottonGinBreaksV1:
        """CottonGinBreaks (/api/agr/v1)."""
        from protheus.apis.cotton_gin_breaks_v1 import CottonGinBreaksV1

        return CottonGinBreaksV1(self)  # type: ignore[arg-type]

    @cached_property
    def cotton_gin_machines_v1(self) -> CottonGinMachinesV1:
        """CottonGinMachines (/api/agr/v1)."""
        from protheus.apis.cotton_gin_machines_v1 import CottonGinMachinesV1

        return CottonGinMachinesV1(self)  # type: ignore[arg-type]

    @cached_property
    def cotton_gins_v1(self) -> CottonGinsV1:
        """CottonGins (/api/agr/v1)."""
        from protheus.apis.cotton_gins_v1 import CottonGinsV1

        return CottonGinsV1(self)  # type: ignore[arg-type]

    @cached_property
    def cotton_poisoning_pointings_v1(self) -> CottonPoisoningPointingsV1:
        """CottonPoisoningPointings (/api/agr/v1)."""
        from protheus.apis.cotton_poisoning_pointings_v1 import CottonPoisoningPointingsV1

        return CottonPoisoningPointingsV1(self)  # type: ignore[arg-type]

    @cached_property
    def currency_quote_v1(self) -> CurrencyQuoteV1:
        """Cambio (/api/fin/v1)."""
        from protheus.apis.currency_quote_v1 import CurrencyQuoteV1

        return CurrencyQuoteV1(self)  # type: ignore[arg-type]

    @cached_property
    def customer_credit_limit_v1(self) -> CustomerCreditLimitV1:
        """Limite de credito do Cliente (/api/fat/v1)."""
        from protheus.apis.customer_credit_limit_v1 import CustomerCreditLimitV1

        return CustomerCreditLimitV1(self)  # type: ignore[arg-type]

    @cached_property
    def customer_shipping_address_v1(self) -> CustomerShippingAddressV1:
        """Endereços de Entrega do Cliente (/api/tms/v1)."""
        from protheus.apis.customer_shipping_address_v1 import CustomerShippingAddressV1

        return CustomerShippingAddressV1(self)  # type: ignore[arg-type]

    @cached_property
    def customer_vendor_v1(self) -> CustomerVendorV1:
        """Cliente/Fornecedor (/api/crm/v1)."""
        from protheus.apis.customer_vendor_v1 import CustomerVendorV1

        return CustomerVendorV1(self)  # type: ignore[arg-type]

    @cached_property
    def discovery_environments_v1(self) -> DiscoveryEnvironmentsV1:
        """DiscoveryEnvironments (/api/framework/v1)."""
        from protheus.apis.discovery_environments_v1 import DiscoveryEnvironmentsV1

        return DiscoveryEnvironmentsV1(self)  # type: ignore[arg-type]

    @cached_property
    def discovery_keys_v1(self) -> DiscoveryKeysV1:
        """Chaves de configuracao de stages (/api/framework/v1)."""
        from protheus.apis.discovery_keys_v1 import DiscoveryKeysV1

        return DiscoveryKeysV1(self)  # type: ignore[arg-type]

    @cached_property
    def discovery_stages_v1(self) -> DiscoveryStagesV1:
        """DiscoveryStages (/api/framework/v1)."""
        from protheus.apis.discovery_stages_v1 import DiscoveryStagesV1

        return DiscoveryStagesV1(self)  # type: ignore[arg-type]

    @cached_property
    def documents_v1(self) -> DocumentsV1:
        """Documentos (/api/crm/v1)."""
        from protheus.apis.documents_v1 import DocumentsV1

        return DocumentsV1(self)  # type: ignore[arg-type]

    @cached_property
    def employee_data_content_v1(self) -> EmployeeDataContentV1:
        """Relação de Funcionários - Global (/api/rh/v1)."""
        from protheus.apis.employee_data_content_v1 import EmployeeDataContentV1

        return EmployeeDataContentV1(self)  # type: ignore[arg-type]

    @cached_property
    def employees_manager_data_content_v1(self) -> EmployeesManagerDataContentV1:
        """Líder Direto dos Empregados (/api/rh/v1)."""
        from protheus.apis.employees_manager_data_content_v1 import EmployeesManagerDataContentV1

        return EmployeesManagerDataContentV1(self)  # type: ignore[arg-type]

    @cached_property
    def entities_v1(self) -> EntitiesV1:
        """Entities (/api/agr/v1)."""
        from protheus.apis.entities_v1 import EntitiesV1

        return EntitiesV1(self)  # type: ignore[arg-type]

    @cached_property
    def esocial_audit_v1(self) -> EsocialAuditV1:
        """Painel de Auditoria do eSocial (/api/rh/esocial/v1)."""
        from protheus.apis.esocial_audit_v1 import EsocialAuditV1

        return EsocialAuditV1(self)  # type: ignore[arg-type]

    @cached_property
    def esocial_branches_v1(self) -> EsocialBranchesV1:
        """Filiais (/api/rh/esocial/v1)."""
        from protheus.apis.esocial_branches_v1 import EsocialBranchesV1

        return EsocialBranchesV1(self)  # type: ignore[arg-type]

    @cached_property
    def esocial_establishment_v1(self) -> EsocialEstablishmentV1:
        """S-1005 Estabelecimentos do eSocial (/api/rh/esocial/v1)."""
        from protheus.apis.esocial_establishment_v1 import EsocialEstablishmentV1

        return EsocialEstablishmentV1(self)  # type: ignore[arg-type]

    @cached_property
    def esocial_events_v1(self) -> EsocialEventsV1:
        """Lista de eventos (/api/rh/esocial/v1)."""
        from protheus.apis.esocial_events_v1 import EsocialEventsV1

        return EsocialEventsV1(self)  # type: ignore[arg-type]

    @cached_property
    def events_v1(self) -> EventsV1:
        """Eventos (/api/crm/v1)."""
        from protheus.apis.events_v1 import EventsV1

        return EventsV1(self)  # type: ignore[arg-type]

    @cached_property
    def fgts_per_worker_in_labor_process_v1(self) -> FgtsPerWorkerInLaborProcessV1:
        """Evento Totalizador S-5503 (/api/rh/esocial/v1)."""
        from protheus.apis.fgts_per_worker_in_labor_process_v1 import FgtsPerWorkerInLaborProcessV1

        return FgtsPerWorkerInLaborProcessV1(self)  # type: ignore[arg-type]

    @cached_property
    def freight_accounting_batches_v1(self) -> FreightAccountingBatchesV1:
        """FreightAccountingBatches (/api/gfe/v1)."""
        from protheus.apis.freight_accounting_batches_v1 import FreightAccountingBatchesV1

        return FreightAccountingBatchesV1(self)  # type: ignore[arg-type]

    @cached_property
    def freight_components_v1(self) -> FreightComponentsV1:
        """Freight Components (/api/gfe/v1)."""
        from protheus.apis.freight_components_v1 import FreightComponentsV1

        return FreightComponentsV1(self)  # type: ignore[arg-type]

    @cached_property
    def freight_documents_v1(self) -> FreightDocumentsV1:
        """FreightDocuments (/api/gfe/v1)."""
        from protheus.apis.freight_documents_v1 import FreightDocumentsV1

        return FreightDocumentsV1(self)  # type: ignore[arg-type]

    @cached_property
    def freight_invoices_v1(self) -> FreightInvoicesV1:
        """FreightInvoices (/api/gfe/v1)."""
        from protheus.apis.freight_invoices_v1 import FreightInvoicesV1

        return FreightInvoicesV1(self)  # type: ignore[arg-type]

    @cached_property
    def gpe_esocial_motives_v1(self) -> GpeEsocialMotivesV1:
        """Motivos de Afastamento (/api/rh/esocial/v1)."""
        from protheus.apis.gpe_esocial_motives_v1 import GpeEsocialMotivesV1

        return GpeEsocialMotivesV1(self)  # type: ignore[arg-type]

    @cached_property
    def grain_quality_test_kinds_v1(self) -> GrainQualityTestKindsV1:
        """GrainQualityTestKinds (/api/agr/v1)."""
        from protheus.apis.grain_quality_test_kinds_v1 import GrainQualityTestKindsV1

        return GrainQualityTestKindsV1(self)  # type: ignore[arg-type]

    @cached_property
    def item_reserve_v1(self) -> ItemReserveV1:
        """Reservas de Produto (/api/retail/v1)."""
        from protheus.apis.item_reserve_v1 import ItemReserveV1

        return ItemReserveV1(self)  # type: ignore[arg-type]

    @cached_property
    def job_scheduler_v1_001(self) -> JobSchedulerV1001:
        """Agendamento de Serviço (/api/framework/v1)."""
        from protheus.apis.job_scheduler_v1_001 import JobSchedulerV1001

        return JobSchedulerV1001(self)  # type: ignore[arg-type]

    @cached_property
    def job_scheduler_v1_100(self) -> JobSchedulerV1100:
        """Agendamento de Serviço (/api/framework/v1)."""
        from protheus.apis.job_scheduler_v1_100 import JobSchedulerV1100

        return JobSchedulerV1100(self)  # type: ignore[arg-type]

    @cached_property
    def manifest_v1(self) -> ManifestV1:
        """Manifest (/api/gfe/v1)."""
        from protheus.apis.manifest_v1 import ManifestV1

        return ManifestV1(self)  # type: ignore[arg-type]

    @cached_property
    def market_segment_v2(self) -> MarketSegmentV2:
        """Segmentos de Mercado (/api/services/crm/v2)."""
        from protheus.apis.market_segment_v2 import MarketSegmentV2

        return MarketSegmentV2(self)  # type: ignore[arg-type]

    @cached_property
    def menus_v1(self) -> MenusV1:
        """Menus (/api/framework/v1)."""
        from protheus.apis.menus_v1 import MenusV1

        return MenusV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_allocations_v1(self) -> MrpAllocationsV1:
        """Empenhos da Produção MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_allocations_v1 import MrpAllocationsV1

        return MrpAllocationsV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_bill_of_material_v1(self) -> MrpBillOfMaterialV1:
        """Estruturas do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_bill_of_material_v1 import MrpBillOfMaterialV1

        return MrpBillOfMaterialV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_calendar_v1(self) -> MrpCalendarV1:
        """Calendário do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_calendar_v1 import MrpCalendarV1

        return MrpCalendarV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_demands_v1(self) -> MrpDemandsV1:
        """Demandas do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_demands_v1 import MrpDemandsV1

        return MrpDemandsV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_prod_version_v1(self) -> MrpProdVersionV1:
        """Versão da Produção MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_prod_version_v1 import MrpProdVersionV1

        return MrpProdVersionV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_product_indicator_v1(self) -> MrpProductIndicatorV1:
        """Indicadores do Produto do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_product_indicator_v1 import MrpProductIndicatorV1

        return MrpProductIndicatorV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_product_v1(self) -> MrpProductV1:
        """Produto do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_product_v1 import MrpProductV1

        return MrpProductV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_production_orders_v1(self) -> MrpProductionOrdersV1:
        """Ordens de produção do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_production_orders_v1 import MrpProductionOrdersV1

        return MrpProductionOrdersV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_purchase_order_v1(self) -> MrpPurchaseOrderV1:
        """Solicitação de Compra do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_purchase_order_v1 import MrpPurchaseOrderV1

        return MrpPurchaseOrderV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_purchase_request_v1(self) -> MrpPurchaseRequestV1:
        """Pedido de Compra do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_purchase_request_v1 import MrpPurchaseRequestV1

        return MrpPurchaseRequestV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_rejected_inventory_v1(self) -> MrpRejectedInventoryV1:
        """Estoque Rejeitado do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_rejected_inventory_v1 import MrpRejectedInventoryV1

        return MrpRejectedInventoryV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_routing_v1(self) -> MrpRoutingV1:
        """Roteiro Produtivo do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_routing_v1 import MrpRoutingV1

        return MrpRoutingV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_stock_balance_v1(self) -> MrpStockBalanceV1:
        """Estoque do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_stock_balance_v1 import MrpStockBalanceV1

        return MrpStockBalanceV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_transporting_lanes_v1(self) -> MrpTransportingLanesV1:
        """Malha de Distribuição do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_transporting_lanes_v1 import MrpTransportingLanesV1

        return MrpTransportingLanesV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_ware_house_inventory_policies_v1(self) -> MrpWareHouseInventoryPoliciesV1:
        """Políticas de Estoque por Grupo de Armazém do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_ware_house_inventory_policies_v1 import MrpWareHouseInventoryPoliciesV1

        return MrpWareHouseInventoryPoliciesV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_warehouse_group_v1(self) -> MrpWarehouseGroupV1:
        """Grupo de Armazém do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_warehouse_group_v1 import MrpWarehouseGroupV1

        return MrpWarehouseGroupV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_warehouse_v1(self) -> MrpWarehouseV1:
        """Armazéns do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_warehouse_v1 import MrpWarehouseV1

        return MrpWarehouseV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_work_center_v1(self) -> MrpWorkCenterV1:
        """Centro de trabalho do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_work_center_v1 import MrpWorkCenterV1

        return MrpWorkCenterV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrpbom_routing_v1(self) -> MrpbomRoutingV1:
        """Estrutura por Operação do MRP (/api/pcp/v1)."""
        from protheus.apis.mrpbom_routing_v1 import MrpbomRoutingV1

        return MrpbomRoutingV1(self)  # type: ignore[arg-type]

    @cached_property
    def notes_v1(self) -> NotesV1:
        """Notas (/api/crm/v1)."""
        from protheus.apis.notes_v1 import NotesV1

        return NotesV1(self)  # type: ignore[arg-type]

    @cached_property
    def opportunity_v1(self) -> OpportunityV1:
        """Oportunidades (/api/crm/v1)."""
        from protheus.apis.opportunity_v1 import OpportunityV1

        return OpportunityV1(self)  # type: ignore[arg-type]

    @cached_property
    def payment_condition_v1(self) -> PaymentConditionV1:
        """Condição de Pagamento (/api/fat/v1)."""
        from protheus.apis.payment_condition_v1 import PaymentConditionV1

        return PaymentConditionV1(self)  # type: ignore[arg-type]

    @cached_property
    def payroll_control_v1(self) -> PayrollControlV1:
        """Folha de pagamento para linha de produtos totvs - Global (/api/rh/v1)."""
        from protheus.apis.payroll_control_v1 import PayrollControlV1

        return PayrollControlV1(self)  # type: ignore[arg-type]

    @cached_property
    def price_list_header_item_v2(self) -> PriceListHeaderItemV2:
        """Tabela de Preços (/api/supply/v2)."""
        from protheus.apis.price_list_header_item_v2 import PriceListHeaderItemV2

        return PriceListHeaderItemV2(self)  # type: ignore[arg-type]

    @cached_property
    def prospects_v1(self) -> ProspectsV1:
        """Prospects (/api/crm/v1)."""
        from protheus.apis.prospects_v1 import ProspectsV1

        return ProspectsV1(self)  # type: ignore[arg-type]

    @cached_property
    def purchase_groups_v1(self) -> PurchaseGroupsV1:
        """Grupo de Compras (/api/purchasegroups/v1)."""
        from protheus.apis.purchase_groups_v1 import PurchaseGroupsV1

        return PurchaseGroupsV1(self)  # type: ignore[arg-type]

    @cached_property
    def region_groups_v1(self) -> RegionGroupsV1:
        """Grupo de Região (/api/tms/v1)."""
        from protheus.apis.region_groups_v1 import RegionGroupsV1

        return RegionGroupsV1(self)  # type: ignore[arg-type]

    @cached_property
    def requesters_v1(self) -> RequestersV1:
        """Solicitante (/api/tms/v1)."""
        from protheus.apis.requesters_v1 import RequestersV1

        return RequestersV1(self)  # type: ignore[arg-type]

    @cached_property
    def resource_v1(self) -> ResourceV1:
        """Recursos (/api/sfc/v1)."""
        from protheus.apis.resource_v1 import ResourceV1

        return ResourceV1(self)  # type: ignore[arg-type]

    @cached_property
    def retail_item_v1(self) -> RetailItemV1:
        """Produtos Varejo (/api/retail/v1)."""
        from protheus.apis.retail_item_v1 import RetailItemV1

        return RetailItemV1(self)  # type: ignore[arg-type]

    @cached_property
    def retail_price_list_v1(self) -> RetailPriceListV1:
        """Tabela de Preços Varejo (/api/retail/v1)."""
        from protheus.apis.retail_price_list_v1 import RetailPriceListV1

        return RetailPriceListV1(self)  # type: ignore[arg-type]

    @cached_property
    def retail_sales_orders_v1(self) -> RetailSalesOrdersV1:
        """Pedidos de Venda do Varejo (/api/retail/v1)."""
        from protheus.apis.retail_sales_orders_v1 import RetailSalesOrdersV1

        return RetailSalesOrdersV1(self)  # type: ignore[arg-type]

    @cached_property
    def retail_sales_v1(self) -> RetailSalesV1:
        """Vendas do Varejo (/api/retail/v1)."""
        from protheus.apis.retail_sales_v1 import RetailSalesV1

        return RetailSalesV1(self)  # type: ignore[arg-type]

    @cached_property
    def retail_stock_level_v1(self) -> RetailStockLevelV1:
        """Saldo em Estoque (/api/retail/v1)."""
        from protheus.apis.retail_stock_level_v1 import RetailStockLevelV1

        return RetailStockLevelV1(self)  # type: ignore[arg-type]

    @cached_property
    def roles_v1(self) -> RolesV1:
        """Papeis (/api/framework/v1)."""
        from protheus.apis.roles_v1 import RolesV1

        return RolesV1(self)  # type: ignore[arg-type]

    @cached_property
    def sales_charge_v1(self) -> SalesChargeV1:
        """Comissão de Venda (/api/fat/v1)."""
        from protheus.apis.sales_charge_v1 import SalesChargeV1

        return SalesChargeV1(self)  # type: ignore[arg-type]

    @cached_property
    def sales_process_v1(self) -> SalesProcessV1:
        """Processo de Venda (/api/crm/v1)."""
        from protheus.apis.sales_process_v1 import SalesProcessV1

        return SalesProcessV1(self)  # type: ignore[arg-type]

    @cached_property
    def sales_targets_v1(self) -> SalesTargetsV1:
        """Metas de Vendas (/api/crm/v1)."""
        from protheus.apis.sales_targets_v1 import SalesTargetsV1

        return SalesTargetsV1(self)  # type: ignore[arg-type]

    @cached_property
    def sales_taxes_v1(self) -> SalesTaxesV1:
        """Impostos do Pedido de Venda (/api/fat/v1)."""
        from protheus.apis.sales_taxes_v1 import SalesTaxesV1

        return SalesTaxesV1(self)  # type: ignore[arg-type]

    @cached_property
    def seller_activity_v1(self) -> SellerActivityV1:
        """Atividade do Vendedor (/api/crm/v1)."""
        from protheus.apis.seller_activity_v1 import SellerActivityV1

        return SellerActivityV1(self)  # type: ignore[arg-type]

    @cached_property
    def sellers_v2(self) -> SellersV2:
        """Vendedor (/api/crm/v2)."""
        from protheus.apis.sellers_v2 import SellersV2

        return SellersV2(self)  # type: ignore[arg-type]

    @cached_property
    def stop_reason_v1(self) -> StopReasonV1:
        """Motivo de Parada (/api/pcp/v1)."""
        from protheus.apis.stop_reason_v1 import StopReasonV1

        return StopReasonV1(self)  # type: ignore[arg-type]

    @cached_property
    def stop_report_v1(self) -> StopReportV1:
        """Apontamentos de Parada (/api/pcp/v1)."""
        from protheus.apis.stop_report_v1 import StopReportV1

        return StopReportV1(self)  # type: ignore[arg-type]

    @cached_property
    def suspects_v1(self) -> SuspectsV1:
        """Suspects (/api/crm/v1)."""
        from protheus.apis.suspects_v1 import SuspectsV1

        return SuspectsV1(self)  # type: ignore[arg-type]

    @cached_property
    def system_modules_v1(self) -> SystemModulesV1:
        """Módulos do sistema (/api/framework/v1)."""
        from protheus.apis.system_modules_v1 import SystemModulesV1

        return SystemModulesV1(self)  # type: ignore[arg-type]

    @cached_property
    def system_parameter_v1(self) -> SystemParameterV1:
        """Parametros de Sistema (/api/framework/v1)."""
        from protheus.apis.system_parameter_v1 import SystemParameterV1

        return SystemParameterV1(self)  # type: ignore[arg-type]

    @cached_property
    def taf_esocial_remove_company_v1(self) -> TafEsocialRemoveCompanyV1:
        """TAF e-Social - Remover empregador da base de dados do RET (/api/rh/esocial/v1)."""
        from protheus.apis.taf_esocial_remove_company_v1 import TafEsocialRemoveCompanyV1

        return TafEsocialRemoveCompanyV1(self)  # type: ignore[arg-type]

    @cached_property
    def token_v1(self) -> TokenV1:
        """Token (/api/oauth2/v1)."""
        from protheus.apis.token_v1 import TokenV1

        return TokenV1(self)  # type: ignore[arg-type]

    @cached_property
    def total_input_document_v1(self) -> TotalInputDocumentV1:
        """Total de Nota de Entrada (/api/retail/v1)."""
        from protheus.apis.total_input_document_v1 import TotalInputDocumentV1

        return TotalInputDocumentV1(self)  # type: ignore[arg-type]

    @cached_property
    def total_output_document_v1(self) -> TotalOutputDocumentV1:
        """Total de Nota de Saída (/api/retail/v1)."""
        from protheus.apis.total_output_document_v1 import TotalOutputDocumentV1

        return TotalOutputDocumentV1(self)  # type: ignore[arg-type]

    @cached_property
    def treadmills_v1(self) -> TreadmillsV1:
        """Treadmills (/api/agr/v1)."""
        from protheus.apis.treadmills_v1 import TreadmillsV1

        return TreadmillsV1(self)  # type: ignore[arg-type]

    @cached_property
    def tsi_branches_v1(self) -> TsiBranchesV1:
        """Lista de filiais do grupo de empresas (/api/tsi/v1)."""
        from protheus.apis.tsi_branches_v1 import TsiBranchesV1

        return TsiBranchesV1(self)  # type: ignore[arg-type]

    @cached_property
    def tsi_integration_errors_v1(self) -> TsiIntegrationErrorsV1:
        """Consulta os erros da integração TSI (/api/tsi/v1)."""
        from protheus.apis.tsi_integration_errors_v1 import TsiIntegrationErrorsV1

        return TsiIntegrationErrorsV1(self)  # type: ignore[arg-type]

    @cached_property
    def tsi_service_status_v1(self) -> TsiServiceStatusV1:
        """Consulta o status do serviço (/api/tsi/v1)."""
        from protheus.apis.tsi_service_status_v1 import TsiServiceStatusV1

        return TsiServiceStatusV1(self)  # type: ignore[arg-type]

    @cached_property
    def unit_of_measure_v1(self) -> UnitOfMeasureV1:
        """Unidade de Medida (/api/entradas/v1)."""
        from protheus.apis.unit_of_measure_v1 import UnitOfMeasureV1

        return UnitOfMeasureV1(self)  # type: ignore[arg-type]

    @cached_property
    def unit_of_measure_v2(self) -> UnitOfMeasureV2:
        """Unidade de Medida (/api/supply/v2)."""
        from protheus.apis.unit_of_measure_v2 import UnitOfMeasureV2

        return UnitOfMeasureV2(self)  # type: ignore[arg-type]

    @cached_property
    def urbano_coletor_v1(self) -> UrbanoColetorV1:
        """Coletor (/api/coletorurbano/coletor)."""
        from protheus.apis.urbano_coletor_v1 import UrbanoColetorV1

        return UrbanoColetorV1(self)  # type: ignore[arg-type]

    @cached_property
    def user_v1(self) -> UserV1:
        """Usuário (/api/framework/v1)."""
        from protheus.apis.user_v1 import UserV1

        return UserV1(self)  # type: ignore[arg-type]

    @cached_property
    def waste_reason_v1(self) -> WasteReasonV1:
        """Motivos de Refugo (/api/pcp/v1)."""
        from protheus.apis.waste_reason_v1 import WasteReasonV1

        return WasteReasonV1(self)  # type: ignore[arg-type]


class AsyncApis:
    """Lazy per-API accessors; mixed into the async client."""

    @cached_property
    def accounting_calendar_v1(self) -> AsyncAccountingCalendarV1:
        """Calendário Contábil (/api/ctb/v1)."""
        from protheus.apis.accounting_calendar_v1 import AsyncAccountingCalendarV1

        return AsyncAccountingCalendarV1(self)  # type: ignore[arg-type]

    @cached_property
    def accounting_items_v1(self) -> AsyncAccountingItemsV1:
        """Item Contábil (/api/ctb/v1)."""
        from protheus.apis.accounting_items_v1 import AsyncAccountingItemsV1

        return AsyncAccountingItemsV1(self)  # type: ignore[arg-type]

    @cached_property
    def address_stock_v1(self) -> AsyncAddressStockV1:
        """Endereços (/api/entradas/v1)."""
        from protheus.apis.address_stock_v1 import AsyncAddressStockV1

        return AsyncAddressStockV1(self)  # type: ignore[arg-type]

    @cached_property
    def annotation_v1(self) -> AsyncAnnotationV1:
        """Apontamento de Visita (/api/crm/v1)."""
        from protheus.apis.annotation_v1 import AsyncAnnotationV1

        return AsyncAnnotationV1(self)  # type: ignore[arg-type]

    @cached_property
    def approval_profile_v1(self) -> AsyncApprovalProfileV1:
        """Perfil de Aprovação (/api/framework/v1)."""
        from protheus.apis.approval_profile_v1 import AsyncApprovalProfileV1

        return AsyncApprovalProfileV1(self)  # type: ignore[arg-type]

    @cached_property
    def approval_profile_v2(self) -> AsyncApprovalProfileV2:
        """Perfil/Grade de Aprovação (/api/supply/v2)."""
        from protheus.apis.approval_profile_v2 import AsyncApprovalProfileV2

        return AsyncApprovalProfileV2(self)  # type: ignore[arg-type]

    @cached_property
    def approvers_v1(self) -> AsyncApproversV1:
        """Aprovadores (/api/supply/v1)."""
        from protheus.apis.approvers_v1 import AsyncApproversV1

        return AsyncApproversV1(self)  # type: ignore[arg-type]

    @cached_property
    def audit_checklist_v1(self) -> AsyncAuditChecklistV1:
        """Checklist de Auditoria (/api/quality/v1)."""
        from protheus.apis.audit_checklist_v1 import AsyncAuditChecklistV1

        return AsyncAuditChecklistV1(self)  # type: ignore[arg-type]

    @cached_property
    def audit_panel_v1(self) -> AsyncAuditPanelV1:
        """Painel de Auditoria (/api/rh/v1)."""
        from protheus.apis.audit_panel_v1 import AsyncAuditPanelV1

        return AsyncAuditPanelV1(self)  # type: ignore[arg-type]

    @cached_property
    def audit_questionnaire_v1(self) -> AsyncAuditQuestionnaireV1:
        """Questionário de Auditoria (/api/quality/v1)."""
        from protheus.apis.audit_questionnaire_v1 import AsyncAuditQuestionnaireV1

        return AsyncAuditQuestionnaireV1(self)  # type: ignore[arg-type]

    @cached_property
    def audit_topic_v1(self) -> AsyncAuditTopicV1:
        """Tópico de Auditorias (/api/quality/v1)."""
        from protheus.apis.audit_topic_v1 import AsyncAuditTopicV1

        return AsyncAuditTopicV1(self)  # type: ignore[arg-type]

    @cached_property
    def beneficiaries_coparticipation_v1(self) -> AsyncBeneficiariesCoparticipationV1:
        """Relação de Coparticipações dos Beneficiários e seus dependentes - Global (/api/rh/v1)."""
        from protheus.apis.beneficiaries_coparticipation_v1 import AsyncBeneficiariesCoparticipationV1

        return AsyncBeneficiariesCoparticipationV1(self)  # type: ignore[arg-type]

    @cached_property
    def beneficiaries_data_content_v1(self) -> AsyncBeneficiariesDataContentV1:
        """Relação de Benficiários - Global (/api/rh/v1)."""
        from protheus.apis.beneficiaries_data_content_v1 import AsyncBeneficiariesDataContentV1

        return AsyncBeneficiariesDataContentV1(self)  # type: ignore[arg-type]

    @cached_property
    def budget_balance_type_v1(self) -> AsyncBudgetBalanceTypeV1:
        """Tipo de Saldo Orçamentário (/api/pco/v1)."""
        from protheus.apis.budget_balance_type_v1 import AsyncBudgetBalanceTypeV1

        return AsyncBudgetBalanceTypeV1(self)  # type: ignore[arg-type]

    @cached_property
    def buyers_v1(self) -> AsyncBuyersV1:
        """Compradores (/api/supply/v1)."""
        from protheus.apis.buyers_v1 import AsyncBuyersV1

        return AsyncBuyersV1(self)  # type: ignore[arg-type]

    @cached_property
    def campaigns_v1(self) -> AsyncCampaignsV1:
        """Campanhas (/api/crm/v1)."""
        from protheus.apis.campaigns_v1 import AsyncCampaignsV1

        return AsyncCampaignsV1(self)  # type: ignore[arg-type]

    @cached_property
    def candidates_v2(self) -> AsyncCandidatesV2:
        """Candidato (/api/rh/v2)."""
        from protheus.apis.candidates_v2 import AsyncCandidatesV2

        return AsyncCandidatesV2(self)  # type: ignore[arg-type]

    @cached_property
    def carrier_v1(self) -> AsyncCarrierV1:
        """Transportadora (/api/fat/v1)."""
        from protheus.apis.carrier_v1 import AsyncCarrierV1

        return AsyncCarrierV1(self)  # type: ignore[arg-type]

    @cached_property
    def cashier_operator_v1(self) -> AsyncCashierOperatorV1:
        """Operador de Caixa (/api/retail/v1)."""
        from protheus.apis.cashier_operator_v1 import AsyncCashierOperatorV1

        return AsyncCashierOperatorV1(self)  # type: ignore[arg-type]

    @cached_property
    def cat_report_v1(self) -> AsyncCatReportV1:
        """Painel de Impressão da CAT (/api/rh/esocial/v1)."""
        from protheus.apis.cat_report_v1 import AsyncCatReportV1

        return AsyncCatReportV1(self)  # type: ignore[arg-type]

    @cached_property
    def class_value_v1(self) -> AsyncClassValueV1:
        """Classe de Valor (/api/ctb/v1)."""
        from protheus.apis.class_value_v1 import AsyncClassValueV1

        return AsyncClassValueV1(self)  # type: ignore[arg-type]

    @cached_property
    def commercial_proposal_v1(self) -> AsyncCommercialProposalV1:
        """Proposta Comercial (/api/crm/v1)."""
        from protheus.apis.commercial_proposal_v1 import AsyncCommercialProposalV1

        return AsyncCommercialProposalV1(self)  # type: ignore[arg-type]

    @cached_property
    def contact_relationship_v1(self) -> AsyncContactRelationshipV1:
        """Relacionamento de Contatos x Entidade (/api/crm/v1)."""
        from protheus.apis.contact_relationship_v1 import AsyncContactRelationshipV1

        return AsyncContactRelationshipV1(self)  # type: ignore[arg-type]

    @cached_property
    def contact_v1(self) -> AsyncContactV1:
        """Contatos (/api/crm/contact/v1)."""
        from protheus.apis.contact_v1 import AsyncContactV1

        return AsyncContactV1(self)  # type: ignore[arg-type]

    @cached_property
    def contaminants_v1(self) -> AsyncContaminantsV1:
        """Contaminants (/api/agr/v1)."""
        from protheus.apis.contaminants_v1 import AsyncContaminantsV1

        return AsyncContaminantsV1(self)  # type: ignore[arg-type]

    @cached_property
    def cost_center_v1(self) -> AsyncCostCenterV1:
        """Centro de Custo (/api/ctb/v1)."""
        from protheus.apis.cost_center_v1 import AsyncCostCenterV1

        return AsyncCostCenterV1(self)  # type: ignore[arg-type]

    @cached_property
    def cotton_bales_on_treadmills_v1(self) -> AsyncCottonBalesOnTreadmillsV1:
        """CottonBalesOnTreadmills (/api/agr/v1)."""
        from protheus.apis.cotton_bales_on_treadmills_v1 import AsyncCottonBalesOnTreadmillsV1

        return AsyncCottonBalesOnTreadmillsV1(self)  # type: ignore[arg-type]

    @cached_property
    def cotton_bales_v1(self) -> AsyncCottonBalesV1:
        """CottonBales (/api/agr/v1)."""
        from protheus.apis.cotton_bales_v1 import AsyncCottonBalesV1

        return AsyncCottonBalesV1(self)  # type: ignore[arg-type]

    @cached_property
    def cotton_color_grades_v1(self) -> AsyncCottonColorGradesV1:
        """CottonColorGrades (/api/agr/v1)."""
        from protheus.apis.cotton_color_grades_v1 import AsyncCottonColorGradesV1

        return AsyncCottonColorGradesV1(self)  # type: ignore[arg-type]

    @cached_property
    def cotton_gin_break_pointings_v1(self) -> AsyncCottonGinBreakPointingsV1:
        """CottonGinBreakPointings (/api/agr/v1)."""
        from protheus.apis.cotton_gin_break_pointings_v1 import AsyncCottonGinBreakPointingsV1

        return AsyncCottonGinBreakPointingsV1(self)  # type: ignore[arg-type]

    @cached_property
    def cotton_gin_breaks_v1(self) -> AsyncCottonGinBreaksV1:
        """CottonGinBreaks (/api/agr/v1)."""
        from protheus.apis.cotton_gin_breaks_v1 import AsyncCottonGinBreaksV1

        return AsyncCottonGinBreaksV1(self)  # type: ignore[arg-type]

    @cached_property
    def cotton_gin_machines_v1(self) -> AsyncCottonGinMachinesV1:
        """CottonGinMachines (/api/agr/v1)."""
        from protheus.apis.cotton_gin_machines_v1 import AsyncCottonGinMachinesV1

        return AsyncCottonGinMachinesV1(self)  # type: ignore[arg-type]

    @cached_property
    def cotton_gins_v1(self) -> AsyncCottonGinsV1:
        """CottonGins (/api/agr/v1)."""
        from protheus.apis.cotton_gins_v1 import AsyncCottonGinsV1

        return AsyncCottonGinsV1(self)  # type: ignore[arg-type]

    @cached_property
    def cotton_poisoning_pointings_v1(self) -> AsyncCottonPoisoningPointingsV1:
        """CottonPoisoningPointings (/api/agr/v1)."""
        from protheus.apis.cotton_poisoning_pointings_v1 import AsyncCottonPoisoningPointingsV1

        return AsyncCottonPoisoningPointingsV1(self)  # type: ignore[arg-type]

    @cached_property
    def currency_quote_v1(self) -> AsyncCurrencyQuoteV1:
        """Cambio (/api/fin/v1)."""
        from protheus.apis.currency_quote_v1 import AsyncCurrencyQuoteV1

        return AsyncCurrencyQuoteV1(self)  # type: ignore[arg-type]

    @cached_property
    def customer_credit_limit_v1(self) -> AsyncCustomerCreditLimitV1:
        """Limite de credito do Cliente (/api/fat/v1)."""
        from protheus.apis.customer_credit_limit_v1 import AsyncCustomerCreditLimitV1

        return AsyncCustomerCreditLimitV1(self)  # type: ignore[arg-type]

    @cached_property
    def customer_shipping_address_v1(self) -> AsyncCustomerShippingAddressV1:
        """Endereços de Entrega do Cliente (/api/tms/v1)."""
        from protheus.apis.customer_shipping_address_v1 import AsyncCustomerShippingAddressV1

        return AsyncCustomerShippingAddressV1(self)  # type: ignore[arg-type]

    @cached_property
    def customer_vendor_v1(self) -> AsyncCustomerVendorV1:
        """Cliente/Fornecedor (/api/crm/v1)."""
        from protheus.apis.customer_vendor_v1 import AsyncCustomerVendorV1

        return AsyncCustomerVendorV1(self)  # type: ignore[arg-type]

    @cached_property
    def discovery_environments_v1(self) -> AsyncDiscoveryEnvironmentsV1:
        """DiscoveryEnvironments (/api/framework/v1)."""
        from protheus.apis.discovery_environments_v1 import AsyncDiscoveryEnvironmentsV1

        return AsyncDiscoveryEnvironmentsV1(self)  # type: ignore[arg-type]

    @cached_property
    def discovery_keys_v1(self) -> AsyncDiscoveryKeysV1:
        """Chaves de configuracao de stages (/api/framework/v1)."""
        from protheus.apis.discovery_keys_v1 import AsyncDiscoveryKeysV1

        return AsyncDiscoveryKeysV1(self)  # type: ignore[arg-type]

    @cached_property
    def discovery_stages_v1(self) -> AsyncDiscoveryStagesV1:
        """DiscoveryStages (/api/framework/v1)."""
        from protheus.apis.discovery_stages_v1 import AsyncDiscoveryStagesV1

        return AsyncDiscoveryStagesV1(self)  # type: ignore[arg-type]

    @cached_property
    def documents_v1(self) -> AsyncDocumentsV1:
        """Documentos (/api/crm/v1)."""
        from protheus.apis.documents_v1 import AsyncDocumentsV1

        return AsyncDocumentsV1(self)  # type: ignore[arg-type]

    @cached_property
    def employee_data_content_v1(self) -> AsyncEmployeeDataContentV1:
        """Relação de Funcionários - Global (/api/rh/v1)."""
        from protheus.apis.employee_data_content_v1 import AsyncEmployeeDataContentV1

        return AsyncEmployeeDataContentV1(self)  # type: ignore[arg-type]

    @cached_property
    def employees_manager_data_content_v1(self) -> AsyncEmployeesManagerDataContentV1:
        """Líder Direto dos Empregados (/api/rh/v1)."""
        from protheus.apis.employees_manager_data_content_v1 import AsyncEmployeesManagerDataContentV1

        return AsyncEmployeesManagerDataContentV1(self)  # type: ignore[arg-type]

    @cached_property
    def entities_v1(self) -> AsyncEntitiesV1:
        """Entities (/api/agr/v1)."""
        from protheus.apis.entities_v1 import AsyncEntitiesV1

        return AsyncEntitiesV1(self)  # type: ignore[arg-type]

    @cached_property
    def esocial_audit_v1(self) -> AsyncEsocialAuditV1:
        """Painel de Auditoria do eSocial (/api/rh/esocial/v1)."""
        from protheus.apis.esocial_audit_v1 import AsyncEsocialAuditV1

        return AsyncEsocialAuditV1(self)  # type: ignore[arg-type]

    @cached_property
    def esocial_branches_v1(self) -> AsyncEsocialBranchesV1:
        """Filiais (/api/rh/esocial/v1)."""
        from protheus.apis.esocial_branches_v1 import AsyncEsocialBranchesV1

        return AsyncEsocialBranchesV1(self)  # type: ignore[arg-type]

    @cached_property
    def esocial_establishment_v1(self) -> AsyncEsocialEstablishmentV1:
        """S-1005 Estabelecimentos do eSocial (/api/rh/esocial/v1)."""
        from protheus.apis.esocial_establishment_v1 import AsyncEsocialEstablishmentV1

        return AsyncEsocialEstablishmentV1(self)  # type: ignore[arg-type]

    @cached_property
    def esocial_events_v1(self) -> AsyncEsocialEventsV1:
        """Lista de eventos (/api/rh/esocial/v1)."""
        from protheus.apis.esocial_events_v1 import AsyncEsocialEventsV1

        return AsyncEsocialEventsV1(self)  # type: ignore[arg-type]

    @cached_property
    def events_v1(self) -> AsyncEventsV1:
        """Eventos (/api/crm/v1)."""
        from protheus.apis.events_v1 import AsyncEventsV1

        return AsyncEventsV1(self)  # type: ignore[arg-type]

    @cached_property
    def fgts_per_worker_in_labor_process_v1(self) -> AsyncFgtsPerWorkerInLaborProcessV1:
        """Evento Totalizador S-5503 (/api/rh/esocial/v1)."""
        from protheus.apis.fgts_per_worker_in_labor_process_v1 import AsyncFgtsPerWorkerInLaborProcessV1

        return AsyncFgtsPerWorkerInLaborProcessV1(self)  # type: ignore[arg-type]

    @cached_property
    def freight_accounting_batches_v1(self) -> AsyncFreightAccountingBatchesV1:
        """FreightAccountingBatches (/api/gfe/v1)."""
        from protheus.apis.freight_accounting_batches_v1 import AsyncFreightAccountingBatchesV1

        return AsyncFreightAccountingBatchesV1(self)  # type: ignore[arg-type]

    @cached_property
    def freight_components_v1(self) -> AsyncFreightComponentsV1:
        """Freight Components (/api/gfe/v1)."""
        from protheus.apis.freight_components_v1 import AsyncFreightComponentsV1

        return AsyncFreightComponentsV1(self)  # type: ignore[arg-type]

    @cached_property
    def freight_documents_v1(self) -> AsyncFreightDocumentsV1:
        """FreightDocuments (/api/gfe/v1)."""
        from protheus.apis.freight_documents_v1 import AsyncFreightDocumentsV1

        return AsyncFreightDocumentsV1(self)  # type: ignore[arg-type]

    @cached_property
    def freight_invoices_v1(self) -> AsyncFreightInvoicesV1:
        """FreightInvoices (/api/gfe/v1)."""
        from protheus.apis.freight_invoices_v1 import AsyncFreightInvoicesV1

        return AsyncFreightInvoicesV1(self)  # type: ignore[arg-type]

    @cached_property
    def gpe_esocial_motives_v1(self) -> AsyncGpeEsocialMotivesV1:
        """Motivos de Afastamento (/api/rh/esocial/v1)."""
        from protheus.apis.gpe_esocial_motives_v1 import AsyncGpeEsocialMotivesV1

        return AsyncGpeEsocialMotivesV1(self)  # type: ignore[arg-type]

    @cached_property
    def grain_quality_test_kinds_v1(self) -> AsyncGrainQualityTestKindsV1:
        """GrainQualityTestKinds (/api/agr/v1)."""
        from protheus.apis.grain_quality_test_kinds_v1 import AsyncGrainQualityTestKindsV1

        return AsyncGrainQualityTestKindsV1(self)  # type: ignore[arg-type]

    @cached_property
    def item_reserve_v1(self) -> AsyncItemReserveV1:
        """Reservas de Produto (/api/retail/v1)."""
        from protheus.apis.item_reserve_v1 import AsyncItemReserveV1

        return AsyncItemReserveV1(self)  # type: ignore[arg-type]

    @cached_property
    def job_scheduler_v1_001(self) -> AsyncJobSchedulerV1001:
        """Agendamento de Serviço (/api/framework/v1)."""
        from protheus.apis.job_scheduler_v1_001 import AsyncJobSchedulerV1001

        return AsyncJobSchedulerV1001(self)  # type: ignore[arg-type]

    @cached_property
    def job_scheduler_v1_100(self) -> AsyncJobSchedulerV1100:
        """Agendamento de Serviço (/api/framework/v1)."""
        from protheus.apis.job_scheduler_v1_100 import AsyncJobSchedulerV1100

        return AsyncJobSchedulerV1100(self)  # type: ignore[arg-type]

    @cached_property
    def manifest_v1(self) -> AsyncManifestV1:
        """Manifest (/api/gfe/v1)."""
        from protheus.apis.manifest_v1 import AsyncManifestV1

        return AsyncManifestV1(self)  # type: ignore[arg-type]

    @cached_property
    def market_segment_v2(self) -> AsyncMarketSegmentV2:
        """Segmentos de Mercado (/api/services/crm/v2)."""
        from protheus.apis.market_segment_v2 import AsyncMarketSegmentV2

        return AsyncMarketSegmentV2(self)  # type: ignore[arg-type]

    @cached_property
    def menus_v1(self) -> AsyncMenusV1:
        """Menus (/api/framework/v1)."""
        from protheus.apis.menus_v1 import AsyncMenusV1

        return AsyncMenusV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_allocations_v1(self) -> AsyncMrpAllocationsV1:
        """Empenhos da Produção MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_allocations_v1 import AsyncMrpAllocationsV1

        return AsyncMrpAllocationsV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_bill_of_material_v1(self) -> AsyncMrpBillOfMaterialV1:
        """Estruturas do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_bill_of_material_v1 import AsyncMrpBillOfMaterialV1

        return AsyncMrpBillOfMaterialV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_calendar_v1(self) -> AsyncMrpCalendarV1:
        """Calendário do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_calendar_v1 import AsyncMrpCalendarV1

        return AsyncMrpCalendarV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_demands_v1(self) -> AsyncMrpDemandsV1:
        """Demandas do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_demands_v1 import AsyncMrpDemandsV1

        return AsyncMrpDemandsV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_prod_version_v1(self) -> AsyncMrpProdVersionV1:
        """Versão da Produção MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_prod_version_v1 import AsyncMrpProdVersionV1

        return AsyncMrpProdVersionV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_product_indicator_v1(self) -> AsyncMrpProductIndicatorV1:
        """Indicadores do Produto do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_product_indicator_v1 import AsyncMrpProductIndicatorV1

        return AsyncMrpProductIndicatorV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_product_v1(self) -> AsyncMrpProductV1:
        """Produto do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_product_v1 import AsyncMrpProductV1

        return AsyncMrpProductV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_production_orders_v1(self) -> AsyncMrpProductionOrdersV1:
        """Ordens de produção do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_production_orders_v1 import AsyncMrpProductionOrdersV1

        return AsyncMrpProductionOrdersV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_purchase_order_v1(self) -> AsyncMrpPurchaseOrderV1:
        """Solicitação de Compra do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_purchase_order_v1 import AsyncMrpPurchaseOrderV1

        return AsyncMrpPurchaseOrderV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_purchase_request_v1(self) -> AsyncMrpPurchaseRequestV1:
        """Pedido de Compra do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_purchase_request_v1 import AsyncMrpPurchaseRequestV1

        return AsyncMrpPurchaseRequestV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_rejected_inventory_v1(self) -> AsyncMrpRejectedInventoryV1:
        """Estoque Rejeitado do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_rejected_inventory_v1 import AsyncMrpRejectedInventoryV1

        return AsyncMrpRejectedInventoryV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_routing_v1(self) -> AsyncMrpRoutingV1:
        """Roteiro Produtivo do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_routing_v1 import AsyncMrpRoutingV1

        return AsyncMrpRoutingV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_stock_balance_v1(self) -> AsyncMrpStockBalanceV1:
        """Estoque do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_stock_balance_v1 import AsyncMrpStockBalanceV1

        return AsyncMrpStockBalanceV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_transporting_lanes_v1(self) -> AsyncMrpTransportingLanesV1:
        """Malha de Distribuição do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_transporting_lanes_v1 import AsyncMrpTransportingLanesV1

        return AsyncMrpTransportingLanesV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_ware_house_inventory_policies_v1(self) -> AsyncMrpWareHouseInventoryPoliciesV1:
        """Políticas de Estoque por Grupo de Armazém do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_ware_house_inventory_policies_v1 import AsyncMrpWareHouseInventoryPoliciesV1

        return AsyncMrpWareHouseInventoryPoliciesV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_warehouse_group_v1(self) -> AsyncMrpWarehouseGroupV1:
        """Grupo de Armazém do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_warehouse_group_v1 import AsyncMrpWarehouseGroupV1

        return AsyncMrpWarehouseGroupV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_warehouse_v1(self) -> AsyncMrpWarehouseV1:
        """Armazéns do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_warehouse_v1 import AsyncMrpWarehouseV1

        return AsyncMrpWarehouseV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrp_work_center_v1(self) -> AsyncMrpWorkCenterV1:
        """Centro de trabalho do MRP (/api/pcp/v1)."""
        from protheus.apis.mrp_work_center_v1 import AsyncMrpWorkCenterV1

        return AsyncMrpWorkCenterV1(self)  # type: ignore[arg-type]

    @cached_property
    def mrpbom_routing_v1(self) -> AsyncMrpbomRoutingV1:
        """Estrutura por Operação do MRP (/api/pcp/v1)."""
        from protheus.apis.mrpbom_routing_v1 import AsyncMrpbomRoutingV1

        return AsyncMrpbomRoutingV1(self)  # type: ignore[arg-type]

    @cached_property
    def notes_v1(self) -> AsyncNotesV1:
        """Notas (/api/crm/v1)."""
        from protheus.apis.notes_v1 import AsyncNotesV1

        return AsyncNotesV1(self)  # type: ignore[arg-type]

    @cached_property
    def opportunity_v1(self) -> AsyncOpportunityV1:
        """Oportunidades (/api/crm/v1)."""
        from protheus.apis.opportunity_v1 import AsyncOpportunityV1

        return AsyncOpportunityV1(self)  # type: ignore[arg-type]

    @cached_property
    def payment_condition_v1(self) -> AsyncPaymentConditionV1:
        """Condição de Pagamento (/api/fat/v1)."""
        from protheus.apis.payment_condition_v1 import AsyncPaymentConditionV1

        return AsyncPaymentConditionV1(self)  # type: ignore[arg-type]

    @cached_property
    def payroll_control_v1(self) -> AsyncPayrollControlV1:
        """Folha de pagamento para linha de produtos totvs - Global (/api/rh/v1)."""
        from protheus.apis.payroll_control_v1 import AsyncPayrollControlV1

        return AsyncPayrollControlV1(self)  # type: ignore[arg-type]

    @cached_property
    def price_list_header_item_v2(self) -> AsyncPriceListHeaderItemV2:
        """Tabela de Preços (/api/supply/v2)."""
        from protheus.apis.price_list_header_item_v2 import AsyncPriceListHeaderItemV2

        return AsyncPriceListHeaderItemV2(self)  # type: ignore[arg-type]

    @cached_property
    def prospects_v1(self) -> AsyncProspectsV1:
        """Prospects (/api/crm/v1)."""
        from protheus.apis.prospects_v1 import AsyncProspectsV1

        return AsyncProspectsV1(self)  # type: ignore[arg-type]

    @cached_property
    def purchase_groups_v1(self) -> AsyncPurchaseGroupsV1:
        """Grupo de Compras (/api/purchasegroups/v1)."""
        from protheus.apis.purchase_groups_v1 import AsyncPurchaseGroupsV1

        return AsyncPurchaseGroupsV1(self)  # type: ignore[arg-type]

    @cached_property
    def region_groups_v1(self) -> AsyncRegionGroupsV1:
        """Grupo de Região (/api/tms/v1)."""
        from protheus.apis.region_groups_v1 import AsyncRegionGroupsV1

        return AsyncRegionGroupsV1(self)  # type: ignore[arg-type]

    @cached_property
    def requesters_v1(self) -> AsyncRequestersV1:
        """Solicitante (/api/tms/v1)."""
        from protheus.apis.requesters_v1 import AsyncRequestersV1

        return AsyncRequestersV1(self)  # type: ignore[arg-type]

    @cached_property
    def resource_v1(self) -> AsyncResourceV1:
        """Recursos (/api/sfc/v1)."""
        from protheus.apis.resource_v1 import AsyncResourceV1

        return AsyncResourceV1(self)  # type: ignore[arg-type]

    @cached_property
    def retail_item_v1(self) -> AsyncRetailItemV1:
        """Produtos Varejo (/api/retail/v1)."""
        from protheus.apis.retail_item_v1 import AsyncRetailItemV1

        return AsyncRetailItemV1(self)  # type: ignore[arg-type]

    @cached_property
    def retail_price_list_v1(self) -> AsyncRetailPriceListV1:
        """Tabela de Preços Varejo (/api/retail/v1)."""
        from protheus.apis.retail_price_list_v1 import AsyncRetailPriceListV1

        return AsyncRetailPriceListV1(self)  # type: ignore[arg-type]

    @cached_property
    def retail_sales_orders_v1(self) -> AsyncRetailSalesOrdersV1:
        """Pedidos de Venda do Varejo (/api/retail/v1)."""
        from protheus.apis.retail_sales_orders_v1 import AsyncRetailSalesOrdersV1

        return AsyncRetailSalesOrdersV1(self)  # type: ignore[arg-type]

    @cached_property
    def retail_sales_v1(self) -> AsyncRetailSalesV1:
        """Vendas do Varejo (/api/retail/v1)."""
        from protheus.apis.retail_sales_v1 import AsyncRetailSalesV1

        return AsyncRetailSalesV1(self)  # type: ignore[arg-type]

    @cached_property
    def retail_stock_level_v1(self) -> AsyncRetailStockLevelV1:
        """Saldo em Estoque (/api/retail/v1)."""
        from protheus.apis.retail_stock_level_v1 import AsyncRetailStockLevelV1

        return AsyncRetailStockLevelV1(self)  # type: ignore[arg-type]

    @cached_property
    def roles_v1(self) -> AsyncRolesV1:
        """Papeis (/api/framework/v1)."""
        from protheus.apis.roles_v1 import AsyncRolesV1

        return AsyncRolesV1(self)  # type: ignore[arg-type]

    @cached_property
    def sales_charge_v1(self) -> AsyncSalesChargeV1:
        """Comissão de Venda (/api/fat/v1)."""
        from protheus.apis.sales_charge_v1 import AsyncSalesChargeV1

        return AsyncSalesChargeV1(self)  # type: ignore[arg-type]

    @cached_property
    def sales_process_v1(self) -> AsyncSalesProcessV1:
        """Processo de Venda (/api/crm/v1)."""
        from protheus.apis.sales_process_v1 import AsyncSalesProcessV1

        return AsyncSalesProcessV1(self)  # type: ignore[arg-type]

    @cached_property
    def sales_targets_v1(self) -> AsyncSalesTargetsV1:
        """Metas de Vendas (/api/crm/v1)."""
        from protheus.apis.sales_targets_v1 import AsyncSalesTargetsV1

        return AsyncSalesTargetsV1(self)  # type: ignore[arg-type]

    @cached_property
    def sales_taxes_v1(self) -> AsyncSalesTaxesV1:
        """Impostos do Pedido de Venda (/api/fat/v1)."""
        from protheus.apis.sales_taxes_v1 import AsyncSalesTaxesV1

        return AsyncSalesTaxesV1(self)  # type: ignore[arg-type]

    @cached_property
    def seller_activity_v1(self) -> AsyncSellerActivityV1:
        """Atividade do Vendedor (/api/crm/v1)."""
        from protheus.apis.seller_activity_v1 import AsyncSellerActivityV1

        return AsyncSellerActivityV1(self)  # type: ignore[arg-type]

    @cached_property
    def sellers_v2(self) -> AsyncSellersV2:
        """Vendedor (/api/crm/v2)."""
        from protheus.apis.sellers_v2 import AsyncSellersV2

        return AsyncSellersV2(self)  # type: ignore[arg-type]

    @cached_property
    def stop_reason_v1(self) -> AsyncStopReasonV1:
        """Motivo de Parada (/api/pcp/v1)."""
        from protheus.apis.stop_reason_v1 import AsyncStopReasonV1

        return AsyncStopReasonV1(self)  # type: ignore[arg-type]

    @cached_property
    def stop_report_v1(self) -> AsyncStopReportV1:
        """Apontamentos de Parada (/api/pcp/v1)."""
        from protheus.apis.stop_report_v1 import AsyncStopReportV1

        return AsyncStopReportV1(self)  # type: ignore[arg-type]

    @cached_property
    def suspects_v1(self) -> AsyncSuspectsV1:
        """Suspects (/api/crm/v1)."""
        from protheus.apis.suspects_v1 import AsyncSuspectsV1

        return AsyncSuspectsV1(self)  # type: ignore[arg-type]

    @cached_property
    def system_modules_v1(self) -> AsyncSystemModulesV1:
        """Módulos do sistema (/api/framework/v1)."""
        from protheus.apis.system_modules_v1 import AsyncSystemModulesV1

        return AsyncSystemModulesV1(self)  # type: ignore[arg-type]

    @cached_property
    def system_parameter_v1(self) -> AsyncSystemParameterV1:
        """Parametros de Sistema (/api/framework/v1)."""
        from protheus.apis.system_parameter_v1 import AsyncSystemParameterV1

        return AsyncSystemParameterV1(self)  # type: ignore[arg-type]

    @cached_property
    def taf_esocial_remove_company_v1(self) -> AsyncTafEsocialRemoveCompanyV1:
        """TAF e-Social - Remover empregador da base de dados do RET (/api/rh/esocial/v1)."""
        from protheus.apis.taf_esocial_remove_company_v1 import AsyncTafEsocialRemoveCompanyV1

        return AsyncTafEsocialRemoveCompanyV1(self)  # type: ignore[arg-type]

    @cached_property
    def token_v1(self) -> AsyncTokenV1:
        """Token (/api/oauth2/v1)."""
        from protheus.apis.token_v1 import AsyncTokenV1

        return AsyncTokenV1(self)  # type: ignore[arg-type]

    @cached_property
    def total_input_document_v1(self) -> AsyncTotalInputDocumentV1:
        """Total de Nota de Entrada (/api/retail/v1)."""
        from protheus.apis.total_input_document_v1 import AsyncTotalInputDocumentV1

        return AsyncTotalInputDocumentV1(self)  # type: ignore[arg-type]

    @cached_property
    def total_output_document_v1(self) -> AsyncTotalOutputDocumentV1:
        """Total de Nota de Saída (/api/retail/v1)."""
        from protheus.apis.total_output_document_v1 import AsyncTotalOutputDocumentV1

        return AsyncTotalOutputDocumentV1(self)  # type: ignore[arg-type]

    @cached_property
    def treadmills_v1(self) -> AsyncTreadmillsV1:
        """Treadmills (/api/agr/v1)."""
        from protheus.apis.treadmills_v1 import AsyncTreadmillsV1

        return AsyncTreadmillsV1(self)  # type: ignore[arg-type]

    @cached_property
    def tsi_branches_v1(self) -> AsyncTsiBranchesV1:
        """Lista de filiais do grupo de empresas (/api/tsi/v1)."""
        from protheus.apis.tsi_branches_v1 import AsyncTsiBranchesV1

        return AsyncTsiBranchesV1(self)  # type: ignore[arg-type]

    @cached_property
    def tsi_integration_errors_v1(self) -> AsyncTsiIntegrationErrorsV1:
        """Consulta os erros da integração TSI (/api/tsi/v1)."""
        from protheus.apis.tsi_integration_errors_v1 import AsyncTsiIntegrationErrorsV1

        return AsyncTsiIntegrationErrorsV1(self)  # type: ignore[arg-type]

    @cached_property
    def tsi_service_status_v1(self) -> AsyncTsiServiceStatusV1:
        """Consulta o status do serviço (/api/tsi/v1)."""
        from protheus.apis.tsi_service_status_v1 import AsyncTsiServiceStatusV1

        return AsyncTsiServiceStatusV1(self)  # type: ignore[arg-type]

    @cached_property
    def unit_of_measure_v1(self) -> AsyncUnitOfMeasureV1:
        """Unidade de Medida (/api/entradas/v1)."""
        from protheus.apis.unit_of_measure_v1 import AsyncUnitOfMeasureV1

        return AsyncUnitOfMeasureV1(self)  # type: ignore[arg-type]

    @cached_property
    def unit_of_measure_v2(self) -> AsyncUnitOfMeasureV2:
        """Unidade de Medida (/api/supply/v2)."""
        from protheus.apis.unit_of_measure_v2 import AsyncUnitOfMeasureV2

        return AsyncUnitOfMeasureV2(self)  # type: ignore[arg-type]

    @cached_property
    def urbano_coletor_v1(self) -> AsyncUrbanoColetorV1:
        """Coletor (/api/coletorurbano/coletor)."""
        from protheus.apis.urbano_coletor_v1 import AsyncUrbanoColetorV1

        return AsyncUrbanoColetorV1(self)  # type: ignore[arg-type]

    @cached_property
    def user_v1(self) -> AsyncUserV1:
        """Usuário (/api/framework/v1)."""
        from protheus.apis.user_v1 import AsyncUserV1

        return AsyncUserV1(self)  # type: ignore[arg-type]

    @cached_property
    def waste_reason_v1(self) -> AsyncWasteReasonV1:
        """Motivos de Refugo (/api/pcp/v1)."""
        from protheus.apis.waste_reason_v1 import AsyncWasteReasonV1

        return AsyncWasteReasonV1(self)  # type: ignore[arg-type]
