from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from .base import Base


class DBConnectionHandler:
    def __init__(self):
        self.__engine = create_engine(getenv("SQLALCHEMY_STRING_DATABASE"), echo=False)
        self.session: Session = None
        self.__create_table()

    def __create_table(self):
        Base.metadata.create_all(bind=self.__engine, checkfirst=True)

    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
