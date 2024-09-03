def votar_piloto():
    """Função serve para você escolher
       dois pilotos e você mesmo escolher a posição"""
    escolha_piloto = {
        'Nick': {'Primeiro': 0, 'Segundo': 0, 'Terceiro': 0},
        'Pascal': {'Primeiro': 0, 'Segundo': 0, 'Terceiro': 0},
        'Oliver': {'Primeiro': 0, 'Segundo': 0, 'Terceiro': 0}
    }    
    pilotos = ['Nick', 'Pascal', 'Oliver']
    posicoes = ['Primeiro', 'Segundo', 'Terceiro']

    print('Escolha dois pilotos e as suas posições')    
    for _ in range(2):
        piloto = int(input('''
            1-Nick
            2-Pascal
            3-Oliver
            Escolha o número do piloto: ''')) - 1
        posicao = int(input('''
            1-Primeiro
            2-Segundo
            3-Terceiro
            Escolha a posição: ''')) - 1

        # Incrementa a posição escolhida para o piloto
        escolha_piloto[pilotos[piloto]][posicoes[posicao]] += 1
    return escolha_piloto
