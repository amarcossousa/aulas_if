from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship

# Classe para criar Usuarios 
class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column (String)
    senha = Column (String)
    telefone = Column (String)

    produto = relationship('Produto', back_populates='usuario')

# Classes para criar as tabelas no bd
class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    detalhes = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
    tamanhos = Column(String)
    usuario_id = Column(Integer, ForeignKey('usuario.id', name='FK_usuario'))

    usuario = relationship('Usuario', back_populates='produto')