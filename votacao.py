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
    print('Mas escolha com cautela, pois a escolha errada implicará na perda de pontos ')
    while pontos > 0 and len(escolha_piloto) < 2:
        try:
            piloto = int(input('''
                1-Nick
                2-Pascal
                3-Oliver
                Escolha o piloto desejado: ''')) - 1
            
            if 0 <= piloto < len(corredores):
                posicao = int(input('''
                    1-Primeiro
                    2-Segundo
                    3-Terceiro
                    Escolha a posição: '''))

                if 1 <= posicao <= 3:
                    escolha_piloto[corredores[piloto]] = posicao
                    pontos -= 10
                else:
                    print("Posição inválida. Escolha entre 1 (Primeiro), 2 (Segundo) ou 3 (Terceiro).")
            else:
                print("Piloto inválido. Escolha um número de 1 a 3.")

        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
        print('-=' * 40)

    return escolha_piloto, pontos, votacao


def checar_palpite(escolha_piloto: dict, ganhadores: dict, usuario: str) -> int:
    """Função serve para checar se acertou o palpite e atualizar os pontos no banco de dados"""
    linhas = []
    pontos = 0

    try:
        # Lendo o arquivo e encontrando o usuário
        with open('banco_de_dados.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        # Buscando o usuário e atualizando os pontos
        for i, linha in enumerate(linhas):
            dados = linha.strip().split(',')
            if dados[0] == usuario:
                try:
                    pontos = int(dados[-1])  # Pega a pontuação atual do usuário
                except ValueError:
                    print("Erro ao ler os pontos do usuário. Definindo pontos como 0.")
                    pontos = 0

                contador = 1
                # Checando os palpites
                for chave, valor in escolha_piloto.items():
                    if chave in ganhadores and valor == ganhadores[chave]:
                        pontos += 50
                        print(f'{contador}° palpite: Parabéns! Você acertou. Ganhou 50 pontos e está com {pontos}.')
                    else:
                        print(f'{contador}° palpite: Você errou. Agora está com {pontos} pontos.')
                    contador += 1

                # Atualizando a pontuação do usuário no arquivo
                dados[-1] = str(pontos)
                linhas[i] = ','.join(dados) + '\n'
                break

        # Escrevendo os dados atualizados de volta no arquivo
        with open('banco_de_dados.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.writelines(linhas)

    except FileNotFoundError:
        print("Erro: O arquivo 'banco_de_dados.txt' não foi encontrado.")
    return pontos
