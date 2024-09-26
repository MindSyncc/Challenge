import time
from os import system

escolha_piloto = {}
corredores = ['Nick', 'Pascal', 'Oliver']
votacao = False

def votar_piloto(escolha_piloto: dict, corredores: list, pontos: int):
    """Função serve para você escolher
       dois pilotos e suas posições."""
    global votacao
    votacao = True
    system('clear')
    time.sleep(1)
    print('-=' * 40)
    print('Escolha dois pilotos e tente adivinhar qual posição ele alcançará!')
    print('Mas escolha com cautela, pois a escolha errada implicará na perca de pontos ')
    while pontos > 0 and len(escolha_piloto) < 2:
        piloto = int(input('''
            1-Nick
            2-Pascal
            3-Oliver
            Escolha o piloto desejado: ''')) - 1
        posicao = int(input('''
            1-Primeiro
            2-Segundo
            3-Terceiro
            Escolha a posição: '''))
        if 0 <= piloto < len(corredores):
            escolha_piloto[corredores[piloto]] = posicao
            pontos -= 10
        else:
            print("Piloto inválido, tente novamente.")
        print('-=' * 40)

    return escolha_piloto, pontos, votacao

                   # {nick: 1, oliver: 3}  
def checar_palpite(escolha_piloto: dict, ganhadores: dict, usuario: str) -> int:
    """Função serve para checar se acertou o palpite"""
    with open('banco_de_dados.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.strip().split(',')
            if dados[0] == usuario:
                pontos = dados[-1]
    contador = 1
    for chave, valor in escolha_piloto.items():
        if chave in ganhadores and valor == ganhadores[chave]:
            pontos += 50
            print(f'{contador}° palpite: Parabens você acertou, você ganhou {50} e está com {pontos}')
        else:
            print(f'{contador}° palpite: Você errou, agora está com {pontos} pontos')
        contador += 1
    return pontos
