from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()


class Animal(BaseModel):
    id: Optional[int]
    nome: str
    idade: int
    sexo: str
    cor: str


banco: List [Animal] = []

@app.get('/animais')
def listar_animais():
    return banco



@app.post('/animais')
def criar_animal(animal: Animal):
    animal.id = uuid4()
    banco.append(animal)
    return {'mensagem:' 'Confirmado'}