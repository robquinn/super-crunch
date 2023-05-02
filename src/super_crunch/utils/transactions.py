from typing import Literal

import numpy as np
import pandas as pd

from .. import logger


class Transactions:
    def __init__(self, api_response, type) -> None:
        self.df = pd.read_csv(api_response, delimiter=",")
        self.type = type

    def __len__(self):
        return len(self.df)

    def get_dataframe(self) -> pd.DataFrame:
        return self.df

    def change_column_names(self) -> None:
        logger.info("Changing Column Names")
        self.df.columns = [x.lower() for x in self.df.columns]
        self.df.columns = self.df.columns.to_series().apply(lambda x: x.strip())
        self.df.columns = self.df.columns.str.replace("[ ]", "_", regex=True)

    def cast_columns(self) -> pd.DataFrame:
        logger.info("Casting Column Values")

        def numeric_fields() -> None:
            columns = [
                "zip",
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
            self.df[columns] = self.df[columns].apply(
                lambda x: pd.to_numeric(x, errors="coerce")
            )
            self.df[columns] = self.df[columns].replace(np.nan, 0, regex=True)

        def datetime_fields() -> None:
            columns = [
                "contract_date",
                "date_created",
            ]
            if self.type == "closed":
                columns.append("closed_date")
            elif self.type == "pending":
                columns.append("estimated_close_date")

            self.df[columns] = self.df[columns].apply(
                lambda x: pd.Series(x, dtype="string")
            )
            self.df[columns] = self.df[columns].replace(np.nan, None, regex=True)

        def json_fields() -> None:
            columns = [
                "referrals",
            ]

            self.df[columns] = self.df[columns].apply(
                lambda x: pd.Series(x, dtype="string").replace("[]", None, regex=False)
            )

        def str_fields() -> None:
            columns = [
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

            self.df[columns] = self.df[columns].apply(
                lambda x: pd.Series(x, dtype="string")
            )
            self.df[columns] = self.df[columns].replace(np.nan, None, regex=True)

        numeric_fields()
        datetime_fields()
        json_fields()
        str_fields()

    def transform_columns(self) -> pd.DataFrame:
        logger.info("Transforming Column Values")

        def offices() -> pd.DataFrame:
            columns = ["listing_office", "buying_office"]
            self.df[columns] = (
                self.df[columns]
                .replace(to_replace="\\s*\\-.*", value="", regex=True)
                .replace(to_replace="SE Valley", value="Southeast Valley")
                .replace(to_replace="Desert Mtn", value="Desert Mountain")
            )

            def tag_in_tags(
                tag: Literal["Relo", "FH"],
                col_val: Literal["Relocation", "Fountain Hills"],
                index: int,
                cols_to_replace: tuple[
                    Literal["listing_office"], Literal["buying_office"]
                ] = ["listing_office", "buying_office"],
                tag_col: str = "tags",
            ) -> None:
                if (
                    not pd.isna(self.df.at[index, tag_col])
                    and tag in self.df.at[index, tag_col]
                ):
                    for col in cols_to_replace:
                        if not pd.isna(self.df.at[index, col]):
                            self.df.at[index, col] = col_val

            for index, row in self.df.iterrows():
                tag_in_tags(tag="FH", col_val="Fountain Hills", index=index)
                tag_in_tags(tag="Relo", col_val="Relocation", index=index)

        def outside_brokerage_agent() -> pd.DataFrame:
            columns = ["outside_brokerage_agent"]
            self.df[columns] = (
                self.df[columns]
                .replace(to_replace=".*NA", value=None, regex=True)
                .replace(to_replace=".*None.*", value=None, regex=True)
            )

        offices()
        outside_brokerage_agent()
