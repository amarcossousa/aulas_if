from pydantic import BaseModel, Field
from typing import Optional, List


# Classes para definir as conexões entre a API e db
class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: float
    usuario_id: Optional[int]
    disponivel: bool
   
    class Config:
        orm_mode = True


class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    senha: str
    telefone: str
    produtos: List[ProdutoSimples] = []
    
    class Config:
        orm_mode = True


class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    
    class Config:
        orm_mode = True

# Comentario Qualquer
class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: Optional[int]
    usuario: Optional[UsuarioSimples]
    

    class Config:
        orm_mode = True


class Pedido(BaseModel):
    id: Optional[int] = None
    quantidade: int
    local_entrega: Optional[str]
    tipo_entrega: str
    observacao: Optional[str] = 'Descreva o produto aqui'

    usuario_id: Optional[UsuarioSimples]
    produto_id: Optional[ProdutoSimples]

    class Config:
        orm_mode = True

