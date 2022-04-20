from fastapi import FastAPI, Depends
from src.infra.sqlalchemy.config.database import criar_db, get_db
from src.schema import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.series import RepositorioSeries 

app = FastAPI()

criar_db()

@app.post('/series')
def criar_serie(serie: schemas.Series, db: Session = Depends(get_db) ):
    serie_criada = RepositorioSeries(db).criar(serie)
    return serie_criada


@app.get('/series')
def listar_serie(db: Session = Depends(get_db)):
    return RepositorioSeries(db).listar()