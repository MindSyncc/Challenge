import random
from corrida import voltas_lista, posicao

pontos = [25, 18, 15]
corredor = {"nick": voltas_lista[0], "pascal": voltas_lista[1], "oliver": voltas_lista[2]}
print(f'Antes da ordenação: {corredor}')

# ordena o dicionário de forma decrescente pelo valor
corredor = {k: v for k, v in sorted(
    corredor.items(), key=lambda item: item[1], reverse=True)}
print(f'Depois da ordenação: {corredor}')

# gera um novo dicionário para armazenar as pontuações de cada corredor
corredor_pontos = {}

# indice da lista
i = 0
# percorre os itens do dicionário 'corredor' e vai inserindo no novo dicionário os pontos

for key, value in corredor.items():
    corredor_pontos[key] = pontos[i]
    i += 1

print(f'Dicionário com pontos: {corredor_pontos}')