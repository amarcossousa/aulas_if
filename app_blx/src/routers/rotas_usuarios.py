from fastapi import APIRouter, Depends, status
from src.schema.schemas import Usuario, UsuarioSimples
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from typing import List
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario


router = APIRouter()

# Rotas para usuarios
@router.post('/usuarios', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuarios(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@router.get('/usuarios', status_code=202, response_model=List[UsuarioSimples])
def listar_usuario(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios