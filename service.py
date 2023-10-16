from sqlalchemy.exc import IntegrityError

from repository import Repository
from models import Country, Goods, ISG
from schemas import RowValues


class Service:
    repo = Repository()

    def inserting_to_db(self, data: RowValues):
        """
        Inserting datas, if data doesn't exist.
        :param data:
        :return:
        """
        country = self.get_or_create_country(data)
        self.create_isg(data)
        self.create_goods(data, country)

    def get_or_create_country(self, data: RowValues) -> tuple[Country]:
        """
        Insert country into db, if country doesn't exist and return it.
        :param data:
        :return:
        """
        country = self.repo.get_object(Country, name_country=data.country)

        if country:
            return country

        country_created_obj = Country(name_country=data.country)
        self.add_object_to_db(country_created_obj)

        return self.repo.get_object(Country, name_country=data.country)

    def create_isg(self, data: RowValues):
        """
        Insert isg into db if it doesn't exist.
        :param data:
        :return:
        """
        if self.repo.get_object(ISG, id_isg=data.id_isg):
            return

        isg_created_obj = ISG(id_isg=data.id_isg, name_isg=data.isg)
        self.add_object_to_db(isg_created_obj)

    def create_goods(self, data: RowValues, country: tuple[Country]):
        """
        Insert product into db if it doesn't exist.
        :param data:
        :param country:
        :return:
        """
        if self.repo.get_object(Goods, id_tovar=data.id_tovar):
            return

        goods_created_obj = Goods(
            id_tovar=data.id_tovar,
            name_tovar=data.tovar,
            barcod=str(data.barcode),
            id_isg=data.id_isg,
            id_country=country[0].id_country,
        )
        self.add_object_to_db(goods_created_obj)

    def add_object_to_db(self, created_object):
        """
        Insert object into db.
        :param created_object:
        :return:
        """
        try:
            self.repo.add_object(created_object)
        except IntegrityError:
            print(created_object)
            print("Неверный тип данных для вставки в таблицу.")
