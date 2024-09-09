escolhas_piloto = {}
corredores = ['Nick', 'Pascal', 'Oliver']


def votar_piloto(escolha_piloto: dict, nome: dict, corredores: list) -> dict:
    """Função serve para você escolher
       dois pilotos e você mesmo escolher a posição"""
    piloto = int(input('''
        1-Nick
        2-Pascal
        3-Oliver
        Escolha o número do piloto: '''))
    posicao = int(input('''
        1-Primeiro
        2-Segundo
        3-Terceiro
        Escolha a posição: '''))
    for piloto, posicao in escolha_piloto.items():
        escolha_piloto[nome] = {piloto: posicao}


def guardar_voto():
    """Função serve para armazenar votos"""
