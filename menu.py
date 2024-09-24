'''Versão 1.0.6'''
import corrida
import pontos
import votacao
import time
import login

#dicionario_contas = {}


def menu() -> None:
    "Função do menu"
    mensagem = '''Opções do Cartola Formula
    1-Exibir informações da pista?
    2-Simular uma corrida
    3-Estatisticas do piloto
    4-Votacao do piloto
    5-Fazer Login
    6-Cadastro
    6-Sair
    '''
    global dicionario_contas
    tupla_corrida = None
    corredor_pontos = dict()
    while True:
        print(mensagem)
        opcoes = int(input('Escolha sua opção '))
        match opcoes:
            case 1:
                if corrida.corrida_estruturada is True:
                    print('=' * 37)
                    for estrutura in range(len(tupla_corrida)):
                        match estrutura:
                            case 0:
                                print(f'O número de curvas será {tupla_corrida[estrutura]}')
                            case 1:
                                print(f'Uma volta tem {tupla_corrida[estrutura]} metros')
                            case 2:
                                print(f'O tamanho de cada reta é {tupla_corrida[estrutura]} metros')
                            case 3:
                                print(f'Cada curva tem {tupla_corrida[estrutura]} metros ')
                    print('=' * 37)
                    time.sleep(2)
                else:
                    print('A corrida ainda não foi inicializada')
            case 2:
                tupla_corrida = corrida.estruturar_corrida()
                percurso_corrida = corrida.curva_reta(tupla_corrida[1],
                                                     tupla_corrida[2],
                                                     tupla_corrida[0])
                num_voltas = corrida.voltas_corredores(percurso_corrida)
                print(num_voltas)
                corredor_pontos = pontos.definir_ganhador(num_voltas)
                if votacao.votacao is True:
                    votacao.checar_palpite(votacao.escolha_piloto,
                                          pontos.posicao_corredor,
                                          100)
                else:
                    print('Você não realizou uma função')
            case 4:
                if corrida.corrida_estruturada is True:
                    print('Tá tentando votar depois que a corrida aconteceu?')
                else:
                    #Teste
                    votacao.votar_piloto(votacao.escolha_piloto,
                                         votacao.corredores, 100)
            case 5:
                login.login_usuario(dicionario_contas)
            case 6:
                login.cadastrar_usuario(dicionario_contas)
            case 7:
                print('Saindo do programa...')
                break
            case _:
                print('Digite algum número dentro das opções')


menu()
