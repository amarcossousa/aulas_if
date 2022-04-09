from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"mensagem": 'Olá FastAPI - TDS 2022'}


@app.get('/profile')
def profile():
    return {"nome": 'Marcos Sousa'}