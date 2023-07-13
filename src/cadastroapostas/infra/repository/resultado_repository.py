from ..config.connection import DBConnectionHandler
from ..model.resultado import Resultado


class ResultadoRepository:
    @staticmethod
    def insert(**resultado):
        data_insert = Resultado(**resultado)

        with DBConnectionHandler() as db:
            try:
                db.session.add(data_insert)
                db.session.commit()
                db.session.refresh(data_insert)

                return data_insert
            except BaseException as e:
                db.session.rollback()
                raise e
