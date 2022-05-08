from sqlalchemy.orm import Session
from src.schema import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import delete, update, select


class RepositorioProduto():

    def __init__(self, session: Session): # Define a seção no db
        self.session = session

    def criar(self, produto: schemas.Produto): # "Efetiva os modelos no db"
        db_produto = models.Produto(nome=produto.nome, 
                                    detalhes=produto.detalhes,
                                    preco=produto.preco,
                                    disponivel=produto.disponivel,
                                    usuario_id=produto.usuario_id)
                                    
        self.session.add(db_produto)
        self.session.commit()
        self.session.refresh(db_produto)
        return db_produto
    
    def editar(self, id: int, produto: schemas.Produto):
        update_stmt = update(models.Produto).where(
            models.Produto.id == id).values(nome=produto.nome, 
                                                    detalhes=produto.detalhes,
                                                    preco=produto.preco,
                                                    disponivel=produto.disponivel
                                                    )
        self.session.execute(update_stmt)
        self.session.commit()

    def remover(self, produto_id: int):
            stmt = delete(models.Produto).where(models.Produto.id == produto_id)
            self.session.execute(stmt)
            self.session.commit()
    
    def listar(self):
        produtos = self.session.query(models.Produto).all()
        return produtos

    def obter(self, produto_id: int):
        stmt = select(models.Produto).filter_by(id = produto_id)
        produto = self.session.execute(stmt).scalars().one()
        return produto


