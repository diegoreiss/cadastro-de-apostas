from sqlalchemy import Column, Integer, String
from ..config.base import Base


class Resultado(Base):
    __tablename__ = "resultado"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    gols_da_casa = Column(Integer, nullable=False)
    gols_do_visitante = Column(Integer, nullable=False)
    vencedor = Column(String(10), nullable=True)

    def __repr__(self):
        return f"Resultado(id={self.id}, " \
               f"gols_da_casa={self.gols_da_casa}, " \
               f"gols_do_visitante={self.gols_do_visitante}, vencedor={self.vencedor})"

