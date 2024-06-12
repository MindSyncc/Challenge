# Importar as listas de voltas e posições
import corrida
from corrida import voltas_lista, posicao

# Lista de pontos disponíveis para as posições
pontos = [25, 18, 15]

# Dicionário com os corredores e suas voltas
corredor = {"Nick": voltas_lista[0], "Pascal": voltas_lista[1], "Oliver": voltas_lista[2]}

# Ordenar o dicionário de corredores de forma decrescente pelos valores (voltas)
corredor = {k: v for k, v in sorted(corredor.items(), key=lambda item: item[1], reverse=True)}
print('='*37)
print('Distância percorrida por cada piloto: ')
for key, value in corredor.items():           
    print(f'{key} percorreu {value} kms')
print('='*37)
# Novo dicionário para armazenar as pontuações de cada corredor
corredor_pontos = {}

# Índice para a lista de pontos
i = 0

# Percorrer os itens do dicionário 'corredor' e inserir no novo dicionário os pontos
for key, value in corredor.items():
    if i < len(pontos):  # Verifica se ainda há pontos disponíveis na lista
        corredor_pontos[key] = pontos[i]
        print(f'{i+1}°lugar - {key}: {pontos[i]} pontos')
    i += 1  # Incrementa o índice para a próxima posição de pontos
