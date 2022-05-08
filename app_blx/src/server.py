from genericpath import exists
from fastapi import FastAPI, Depends, status
from src.infra.sqlalchemy.config.database import criar_db, get_db
from src.schema.schemas import Produto, ProdutoSimples, Usuario
from sqlalchemy.orm import Session
from typing import List
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario


criar_db()

app = FastAPI()

# Produtos
@app.post('/produtos/', status_code=status.HTTP_201_CREATED, response_model=ProdutoSimples)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@app.get('/produtos/', status_code=status.HTTP_202_ACCEPTED, response_model=List[Produto])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@app.delete('/produto/{produto_id}')
def remover(produto_id: int, db:Session = Depends(get_db)):
    RepositorioProduto(db).remover(produto_id)
    return {'msg': 'Produto excluido com sucesso! '}

@app.put('/produtos/', status_code=status.HTTP_202_ACCEPTED)
def editar_produto(produto: Produto, session: Session = Depends(get_db)):
    RepositorioProduto(session).editar(produto)
    return produto

@app.get('/produto/{produto_id}')
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = RepositorioProduto(db).obter(produto_id)
    return produto

# USUARIOS
@app.post('/usuarios/', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuarios(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@app.get('/usuarios', status_code=202, response_model=List[Usuario])
def listar_usuario(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios


