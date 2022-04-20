from sqlalchemy.orm import Session
from src.schema import schemas
from src.infra.sqlalchemy.models import models


class RepositorioSeries():

    def __init__(self, db: Session):
        self.db = db

    
    def criar(self, series: schemas.Series): # importado de schemas 
        db_series = models.Series (titulo = series.titulo,
                                    ano = series.ano,
                                    genero = series.genero,
                                    qtd_temporadas = series.qtd_temporadas)
        self.db.add(db_series)
        self.db.commit()
        self.db.refresh(db_series)
        return db_series
        


    def listar(self):
        series = self.db.query(models.Series).all()
        return series

    def remover(self):
        pass

    def buscar(self):
        pass
