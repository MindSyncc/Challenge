import corrida
import pontos
import votacao
import time
import login
import banco_de_dados
from os import system


dicionario_contas = {}
banco_de_dados.preencher_contas(dicionario_contas)


def menu() -> None:
    """Função do menu"""
    mensagem = '''Opções do Cartola Formula
    1-Exibir informações da pista?
    2-Simular uma corrida
    3-Estatisticas do piloto
    4-Votação do piloto (A votação só pode ser feita antes de simular a corrida)
    5-Fazer Login
    6-Cadastro
    7-Deslogar
    8-Sair do programa
    '''
    global dicionario_contas
    tupla_corrida = None
    nome_cadastrado = None
    corredor_pontos = dict()
    while True:
        system('clear')
        print(mensagem)
        opcoes = int(input('Escolha sua opção: '))
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
                    time.sleep(5)
                else:
                    print('A corrida ainda não foi simulada.')
                    print('Clique na opção "Simular uma corrida" para visualizar as informações da pista.')
                    print('ATENÇÃO: Caso a corrida seja simulada antes de sua votação. Você perderá a oportunidade de votar.')
                    time.sleep(15)
            case 2:
                tupla_corrida = corrida.estruturar_corrida()
                percurso_corrida = corrida.curva_reta(tupla_corrida[1],
                                                     tupla_corrida[2],
                                                     tupla_corrida[0])
                num_voltas = corrida.voltas_corredores(percurso_corrida)
                print('RESULTADO FINAL DA CORRIDA')
                corredor_pontos = pontos.definir_ganhador(num_voltas)
                if votacao.votacao is True:
                    votacao.checar_palpite(votacao.escolha_piloto,
                                          pontos.posicao_corredor,
                                          nome_cadastrado)
                else:
                    print('\nVocê não participou do processo de votação.')
                    print('Portanto, não poderá votar depois.')
                time.sleep(10)
            case 4:
                if corrida.corrida_estruturada is True:
                    print('Tá tentando votar depois que a corrida aconteceu?')
                else:
                    if login.login_status is True:
                        pontos_usuario = int(dicionario_contas[nome_cadastrado]['pontos'])  # Pegando os pontos do usuário
                        escolha_piloto, pontos_usuario, votacao.votacao = votacao.votar_piloto(votacao.escolha_piloto, votacao.corredores, pontos_usuario)
                        dicionario_contas[nome_cadastrado]['pontos'] = str(pontos_usuario)  # Atualizando os pontos no dicionário
                        banco_de_dados.atualizar_pontos_usuario(dicionario_contas, nome_cadastrado)  # Salvando no arquivo
                    else:
                        print('Você deve estar logado para votar')
                time.sleep(2.5)
            case 5:
                if login.login_status is False:
                    _, nome_cadastrado = login.login_usuario(dicionario_contas)
                else:
                    print('Você já está logado')
                time.sleep(2.5)
            case 6:
                if login.login_status is False:
                    dicionario_contas, nome_cadastrado, _ = login.cadastrar_usuario(dicionario_contas)
                    banco_de_dados.adicionar_usuario(dicionario_contas, nome_cadastrado)
                else:
                    print('Não é possível se cadastrar, você já está logado')
                time.sleep(2)
            case 7:
                if not login.login_status:
                    print('Para que você possa deslogar, é preciso primeiro estar logado')
                else:
                    login.login_status = False
                    print('Deslogado com sucesso!')
                time.sleep(4)
            case 8:
                print('Saindo do programa...')
                time.sleep(2)
                break
            case _:
                print('Digite algum número dentro das opções')
                time.sleep(2)


menu()
