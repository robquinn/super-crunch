from io import StringIO

import numpy as np
import pandas as pd

from .. import logger
from ..constants import CLOSED, OFFICE, PENDING, TRANSACTION_TYPES
from .fields import Fields
from .replace import (
    replace_agent,
    replace_da_title_company,
    replace_mi_mortagage_company,
    replace_offices,
    replace_outside_brokerage_agent,
    replace_tags,
)


class Transactions:
    def __init__(
        self,
        api_response: StringIO,
        fields: Fields,
        type: TRANSACTION_TYPES,
    ) -> None:
        self.df = pd.read_csv(api_response, delimiter=",")
        self.type = type
        self.fields = fields

    def __len__(self):
        return len(self.df)

    def get_dataframe(self) -> pd.DataFrame:
        return self.df

    def change_column_names(self) -> None:
        logger.info("Changing Column Names")
        self.df.columns = [x.lower() for x in self.df.columns]
        self.df.columns = self.df.columns.to_series().apply(lambda x: x.strip())
        self.df.columns = self.df.columns.str.replace("[./]", "", regex=True)
        self.df.columns = self.df.columns.str.replace("\\s+", " ", regex=True)
        self.df.columns = self.df.columns.str.replace("[ ]", "_", regex=True)

    def cast_columns(self) -> None:
        logger.info("Casting Column Values")

        def numeric_fields() -> None:
            columns = self.fields["numeric"]

            self.df[columns] = self.df[columns].replace("[$,%]", "", regex=True)

            self.df[columns] = self.df[columns].apply(
                lambda x: pd.to_numeric(x, errors="coerce")
            )
            self.df[columns] = self.df[columns].replace(np.nan, 0, regex=True)

        def date_fields() -> None:
            columns = self.fields["date"]

            # self.df[columns] = self.df[columns].apply(
            #     lambda x: pd.Series(x, dtype="string")
            # )
            self.df[columns] = self.df[columns].replace("-", None, regex=False)
            self.df[columns] = self.df[columns].apply(
                lambda x: pd.to_datetime(x).dt.date
            )
            self.df[columns] = self.df[columns].replace(np.nan, None, regex=True)

        def json_fields() -> None:
            columns = self.fields["json"]

            self.df[columns] = self.df[columns].apply(
                lambda x: pd.Series(x, dtype="string").replace("[]", None, regex=False)
            )

        def str_fields() -> None:
            columns = self.fields["string"]

            self.df[columns] = self.df[columns].apply(
                lambda x: pd.Series(x, dtype="string")
            )
            self.df[columns] = self.df[columns].replace(np.nan, None, regex=True)

        def boolean_fields() -> None:
            columns = self.fields["boolean"]

            self.df[columns] = self.df[columns].apply(
                lambda x: pd.Series(x, dtype="bool")
            )
            self.df[columns] = (
                self.df[columns]
                .replace(".*(Y|y)(E|e)(S|s).*", True, regex=True)
                .replace(".*(N|n)(O|o).*", False, regex=True)
                .replace(np.nan, None, regex=True)
            )

        if self.fields["numeric"] is not None:
            numeric_fields()
        if self.fields["date"] is not None:
            date_fields()
        if self.fields["json"] is not None:
            json_fields()
        if self.fields["string"] is not None:
            str_fields()
        if self.fields["boolean"] is not None:
            boolean_fields()

    def transform_columns(self) -> None:
        logger.info("Transforming Column Values")

        def offices() -> None:
            columns = self.fields["office"]
            if columns is not None:
                self.df[columns] = replace_offices(
                    columns=columns, df=self.get_dataframe()
                )

        def office_agent() -> None:
            columns = ["agent"]
            self.df[columns] = replace_agent(columns=columns, df=self.get_dataframe())

        def office_tags() -> None:
            columns = ["tags"]
            self.df[columns] = replace_tags(columns=columns, df=self.get_dataframe())

        def pending_and_closed_outside_brokerage_agent() -> None:
            columns = ["outside_brokerage_agent"]
            self.df[columns] = replace_outside_brokerage_agent(
                columns=columns, df=self.df
            )

        def pending_and_closed_mi_mortagage_company() -> None:
            columns = ["mi_mortgage_company"]
            self.df[columns] = replace_mi_mortagage_company(
                columns=columns, df=self.get_dataframe()
            )

        def pending_and_closed_da_title_company() -> None:
            columns = ["da_title_company"]
            self.df[columns] = replace_da_title_company(
                columns=columns, df=self.get_dataframe()
            )

        if self.fields["office"] is not None:
            offices()
        if self.type == OFFICE:
            office_tags()
            office_agent()
        if self.type == CLOSED or self.type == PENDING:
            pending_and_closed_outside_brokerage_agent()
            pending_and_closed_mi_mortagage_company()
            pending_and_closed_da_title_company()
