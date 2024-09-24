# Função para adicionar um usuário ao arquivo
def preencher_contas(dicionario: dict, nome: str) -> dict:
    """Função irá preencher um dicionario
    com todas as contas existentes no início
    do programa"""
    lista = ['nome_de_usuario', 'email', 'senha', 'pontos']
    with open('banco_de_dados.txt', 'w', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.strip().split(',')
            for i in range(5):
                dicionario[dados[0]] = dados[]
                
def adicionar_usuario(dicionario: dict, nome: str):
    """Função para adicionar um usuário ao arquivo
    em uma única linha separada por vírgulas"""
    with open('banco_de_dados.txt', 'a', encoding='utf-8') as arquivo:
        # Grava todas as informações na mesma linha, separadas por vírgulas
        arquivo.write(f'{dicionario[nome]},{dicionario[nome]["nome_de_usuario"]},
                      {dicionario[nome]["email"]},{dicionario[nome]["senhas"]},{dicionario[nome]["pontos"]}\n')
    print(f'Usuário {dicionario[nome]["nome_de_usuario"]} adicionado ao banco de dados!')


# Função para buscar um usuário pelo nome e exibir apenas o nome e os pontos
def buscar_usuario(nome_de_usuario: str):
    """Função para buscar um usuário pelo nome e exibir o nome e os pontos"""
    try:
        with open('banco_de_dados.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()  # Lê todas as linhas do arquivo
            for linha in linhas:
                # Separa os dados da linha por vírgula
                dados = linha.strip().split(',')
                if dados[0] == nome_de_usuario:
                    print(f'Olá, Senhor {dados[1]}, bem-vindo!')
                    print(f'Você possui {dados[4]} pontos.')
                    return
            print(f'Usuário {nome_de_usuario} não encontrado.')
    except FileNotFoundError:
        print('Arquivo não encontrado.')
