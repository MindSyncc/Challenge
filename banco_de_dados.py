def preencher_contas(dicionario: dict) -> dict:
    """Função irá preencher um dicionário
    com todas as contas existentes no início
    do programa"""
    lista = ['nome_de_usuario', 'email', 'senha', 'pontos']

    with open('banco_de_dados.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        dados = linha.strip().split(',')
        if len(dados) == 5:
            usuario = dados[0]
            dicionario[usuario] = {lista[i - 1]: dados[i] for i in range(1, 5)}
    return dicionario


def adicionar_usuario(dicionario: dict, nome: str):
    """Função para adicionar um usuário ao arquivo
    em uma única linha separada por vírgulas"""
    usuario_info = dicionario[nome]
    with open('banco_de_dados.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{nome},{usuario_info["nome_de_usuario"]},{usuario_info["email"]},{usuario_info["senha"]},{usuario_info["pontos"]}\n')
    print(f'Usuário {usuario_info["nome_de_usuario"]} adicionado ao banco de dados!')


def atualizar_pontos_usuario(dicionario: dict, nome: str):
    """Função para atualizar os pontos do usuário no arquivo de banco de dados"""
    usuario_info = dicionario[nome]
    linhas_atualizadas = []

    with open('banco_de_dados.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    
    for linha in linhas:
        dados = linha.strip().split(',')
        if dados[0] == nome:
            linha_atualizada = f'{nome},{usuario_info["nome_de_usuario"]},{usuario_info["email"]},{usuario_info["senha"]},{usuario_info["pontos"]}\n'
            linhas_atualizadas.append(linha_atualizada)
        else:
            linhas_atualizadas.append(linha)
    
    with open('banco_de_dados.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(linhas_atualizadas)

    print(f'Pontos do usuário {usuario_info["nome_de_usuario"]} atualizados no banco de dados!')


def buscar_usuario(nome: str):
    """Função para buscar um usuário pelo nome e exibir o nome e os pontos"""
    try:
        with open('banco_de_dados.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split(',')
                if dados[0] == nome:
                    print(f'Olá, Senhor {dados[1]}, bem-vindo!')
                    print(f'Você possui {dados[4]} pontos.')
                    return
            print(f'Usuário {nome} não encontrado.')
    except FileNotFoundError:
        print('Arquivo não encontrado.')
