from flask import session
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.models import models
from src.schema.schemas import Usuario

class RepositorioUsuario():
    
    def __init__(self, session: Session):
        self.db = session
      
    def criar(self, usuario: Usuario):
        db_usuario = models.Usuario(nome=usuario.nome,
                                    senha=usuario.senha,
                                    telefone=usuario.telefone)
        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh()
        return db_usuario


    def listar(self):
        pass

    def obter(self):
        pass

    def remover(self):
        self