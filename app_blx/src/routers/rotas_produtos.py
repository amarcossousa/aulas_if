from fastapi import APIRouter, Depends, status, HTTPException
from src.schema.schemas import Produto, ProdutoSimples
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from typing import List
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto



router = APIRouter()


# Rotas para produtos
@router.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=ProdutoSimples)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@router.get('/produtos', status_code=status.HTTP_202_ACCEPTED, response_model=List[ProdutoSimples])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@router.delete('/produto/{produto_id}')
def remover(produto_id: int, db:Session = Depends(get_db)):
    RepositorioProduto(db).remover(produto_id)
    return {'msg': 'Produto excluido com sucesso! '}

@router.put('/produtos/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=ProdutoSimples)
def editar_produto(id: int, produto: Produto, session: Session = Depends(get_db)):
    RepositorioProduto(session).editar(id, produto)
    # produto.id = id # Parte do codigo não faz efeito algum
    return produto

@router.get('/produto/{id}')
def obter_produto(id: int, db: Session = Depends(get_db)):
    produto = RepositorioProduto(db).obter(id)
    if not produto:
        raise HTTPException(status_code=404, detail=(f"Não existe um produto com id = {id}"))
    return produto