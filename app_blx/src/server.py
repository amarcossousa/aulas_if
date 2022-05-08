from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import criar_db, get_db
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.routers import rotas_produtos, rotas_usuarios


criar_db()

app = FastAPI()

origins = [
    "htpp://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
app.include_router(rotas_produtos.router)

app.include_router(rotas_usuarios.router)




