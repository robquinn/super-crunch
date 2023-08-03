import re
from typing import Hashable, List, Literal

import pandas as pd


def replace_mi_mortagage_company(columns: List[str], df: pd.DataFrame) -> pd.DataFrame:
    return df[columns].apply(
        lambda x: pd.Series(x, dtype="string")
        .replace(r"^ +| +$", r"", regex=True)
        .str.replace(
            pat=r"United\s*Wholesale\s*Mortgage.*",
            repl="United Wholesale Mortgage LLC",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Fairway\s*Independent\s*Mortgage.*",
            repl="Fairway Independent Mortgage",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Cross\s*Country\s*Mortgage.*",
            repl="Cross Country Mortgage LLC",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Rocket\s*Mortgage.*",
            repl="Rocket Mortgage LLC",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Navy\s*Federal\s*Credit\s*Union.*",
            repl="Navy Federal Credit Union",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Nova\s*Home\s*Loans.*",
            repl="Nova Home Loans",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"VIP\s*Mortgage.*", repl="VIP Mortgage", regex=True, flags=re.I
        )
        .str.replace(
            pat=r"SWBC\s*Mortgage.*",
            repl="SWBC Mortgage Coporation",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Loan\s*Depot\s*\\.com.*",
            repl="LoanDepot.com LLC",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Bank\s*of\s*America.*",
            repl="Bank of America",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Prime\s*Lending.*", repl="PrimeLending", regex=True, flags=re.I
        )
        .str.replace(
            pat=r"Equitable\s*Home\s*Mortgage.*",
            repl="Equitable Home Mortgage",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Wells\s*Fargo.*", repl="Wells Fargo Bank", regex=True, flags=re.I
        )
        .str.replace(
            pat=r"Barrett\s*Financial\s*Group.*",
            repl="Barrett Financial Group",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"BOK\s*Financial\s*Mortgage.*",
            repl="BOK Financial Mortgage",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Azben\s*Limited.*",
            repl="Azben Limited LLC",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Academy\s*Mortgage.*",
            repl="Academy Mortgage Coporation",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Morgan\s*Stanley.*",
            repl="Morgan Stanley Private Bank",
            regex=True,
            flags=re.I,
        )
        .str.replace(pat=r"\s*NP\s*Inc.*", repl="NP Inc", regex=True, flags=re.I)
        .str.replace(
            pat=r"CMG\s*Mortgage.*",
            repl="CMG Mortgage Inc",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"American\s*Pacific.*",
            repl="American Pacific Mortgage Coporation",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Movement\s*Mortgage.*",
            repl="Movement Mortgage LLC",
            regex=True,
            flags=re.I,
        )
        .str.replace(pat=r"US\s*Bank.*", repl="US Bank", regex=True, flags=re.I)
        .str.replace(
            pat=r"MidFirst\s*Bank.*", repl="MidFirst Bank", regex=True, flags=re.I
        )
    )


def replace_da_title_company(columns: List[str], df: pd.DataFrame) -> pd.DataFrame:
    return df[columns].apply(
        lambda x: pd.Series(x, dtype="object")
        .replace(r"^ +| +$", r"", regex=True)
        .str.replace(
            r"Arizona\s*Premier\s*Title.*",
            "Arizona Premier Title Agency",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"First\s*American.*",
            repl="First American Insurance Company",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Pioneer\s*Title.*",
            repl="Pioneer Title Agency",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Fidelity\s*National\s*Title.*",
            repl="Fidelity National Title Agency",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Title\s*Security.*",
            repl="Title Security Agency",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Lawyers\s*Title.*", repl="Lawyers Title", regex=True, flags=re.I
        )
        .str.replace(
            pat=r"Empire\s*West\s*Title.*",
            repl="Empire West Title Agency",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Stewart\s*Title.*",
            repl="Stewart Title & Trust",
            regex=True,
            flags=re.I,
        )
        .str.replace(pat=r"Navi\s*Title.*", repl="Navi Title", regex=True, flags=re.I)
        .str.replace(
            pat=r"Equity\s*Title.*",
            repl="Equity Title Agency",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"WFG\s*National\s*Title.*",
            repl="WFG National Title Insurance Company",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Premier\s*Title.*",
            repl="Premier Title Agency",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Security\s*Title.*",
            repl="Security Title Agency",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Carefree\s*Title.*",
            repl="Carefree Title Agency Inc",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Magnus\s*Title.*",
            repl="Magnus Title Agency",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Chicago\s*Title.*",
            repl="Chicago Title Agency",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"American\s*Title.*",
            repl="American Title Service Agency",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Old\s*Republic\s*Title.*",
            repl="Old Republic Title",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Greystone\s*Title.*",
            repl="Greystone Title Agency",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Great\s*American\s*Title.*",
            repl="Great American Title Agency",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Driggs\s*Title.*",
            repl="Driggs Title Agency",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Landmark\s*Title\s*Assurance.*",
            repl="Landmark Title Assurance Agency",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"First\s*Arizona\s*Title.*",
            repl="First Arizona Title Agency",
            regex=True,
            flags=re.I,
        )
        .str.replace(pat=r"PGP\s*Title.*", repl="PGP Title Inc", regex=True, flags=re.I)
        .str.replace(
            pat=r"Lennar\s*Title.*", repl="Lennar Title", regex=True, flags=re.I
        )
        .str.replace(
            pat=r"Title\s*Alliance\s*Professionals.*",
            repl="Title Alliance Professionals",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"Clear\s*Title\s*Agency.*",
            repl="Clear Title Agency of Arizona",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"GH\s*Title\s*Arizona.*",
            repl="GH Title Arizona LLC",
            regex=True,
            flags=re.I,
        )
        .str.replace(
            pat=r"DHI\s*Title.*", repl="DHI Title Agency", regex=True, flags=re.I
        )
        .str.replace(
            pat=r"Tri\s*Pointe\s*Assurance.*",
            repl="Tri Point Assurance",
            regex=True,
            flags=re.I,
        )
    )


def replace_outside_brokerage_agent(
    columns: List[str], df: pd.DataFrame
) -> pd.DataFrame:
    return (
        df[columns]
        .replace(to_replace=".*NA", value=None, regex=True)
        .replace(to_replace=".*None.*", value=None, regex=True)
    )


def replace_offices(columns: List[str], df: pd.DataFrame) -> pd.DataFrame:
    df[columns] = (
        df[columns]
        .replace(to_replace="\\s*\\-.*", value="", regex=True)
        .replace(to_replace="SE Valley", value="Southeast Valley")
        .replace(to_replace="Desert Mtn", value="Desert Mountain")
    )

    def tag_in_tags(
        tag: Literal["Relo", "FH"],
        col_val: Literal["Relocation", "Fountain Hills"],
        index: Hashable,
        cols_to_replace: List[str],
        tag_col: str = "tags",
    ) -> None:
        if not pd.isna(df.at[index, tag_col]) and tag in df.at[index, tag_col]:
            for col in cols_to_replace:
                if not pd.isna(df.at[index, col]):
                    df.at[index, col] = col_val

    for index, row in df.iterrows():
        tag_in_tags(
            tag="FH",
            col_val="Fountain Hills",
            index=index,
            cols_to_replace=columns,
        )
        tag_in_tags(
            tag="Relo",
            col_val="Relocation",
            index=index,
            cols_to_replace=columns,
        )

    return df[columns]


def replace_agent(columns: List[str], df: pd.DataFrame) -> pd.DataFrame:
    return df[columns].replace(
        to_replace="(Listing|Buying|Other)\\s+", value="", regex=True
    )


def replace_tags(columns: List[str], df: pd.DataFrame) -> pd.DataFrame:
    return df[columns].replace(to_replace="-", value=None, regex=True)
