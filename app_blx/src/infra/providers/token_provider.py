from datetime import datetime, timedelta
from jose import jwt


# CONFIG
SECRETE_KEY = '9250E222C4C71F0C58D4C54B50A880A312E9F9FED55D5C3AA0B0E860DED99165:'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 3000


def criar_access_token(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    dados.update({'exp': expiracao})

    token_jwt = jwt.encode(dados, SECRETE_KEY, algorithm=ALGORITHM)
    return token_jwt

def verificar_access_token(token: str):
    carga = jwt.decode(token, SECRETE_KEY, algorithms=[ALGORITHM])
    return carga.get('sub')