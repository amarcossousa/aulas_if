from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import criar_db
from src.routers import rotas_produtos, rotas_auth, rotas_pedidos


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

# Rotas produtos
app.include_router(rotas_produtos.router)
# Rotas usuarios
app.include_router(rotas_auth.router, prefix="/auth")
# Rotas pedidos
app.include_router(rotas_pedidos.router)






