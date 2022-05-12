from requests import delete
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
from src.schema.schemas import Usuario
from sqlalchemy import select, delete

class RepositorioUsuario():
    
    def __init__(self, session: Session):
        self.session = session
      
    def criar(self, usuario: Usuario):
        db_usuario = models.Usuario(nome=usuario.nome,
                                    senha=usuario.senha,
                                    telefone=usuario.telefone)
        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh(db_usuario)
        return db_usuario


    def listar(self):
        stmt = select(models.Usuario)
        usuarios = self.session.execute(stmt).scalars().all()
        return usuarios

    def obter_por_telefone(self, telefone):
        query = select(models.Usuario).where(
            models.Usuario.telefone == telefone)
        return self.session.execute(query).scalars().first()
    

    def remover(self, usuario_id: int):
        stmt = delete(models.Usuario).where(models.Usuario.id == usuario_id)
        self.session.execute(stmt)
        self.session.commit()