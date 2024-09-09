import re


def cadastrar_usuario(dicionario: dict) -> tuple:
    """Esta função cadastra um usuário e retorna uma tupla com um dicionário de contas criadas e o status de login"""
    login_status = False
    nome_de_usuario = input('Digite aqui o nome de usuário: ')
    dicionario[nome_de_usuario] = {}
    dicionario[nome_de_usuario]['nome'] = input('Digite aqui seu nome: ')
    dicionario[nome_de_usuario]['email'] = input('Digite seu email: ')
    dicionario[nome_de_usuario]['senha'] = input('Digite sua senha: ')

    # Exemplo de como deverá ser a variável dicionario_contas:
    """
    dicionario = {RodrigoSFerreira: {"nome": 'Rodrigo Silveira Ferreira', "email": 'rodrigosilveiraf@email.com', "senha": @ABCdef123},
                  DaniFukushimaH: {"nome": 'Daniela Fukushima Hashimoto', "email": 'amandafukH@outlook.com', "senha": !GHIjkl456}}
    """

    while True:
        if not re.search(r'[!@#$%^&*(),.?":{}|<>_-]', dicionario[nome_de_usuario]['senha']):
            print('A senha deve conter pelo menos um caracter especial')
            dicionario[nome_de_usuario]['senha'] = input('Digite sua senha: ')
        elif not re.search(r'[A-Z]', dicionario[nome_de_usuario]['senha']):
            print('A senha deve conter pelo menos uma letra maiúscula')
            dicionario[nome_de_usuario]['senha'] = input('Digite sua senha: ')
        elif not any(caracter.isdigit() for caracter in dicionario[nome_de_usuario]['senha']):
            print('A senha deve conter pelo menos um algarismo')
            dicionario[nome_de_usuario]['senha'] = input('Digite sua senha: ')
        elif len(dicionario[nome_de_usuario]['senha']) < 8:
            print('A senha deve ter pelo menos 8 caracteres')
            dicionario[nome_de_usuario]['senha'] = input('Digite sua senha: ')
        else:
            login_status = True
            break

    return dicionario, login_status

# O código abaixo é apenas um teste da função cadastrar_usuario

# A priori, o dicionário de contas estará vazio e será colocado acima do loop while True na função menu
dicionario_contas = {}

# Tupla de controle de dados de retorno da função cadastrar_usuario, haja vista que a função retorna dois dados
tupla_retorno = cadastrar_usuario(dicionario_contas)

# Variávies para armazenar as contas e o status de login
dicionario_contas = tupla_retorno[0]
login_status = tupla_retorno[-1]
