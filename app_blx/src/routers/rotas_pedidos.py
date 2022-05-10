from fastapi import APIRouter, Depends, status, HTTPException
from src.schema.schemas import Pedido
from src.infra.sqlalchemy.config.database import get_db
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.repositorio_pedidos import RepositorioPedidos


router = APIRouter()

@router.post('/pedidos', status_code=status.HTTP_201_CREATED)
def fazer_pedido(pedido: Pedido, session: Session = Depends(get_db)):
    pedido_realizado = RepositorioPedidos(session).gravar_pedido(pedido)
    return pedido_realizado

@router.get('/pedidos/{id}', status_code=status.HTTP_202_ACCEPTED)
def listar_pedidos(id: int, session: Session = Depends(get_db)):
    try:
        pedido = RepositorioPedidos(session).buscar_por_id(id)
        return pedido
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um produto com id={id}')

@router.get('/pedidos/{id}/vendas')
def obter_pedido(pedido: int, session: Session = Depends(get_db)):
    pass
