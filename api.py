from fastapi import FastAPI
import json

app = FastAPI()

with open('banco_de_dados.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

@app.get('/api/usuarios')
def usuarios():
    return dados