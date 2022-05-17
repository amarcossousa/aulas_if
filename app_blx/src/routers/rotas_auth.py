from fastapi import APIRouter, Depends, status, HTTPException
from src.schema.schemas import Usuario, UsuarioSimples, LoginData, LoginSucesso
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.providers import hash_provider, token_provider

router = APIRouter()


# Rotas para usuarios
@router.post('/signup', 
            status_code=status.HTTP_201_CREATED, 
            response_model=UsuarioSimples)
def signup(usuario: Usuario, session: Session = Depends(get_db)):
    # Vericar se já existe um usuário para o telefone
    usuario_localizado = RepositorioUsuario(session).obter_por_telefone(usuario.telefone)
    if usuario_localizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail="Já exite um usuário com esse telefone")
    # Cria um novo usuário
    usuario.senha = hash_provider.gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado


@router.post('/token', response_model=LoginSucesso)
async def login(login_data: LoginData, session: Session = Depends(get_db)):
    senha = login_data.senha
    telefone = login_data.telefone

    usuario = RepositorioUsuario(session).obter_por_telefone(telefone)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Telefone ou senha estão incorretos!')
    
    senha_valida = hash_provider.verificar_hash(senha, usuario.senha)
    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Telefone ou senha estão incorretos')
    # Gerar token JWT

    token = token_provider.criar_access_token({'sub': usuario.telefone})
    return LoginSucesso(usuario=usuario, access_token=token)



@router.delete('/usuario/{id}')
def remover_user(id: int, session: Session = Depends(get_db)):
    RepositorioUsuario(session).remover(id)
    return {'msg': 'Usuário removido com sucesso'}