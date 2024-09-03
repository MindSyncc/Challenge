def votar_piloto(dicionario_pilotos: dict):
    escolha_piloto = {piloto: {'Primeiro': 0, 'Segundo': 0, 'Terceiro': 0} for piloto in dicionario_pilotos}
    
    for i in range(2):
        piloto = list(dicionario_pilotos.keys())[int(input("Escolha o piloto (1-{}): ".format(len(dicionario_pilotos)))) - 1]
        posicao = ['Primeiro', 'Segundo', 'Terceiro'][int(input("Escolha a posição (1-3): ")) - 1]
        escolha_piloto[piloto][posicao] += 1

    for piloto in dicionario_pilotos:
        if escolha_piloto[piloto]['Primeiro'] == 1 and dicionario_pilotos[piloto] == 25:
            print(f"Você acertou: {piloto} em 1º lugar!")
        elif escolha_piloto[piloto]['Segundo'] == 1 and dicionario_pilotos[piloto] == 18:
            print(f"Você acertou: {piloto} em 2º lugar!")
        elif escolha_piloto[piloto]['Terceiro'] == 1 and dicionario_pilotos[piloto] == 15:
            print(f"Você acertou: {piloto} em 3º lugar!")

# Teste da função
votar_piloto({'Nick': 25, 'Pascal': 18, 'Oliver': 15})
