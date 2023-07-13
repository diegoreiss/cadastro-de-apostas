from sqlalchemy import Column, String, Integer
from ..config.base import Base


class Apostador(Base):
    __tablename__ = "apostador"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = Column(String(40), nullable=False)
    valor = Column(String(40), unique=True, nullable=False)
