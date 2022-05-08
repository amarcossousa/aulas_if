from fastapi import APIRouter, Depends, status
from src.schema.schemas import Pedido
from src.infra.sqlalchemy.config.database import get_db
from sqlalchemy.orm import Session


router = APIRouter()

@router('/pedidos', status_code=status.HTTP_201_CREATED, response_model=Pedido)
def fazer_pedido(pedido: Pedido, session: Session = Depends(get_db)):
    pass

@router('/pedidos', status_code=status.HTTP_202_ACCEPTED)
def listar_pedidos(session: Session = Depends(get_db)):
    pass

@router('/pedidos/{id}')
def obter_pedido(pedido: int, session: Session = Depends(get_db)):
    pass
