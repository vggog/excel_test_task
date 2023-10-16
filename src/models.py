from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    ...


class Goods(Base):
    __tablename__ = "goods"

    id_tovar: Mapped[int] = mapped_column(primary_key=True)
    name_tovar: Mapped[str]
    barcod: Mapped[Optional[str]]
    id_country: Mapped[int] = mapped_column(ForeignKey("country.id_country"))
    id_isg: Mapped[int] = mapped_column(ForeignKey("isg.id_isg"))
    country: Mapped["Country"] = relationship()
    isg: Mapped["ISG"] = relationship()

    def __repr__(self):
        return (
            f"id_tovar={self.id_tovar} "
            f"name_tovar={self.name_tovar} "
            f"barcod={self.barcod} "
            f"id_country={self.id_country}"
            f"id_isg={self.id_isg}"
        )


class Country(Base):
    __tablename__ = "country"

    id_country: Mapped[int] = mapped_column(primary_key=True)
    name_country: Mapped[str]

    def __repr__(self):
        return f"id_country={self.id_country} name_country={self.name_country}"


class ISG(Base):
    __tablename__ = "isg"

    id_isg: Mapped[int] = mapped_column(primary_key=True)
    name_isg: Mapped[str]

    def __repr__(self):
        return f"id_isg={self.id_isg} name_isg={self.name_isg}"
