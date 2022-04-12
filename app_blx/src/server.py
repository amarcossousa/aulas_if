from fastapi import FastAPI, Depends
from src.infra.sqlalchemy.config.database import criar_db, get_db
from src.schema.schemas import Produto
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto


criar_db()

app = FastAPI()

@app.post('/produtos')
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@app.get('/produtos')
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos
    