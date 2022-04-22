from sqlalchemy import delete, select
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models.models import Series
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

    

    def buscar(self, serie_id: int):
        stmt = select(models.Series).filter_by(id = serie_id)
        serie = self.db.execute(stmt).one()
        return serie
       
    def remover(self, serie_id: int):
            stmt = delete(models.Series).where(models.Series.id == serie_id)
            self.db.execute(stmt)
            self.db.commit()
            