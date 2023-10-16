from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from src.settings import config
from src.models import Base


class Repository:
    engine = create_engine(config.sqlalchemy_url)

    def add_object(self, obj: Base):
        with Session(self.engine) as session:
            session.add(obj)
            session.commit()

    def get_object(self, model, **kwargs):
        """
        :param model: sqlalchemy model class
        :param kwargs: filters for fetch object
        :return:
        """
        with Session(self.engine) as session:
            statement = select(model).filter_by(**kwargs)
            return session.execute(statement).first()
