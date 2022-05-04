from pydantic import BaseModel
from typing import Optional


# Classes para definir as conexões entre a API e db
class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    senha: str
    telefone: str
    
    # usuario: Optional[]

    class Config:
        orm_mode = True


class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str

    class Config:
        orm_mode = True

class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: int
    
    usuario: Optional[UsuarioSimples]

    class Config:
        orm_mode = True

class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: float
   
    class Config:
        orm_mode = True

class Pedido(BaseModel):
    id: Optional[int] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Descreva o produto aqui'

