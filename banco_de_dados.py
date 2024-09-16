# Função para adicionar um usuário ao arquivo
def adicionar_usuario(dicionario: dict, nome_de_usuario: str):
    """Função para adicionar um usuário ao arquivo"""
    with open('banco_de_dados.txt', 'a', encoding='utf-8') as arquivo:
        # Grava cada informação em uma nova linha
        arquivo.write(f'{nome_de_usuario}\n{dicionario["email"]}\n{dicionario["senha"]}\n{dicionario["pontos"]}\n')
    print(f'Usuário {nome_de_usuario} adicionado ao banco de dados!')


# Função para buscar um usuário pelo nome e exibir apenas o nome e os pontos
def buscar_usuario(nome_de_usuario: str):
    """Função para buscar um usuário pelo nome e exibir apenas o nome e os pontos"""
    try:
        with open('banco_de_dados.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()  # Lê todas as linhas do arquivo
            for i in range(0, len(linhas)):  # Itera em blocos de 4 linhas
                nome = linhas[i].strip()
                pontos = linhas[i + 3].strip()
                if nome == nome_de_usuario:
                    print(f'Olá, Senhor {nome}, bem-vindo!')
                    print(f'Você possui {pontos} pontos.')
                    return
            print(f'Usuário {nome_de_usuario} não encontrado.')
    except FileNotFoundError:
        print('Arquivo não encontrado.')


# Exemplo de uso
dicionario_juan = {'email': 'email@gmail.com', 'senha': 'blabla', 'pontos': 75}


buscar_usuario('Pedro')

