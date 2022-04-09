from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/') # decoratror
def home(): 
    return {"mensagem": 'Olá FastAPI - TDS 2022'}


@app.post('/profile')
def profile():
    return {"nome": 'Marcos Sousa'}

# Paramentros de rota 
@app.get('/saudacao/{nome}')
def saudacao(nome: str):
    texto = f'Olá {nome}, tudo em paz?!'
    return {'mensagem': texto}

@app.get('/quadrado/{numero}')
def quadrado(numero:int):
    resultado = numero * numero
    texto = f'O quadrado de {numero} é {resultado}'
    return {"mesagem": texto}

# Paramentros de query strings
@app.get('/dobro')
def dobro(valor: int):
    resultado = 2 * valor
    return{"resultado:"f'O dobro de {valor} é {resultado}'}

@app.get('/area-retangulo') # ?nome=valor
def area_retangulo(largura: int, altura: int = 2):
    area = largura * altura
    return {'area': area}


class Produto(BaseModel):
    nome: str
    valor: float

@app.post('/produtos')
def produtos(produto: Produto):
    return {'mensagem': f'Produto ({produto.nome} - R$ {produto.valor}) cadastrado com sucesso!'}
