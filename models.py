from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class Goods(Base):
    __tablename__ = "goods"

    id_tovar: Mapped[int] = mapped_column(primary_key=True)
    name_tovar: Mapped[str]
    barcod: Mapped[str]
    id_country: Mapped[int] = mapped_column(ForeignKey("country.id_country"))
    id_isg: Mapped[int] = mapped_column(ForeignKey("isg.id_isg"))


class Country(Base):
    __tablename__ = "country"

    id_country: Mapped[int] = mapped_column(primary_key=True)
    country: Mapped[str]


class ISG(Base):
    __tablename__ = "isg"

    id_isg: Mapped[int] = mapped_column(primary_key=True)
    country: Mapped[str]
