from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schema import schemas
from src.infra.sqlalchemy.models import models


class RepositorioPedidos():

    def __init__(self, session: Session ):
        self.session = session

    def gravar_pedido(self, pedido: schemas.Pedido):
        session_pedido = models.Pedido(quantidade=pedido.quantidade,
                                        local_entrega=pedido.local_entrega,
                                        tipo_entrega=pedido.tipo_entrega,
                                        observacao=pedido.observacao)

        self.session.add(session_pedido)
        self.session.commit()
        self.session.refresh(session_pedido)
        return session_pedido

    def buscar_por_id(self, id: int):
        stmt = select(models.Pedido).where(models.Pedido.id == id)
        pedido = self.session.execute(stmt).first()
        return pedido
        
    
    def listar_vendas_por_id(self):
        ...
    
    def listar_compras_por_id():
        ...

    

        