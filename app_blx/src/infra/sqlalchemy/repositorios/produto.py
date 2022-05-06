from sqlalchemy.orm import Session
from src.schema import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import delete 


class RepositorioProduto():

    def __init__(self, db: Session): # Define a seção no db
        self.db = db

    def criar(self, produto: schemas.Produto): # "Efetiva os modelos no bdb"
        db_produto = models.Produto(nome=produto.nome, 
                                    detalhes=produto.detalhes,
                                    preco=produto.preco,
                                    disponivel=produto.disponivel,
                                    usuario_id=produto.usuario_id)
                                    
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto


    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return produtos

    def obter(self):
        pass

    def remover(self, produto_id: int):
            stmt = delete(models.Produto).where(models.Produto.id == produto_id)
            self.db.execute(stmt)
            self.db.commit()
    
    def update():
        pass


