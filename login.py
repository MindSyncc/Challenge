import re
from os import system


def cadastrar_usuario(dicionario: dict) -> tuple:
    """Esta função cadastra um usuário e retorna uma tupla com um dicionário de contas criadas e o status de login"""
    login_status = False
    nome = input('Digite aqui seu nome completo: ').strip().title()
    dicionario[nome] = {}
    dicionario[nome]['nome_de_usuario'] = input('Digite aqui seu nome de usuário: ')
    dicionario[nome]['email'] = input('Digite seu email: ')
    dicionario[nome]['senha'] = input('Digite sua senha: ')
    dicionario[nome]['pontos'] = 100

    # Exemplo de como deverá ser a variável dicionario_contas:
    """
    dicionario = {'Rodrigo Silveira Ferreira': {"nome_de_usuario": 'RodrigoSFerreira', "email": 'rodrigosilveiraf@email.com', "senha": @ABCdef123},
                  'Daniela Fukushima Hashimoto': {"nome_de_usuario": 'DaniFukushimaH', "email": 'danielafukH@outlook.com', "senha": !GHIjkl456}}
    """

    while True:
        if not re.search(r'[!@#$%^&*(),.?":{}|<>_-]', dicionario[nome]['senha']):
            system('clear')
            system('cls')
            print('A senha deve conter pelo menos um caracter especial')
            dicionario[nome]['senha'] = input('Digite sua senha: ')
        elif not re.search(r'[A-Z]', dicionario[nome]['senha']):
            system('clear')
            system('cls')
            print('A senha deve conter pelo menos uma letra maiúscula')
            dicionario[nome]['senha'] = input('Digite sua senha: ')
        elif not any(caracter.isdigit() for caracter in dicionario[nome]['senha']):
            system('clear')
            system('cls')
            print('A senha deve conter pelo menos um algarismo')
            dicionario[nome]['senha'] = input('Digite sua senha: ')
        elif len(dicionario[nome]['senha']) < 8:
            system('clear')
            system('cls')
            print('A senha deve ter pelo menos 8 caracteres')
            dicionario[nome]['senha'] = input('Digite sua senha: ')
        else:
            login_status = True
            break
    print('Cadastro realizado com sucesso!')
    print(f'Seja bem-vindo(a) {nome}!')

    return dicionario, login_status


def login_usuario(dicionario: dict) -> bool:
    """Esta função faz o login do usuário e
    retorna o estado de login ativado"""
    login_status = False
    nome = input('Digite seu nome completo: ').strip().title()
    nome_usuario_de_entrada = input('Digite o nome de usuário: ')
    senha_de_entrada = input('Digite sua senha: ')

    while True:
        if nome in dicionario:
            if nome_usuario_de_entrada == dicionario[nome]['nome_de_usuario'] or senha_de_entrada == dicionario[nome]['senha']:
                system('clear')
                system('cls')
                print('Login realizado com sucesso!')
                print(f'Seja bem-vindo(a) de volta {nome}!')
                break
            else:
                system('clear')
                system('cls')
                print('Nome de usuário ou senha foram digitados incorretamente!')
                nome_usuario_de_entrada = input('Digite o nome de usuário novamente: ')
                senha_de_entrada = input('Digite sua senha novamente: ')
        else:
            system('clear')
            system('cls')
            print('O nome informado é inválido!')
            nome = input('Digite seu nome novamente: ')
    return not login_status
