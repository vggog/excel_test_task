from dataclasses import dataclass


@dataclass
class Config:
    excel_file_path: str


@dataclass
class RowValues:
    id_tovar: int
    tovar: str
    id_isg: int
    isg: str
    country: str
    barcode: int
