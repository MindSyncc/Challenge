import re
from os import system

login_status = False


def cadastrar_usuario(dicionario: dict) -> tuple:
    """Esta função cadastra um usuário e retorna uma tupla
    com um dicionário de contas criadas, o nome do usuário e o status de login."""
    global login_status
    nome = input('Digite aqui seu nome completo: ').strip().title()
    dicionario[nome] = {}
    dicionario[nome]['nome_de_usuario'] = input('Digite aqui seu nome de usuário: ')
    dicionario[nome]['email'] = input('Digite seu email: ')
    dicionario[nome]['senha'] = input('Digite sua senha: ')
    dicionario[nome]['pontos'] = 100

    # Validações de senha
    while True:
        if not re.search(r'[!@#$%^&*(),.?":{}|<>_-]', dicionario[nome]['senha']):
            system('clear')
            print('A senha deve conter pelo menos um caracter especial')
            dicionario[nome]['senha'] = input('Digite sua senha: ')
        elif not re.search(r'[A-Z]', dicionario[nome]['senha']):
            system('clear')
            print('A senha deve conter pelo menos uma letra maiúscula')
            dicionario[nome]['senha'] = input('Digite sua senha: ')
        elif not any(caracter.isdigit() for caracter in dicionario[nome]['senha']):
            system('clear')
            print('A senha deve conter pelo menos um algarismo')
            dicionario[nome]['senha'] = input('Digite sua senha: ')
        elif len(dicionario[nome]['senha']) < 8:
            system('clear')
            print('A senha deve ter pelo menos 8 caracteres')
            dicionario[nome]['senha'] = input('Digite sua senha: ')
        else:
            login_status = True
            break

    print('Cadastro realizado com sucesso!')
    print(f'Seja bem-vindo(a) {nome}!')

    return dicionario, nome, login_status  # Retorna dicionário, nome e status de login


def login_usuario(dicionario: dict) -> tuple:
    """Esta função faz o login do usuário e
    retorna o estado de login ativado"""
    global login_status
    nome = input('Digite seu nome completo: ').strip().title()
    nome_usuario_de_entrada = input('Digite o nome de usuário: ')
    senha_de_entrada = input('Digite sua senha: ')

    tentativas = 0
    while tentativas < 3:
        if nome in dicionario:
            if nome_usuario_de_entrada == dicionario[nome]['nome_de_usuario'] and senha_de_entrada == dicionario[nome]['senha']:
                system('clear')
                system('cls')
                print('Login realizado com sucesso!')
                print(f'Seja bem-vindo(a) de volta {nome}!')
                login_status = True
                return login_status, nome
            else:
                system('clear')
                system('cls')
                print('Nome de usuário ou senha foram digitados incorretamente!')
                nome_usuario_de_entrada = input('Digite o nome de usuário novamente: ')
                senha_de_entrada = input('Digite sua senha novamente: ')
                tentativas += 1
        else:
            system('clear')
            system('cls')
            print('O nome informado é inválido!')
            nome = input('Digite seu nome novamente: ')
            tentativas += 1
    print('Você excedeu o número de tentativas. Por favor, tente novamente mais tarde')
    return login_status, nome