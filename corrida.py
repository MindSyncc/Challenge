import random
import math
# import time
'''
Todos os valores usados abaixo ainda
não são baseados em dados coletados de corrida,
apenas do site da Formula E.
Em versões futuras os códigos serão
melhorados e baseados em dados muito mais consistentes.
Versão 1.0.6
'''
corrida_estruturada = False


def estruturar_corrida() -> tuple:
    """Essa função serve para estruturar a
       corrida que será simulada pelo usuário"""
    global corrida_estruturada
    if corrida_estruturada is False:  
        corrida_estruturada = True
    num_curvas = random.randint(10, 20)
    tamanho_corrida = random.randint(2500, 2950)
    reta = 3 * math.ceil((tamanho_corrida / num_curvas) / 4)
    curva = 1 * math.ceil((tamanho_corrida / num_curvas) / 4)
    return num_curvas, tamanho_corrida, reta, curva


def curva_reta(tamanho_corrida, reta, curva) -> list:
    '''Essa função serve para indentificar qunando o carro
       está numa curva ou numa reta'''
    soma_corrida = [0]
    while sum(soma_corrida) <= tamanho_corrida:
        soma_corrida.append(reta)
        soma_corrida.append(curva)
    return soma_corrida


def voltas_corredores(soma_corrida: list) -> dict:
    """Função serve para calcular a posicao
       dos pilotos a cada segundo"""
    posicao = {'nick': 0,
               'pascal': 0,
               'oliver': 0}
    voltas = {'nick': 0,
              'pascal': 0,
              'oliver': 0}
    for i in range(200):
        for chave in posicao.keys():
            if i % 2 == 0:
                posicao[chave] += math.ceil(random.randint(195, 230) / 3.6)
            else:
                posicao[chave] += math.ceil(random.randint(70, 130) / 3.6)
            print(f'Posicao de {chave} é {posicao[chave]}')
            if posicao[chave] > sum(soma_corrida):
                voltas[chave] += 1
                posicao[chave] -= sum(soma_corrida)
                print(f'O piloto {chave} completou uma volta')
        print('='*37)
    for chave in posicao.keys():
        posicao[chave] /= sum(soma_corrida)
        voltas[chave] += round(posicao[chave], 3)
    return voltas
