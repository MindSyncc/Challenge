escolha_piloto = {}
corredores = ['Nick', 'Pascal', 'Oliver']
votacao = False


def votar_piloto(escolha_piloto: dict, corredores: list, pontos: int):
    """Função serve para você escolher
       dois pilotos e suas posições."""
    global votacao
    votacao = True
    while pontos > 0 and len(escolha_piloto) < 2:
        piloto = int(input('''
            1-Nick
            2-Pascal
            3-Oliver
            Escolha o número do piloto: ''')) - 1
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

    return escolha_piloto, pontos, votacao


def checar_palpite(escolha_piloto: dict, ganhadores: dict, pontos: int) -> int:
    """Função serve para checar se acertou o palpite"""
    for chave, valor in escolha_piloto.items():
        if chave in ganhadores and valor == ganhadores[chave]:
            pontos += 50
            print(f'Parabens você acertou, você ganhou {50} e está com {pontos}')
    print(pontos)
    return pontos
