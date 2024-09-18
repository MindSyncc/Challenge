posicao_corredor = dict()


def definir_ganhador(corredor: dict) -> dict:
    """Essa função define quantos pontos cada piloto ganhará"""
    pontos = (25, 18, 15)

    # Ordenar o dicionário de corredores de forma decrescente pelos valores
    corredor = {k: v for k, v in sorted(corredor.items(),
                key=lambda item: item[1], reverse=True)}
    print('='*37)
    print('Distância percorrida por cada piloto: ')
    for key, value in corredor.items():
        print(f'{key} percorreu {value} kms')
    print('='*37)
    # Novo dicionário para armazenar as pontuações de cada corredor
    corredor_pontos = {}
    posicao_corredor = {}
    # Índice para a lista de pontos
    i = 0

    # Inserir no novo dicionário os pontos
    for key, value in corredor.items():
        if i < len(pontos):  # Verifica se ainda há pontos disponíveis na lista
            corredor_pontos[key] = pontos[i]
            posicao_corredor[key] = i + 1
            print(f'{i+1}°lugar - {key}: {pontos[i]} pontos')
        i += 1  # Incrementa o índice para a próxima posição de pontos
    return corredor_pontos, posicao_corredor
