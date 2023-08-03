from typing import List, TypedDict


class Fields(TypedDict):
    numeric: List[str] | None
    date: List[str] | None
    json: List[str] | None
    string: List[str] | None
    boolean: List[str] | None
    office: List[str] | None
