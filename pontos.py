import random
from corrida import voltas_lista, posicao
pontos = [25, 18, 15]
corredor = {"nick": voltas_lista[0], "pascal": voltas_lista[1], "oliver": voltas_lista[2]}
print(voltas_lista)
voltas_lista.sort(reverse = True)
for i in range(len(voltas_lista)):
    voltas_lista[i] = pontos[i]
print(voltas_lista)
