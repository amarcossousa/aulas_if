from pydantic import BaseModel
from typing import Optional


# Classes para definir as conexões entre a API e db
class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
   

class Produto(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

    class Config:
        orm_mode = True

class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Descreva o produto aqui'

