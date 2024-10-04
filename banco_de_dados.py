import json


def preencher_contas(dicionario: dict) -> dict:
    """Função irá preencher um dicionário
    com todas as contas existentes no início
    do programa"""
    with open('banco_de_dados.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    for usuario, info in dados.items():
        dicionario[usuario] = info
    return dicionario


def adicionar_usuario(dicionario: dict, nome: str):
    """Função para adicionar um usuário ao arquivo
    JSON com os dados separados por campos"""
    with open('banco_de_dados.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    # Adiciona o novo usuário ao dicionário de dados
    dados[nome] = dicionario[nome]

    with open('banco_de_dados.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    print(f'Usuário {dicionario[nome]["nome_de_usuario"]} adicionado ao banco de dados!')


def atualizar_pontos_usuario(dicionario: dict, nome: str):
    """Função para atualizar os pontos do usuário no arquivo JSON"""
    with open('banco_de_dados.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    # Atualiza os pontos do usuário
    dados[nome] = dicionario[nome]

    with open('banco_de_dados.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    print(f'Pontos do usuário {dicionario[nome]["nome_de_usuario"]} atualizados no banco de dados!')


def buscar_usuario(nome: str):
    """Função para buscar um usuário pelo nome e exibir o nome e os pontos"""
    try:
        with open('banco_de_dados.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

            if nome in dados:
                print(f'Olá, Senhor {dados[nome]["nome_de_usuario"]}, bem-vindo!')
                print(f'Você possui {dados[nome]["pontos"]} pontos.')
            else:
                print(f'Usuário {nome} não encontrado.')

    except FileNotFoundError:
        print('Arquivo não encontrado.')
