from datetime import datetime, timedelta
from jose import jwt


# CONFIG
SECRETE_KEY = 'y%~9dMX[gpta6m2:'
ALGORITHM = 'HS256'
EXPERES_IN_MIN = 3000


def criar_access_token(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPERES_IN_MIN)

    dados.update({'exp': expiracao})

    token_jwt = jwt.encode(dados, SECRETE_KEY, algorithm=ALGORITHM)
    return token_jwt

def verificar_access_token(token:str):
    carga = jwt.decode(token, SECRETE_KEY, algorithms=[ALGORITHM])
    return carga.get('sub')