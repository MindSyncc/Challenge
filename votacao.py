def votar_piloto(escolha_piloto: dict, corredores: list, pontos: int) -> dict:
    """Função serve para você escolher
       dois pilotos e suas posições."""
    while pontos > 0 and len(escolha_piloto) < 2:  # Permitir escolher dois pilotos
        piloto = int(input('''
            1-Nick
            2-Pascal
            3-Oliver
            Escolha o número do piloto: ''')) - 1  # Subtrai 1 para alinhar com o índice
        posicao = int(input('''
            1-Primeiro
            2-Segundo
            3-Terceiro
            Escolha a posição: '''))
        if 0 <= piloto < len(corredores):
            escolha_piloto[corredores[piloto]] = posicao  # Adiciona piloto e posição
            pontos -= 10  # Reduz os pontos a cada escolha
        else:
            print("Piloto inválido, tente novamente.")
    return escolha_piloto, pontos  # Retorna o dicionário e os pontos atualizados


def checar_palpite(escolha_piloto: dict, ganhadores: dict, pontos: int) -> int:
    """Função serve para checar se acertou o palpite"""
    for chave, valor in escolha_piloto.items():
        if chave in ganhadores and valor == ganhadores[chave]:
            pontos += 50  # Acrescenta pontos para cada acerto
    return pontos
