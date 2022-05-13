from fastapi import APIRouter, Depends, status, HTTPException
from src.schema.schemas import Usuario, UsuarioSimples
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.providers import hash_provider

router = APIRouter()

# Rotas para usuarios
@router.post('/signup', 
            status_code=status.HTTP_201_CREATED, 
            response_model=UsuarioSimples)
def signup(usuario: Usuario, session: Session = Depends(get_db)):
    # Vericar se já existe um usuário para o telefone
    usuario_localizado = RepositorioUsuario(
        session).obter_por_telefone(usuario.telefone)
    if usuario_localizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail="Já exite um usuário com esse telefone")
    # Cria um novo usuário
    usuario.senha = hash_provider.gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@router.delete('/usuario/{id}')
def remover_user(id: int, session: Session = Depends(get_db)):
    RepositorioUsuario(session).remover(id)
    return {'msg': 'Usuário removido com sucesso'}