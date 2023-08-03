from typing import List

from ..constants import CLOSED, FORECAST, OFFICE, PENDING, TRANSACTION_TYPES


class Columns:
    def __init__(self, type: TRANSACTION_TYPES) -> None:
        self.type = type

    def numeric(self) -> List[str] | None:
        if self.type == CLOSED or self.type == PENDING:
            return [
                "listing_price",
                "sale_price",
                "listing_side_gross_commission",
                "listing_side_agent_net",
                "listing_side_brokerage_net",
                "buying_side_gross_commission",
                "buying_side_agent_net",
                "buying_side_brokerage_net",
                "total_gross_commission",
                "total_agent_net",
                "total_brokerage_net",
            ]
        elif self.type == OFFICE:
            return [
                "sales_price",
                "sales_volume",
                "side_cnt",
                "gci",
                "eff_rate",
                "adj_gci",
                "agent_gross",
                "agent_net",
                "brokerage_gross",
                "brokerage_net",
            ]
        elif self.type == FORECAST:
            return [
                "sales_price",
                "sales_volume",
                "gci",
                "referral",
                "adj_gci",
                "agent_net",
                "brokerage_gross",
                "brokerage_net",
            ]
        else:
            return None

    def date(self) -> List[str] | None:
        if self.type == CLOSED:
            return [
                "contract_date",
                "date_created",
            ]
        elif self.type == PENDING:
            return ["contract_date", "date_created"]
        elif self.type == OFFICE:
            return ["close_date"]
        elif self.type == FORECAST:
            return ["contract_date", "close_date"]
        else:
            return None

    def json(self) -> List[str] | None:
        if self.type == CLOSED or self.type == PENDING:
            return [
                "referrals",
            ]
        elif self.type == OFFICE:
            return None
        elif self.type == FORECAST:
            return None
        else:
            return None

    def boolean(self) -> List[str] | None:
        if self.type == CLOSED or self.type == PENDING:
            return None
        elif self.type == OFFICE:
            return None
        elif self.type == FORECAST:
            return None
        else:
            return None

    def string(self) -> List[str] | None:
        if self.type == CLOSED or self.type == PENDING:
            return [
                "zip",
                "transaction_id",
                "property_address",
                "address_line1",
                "address_line2",
                "city",
                "state",
                "property_type",
                "property_subtype",
                "mls_number",
                "seller_name",
                "seller_email",
                "buyer_name",
                "buyer_email",
                "outside_brokerage_name",
                "outside_brokerage_agent",
                "outside_brokerage_agent_email",
                "seller_source",
                "seller_lead",
                "buyer_source",
                "buyer_lead",
                "listing_office",
                "listing_agent_identifier",
                "listing_agent_name",
                "listing_agent_email",
                "buying_office",
                "buying_agent_identifier",
                "buying_agent_name",
                "buying_agent_email",
                "da_title_company",
                "da_closer_name",
                "da_mailing_address",
                "da_phone",
                "da_email",
                "mi_mortgage_company",
                "mi_lender_name",
                "mi_mailing_address",
                "mi_phone",
                "mi_email",
                "tags",
            ]
        elif self.type == OFFICE:
            return ["zipcode", "type", "agent", "office", "tags"]
        elif self.type == FORECAST:
            return [
                "property_address",
                "accounting_status",
                "trans_type",
                "tags",
                "listing_buying_agent",
            ]
        else:
            return None

    def office(self) -> List[str] | None:
        if self.type == CLOSED or self.type == PENDING:
            return ["listing_office", "buying_office"]
        elif self.type == OFFICE or self.type == FORECAST:
            return ["office"]
        else:
            return None
