import re
from os import system

login_status = False


def cadastrar_usuario(dicionario: dict) -> tuple:
    """Esta função cadastra um usuário e retorna uma tupla
    com um dicionário de contas criadas, o nome do usuário
    e o status de login."""
    global login_status
    nome = input('Digite aqui seu nome completo: ').strip().title()

    # Garantir que o nome seja único
    while nome in dicionario:
        print('Esse nome já está cadastrado. Por favor, use outro nome.')
        nome = input('Digite aqui seu nome completo: ').strip().title()

    dicionario[nome] = {}
    dicionario[nome]['nome_de_usuario'] = input('Digite aqui seu nome de usuário: ').strip()

    # Validação de email
    while True:
        email = input('Digite seu email: ').strip()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print('Email inválido. Por favor, tente novamente.')
        else:
            dicionario[nome]['email'] = email
            break

    # Validações de senha
    while True:
        senha = input('Digite sua senha: ')
        if len(senha) < 8:
            system('clear')
            print('A senha deve ter pelo menos 8 caracteres')
        elif not re.search(r'[!@#$%^&*(),.?":{}|<>_-]', senha):
            system('clear')
            print('A senha deve conter pelo menos um caracter especial')
        elif not re.search(r'[A-Z]', senha):
            system('clear')
            print('A senha deve conter pelo menos uma letra maiúscula')
        elif not any(caracter.isdigit() for caracter in senha):
            system('clear')
            print('A senha deve conter pelo menos um algarismo')
        else:
            dicionario[nome]['senha'] = senha
            login_status = True
            break

    dicionario[nome]['pontos'] = 100  # Pontuação inicial padrão

    print('Cadastro realizado com sucesso!')
    print(f'Seja bem-vindo(a), {nome}!')

    return dicionario, nome, login_status  # Retorna dicionário, nome e status de login


def login_usuario(dicionario: dict) -> tuple:
    """Esta função faz o login do usuário e
    retorna o estado de login ativado."""
    global login_status
    nome = input('Digite seu nome completo: ').strip().title()

    if nome not in dicionario:
        print('Nome não encontrado no sistema. Verifique o nome digitado ou cadastre-se.')
        return login_status, None

    tentativas = 0
    while tentativas < 3:
        nome_usuario_de_entrada = input('Digite o nome de usuário: ').strip()
        senha_de_entrada = input('Digite sua senha: ').strip()

        if nome_usuario_de_entrada == dicionario[nome]['nome_de_usuario'] and senha_de_entrada == dicionario[nome]['senha']:
            system('clear')
            print('Login realizado com sucesso!')
            print(f'Seja bem-vindo(a) de volta, {nome}!')
            login_status = True
            return login_status, nome
        else:
            tentativas += 1
            print(f'Nome de usuário ou senha incorretos. Tentativas restantes: {3 - tentativas}')

        if tentativas == 3:
            print('Você excedeu o número de tentativas. Tente novamente mais tarde.')

    return login_status, None
