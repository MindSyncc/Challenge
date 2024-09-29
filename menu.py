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
    3-Votação do piloto (A votação só pode ser feita antes de simular a corrida)
    4-Fazer Login
    5-Cadastro
    6-Deslogar
    7-Sair do programa
    '''
    global dicionario_contas
    tupla_corrida = None
    nome_cadastrado = None

    while True:
        system('clear')
        print(mensagem)
        try:
            opcoes = int(input('Escolha sua opção: '))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número correspondente às opções.")
            time.sleep(2)
            continue

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
                    time.sleep(4.5)
                else:
                    print('A corrida ainda não foi simulada.')
                    print('Clique na opção "Simular uma corrida" para visualizar as informações da pista.')
                    print('ATENÇÃO: Caso a corrida seja simulada antes de sua votação, você perderá a oportunidade de votar.')
                    time.sleep(5)

            case 2:
                tupla_corrida = corrida.estruturar_corrida()
                percurso_corrida = corrida.curva_reta(tupla_corrida[1],
                                                     tupla_corrida[2],
                                                     tupla_corrida[0])
                num_voltas = corrida.voltas_corredores(percurso_corrida)
                print('RESULTADO FINAL DA CORRIDA')
                posicao_corredor = pontos.definir_ganhador(num_voltas)
                if votacao.votacao is True:
                    votacao.checar_palpite(votacao.escolha_piloto,
                                          posicao_corredor,
                                          nome_cadastrado)
                else:
                    print('\nVocê não participou do processo de votação.')
                    print('Portanto, não poderá votar depois.')
                time.sleep(5)

            case 3:
                if corrida.corrida_estruturada is True:
                    print('''A corrida já aconteceu, você já não pode mais votar.
Deseja reiniciar a corrida?''')
                    try:
                        opcao = int(input('1 - Sim\n2 - Não\n'))
                        if opcao == 1:
                            corrida.corrida_estruturada = False
                            votacao.escolha_piloto = {}
                            print('Corrida reiniciada')
                        elif opcao == 2:
                            print('Não houve reinicio.')
                        else:
                            print('Opção inválida. Tente novamente.')
                    except ValueError:
                        print("Entrada inválida. Por favor, insira 1 para Sim ou 2 para Não.")
                else:
                    if login.login_status is True:
                        try:
                            pontos_usuario = int(dicionario_contas[nome_cadastrado]['pontos'])
                        except (KeyError, ValueError):
                            print("Erro ao acessar os pontos do usuário. Verifique se o usuário está logado corretamente.")
                            continue
                        pontos_usuario, votacao.votacao = votacao.votar_piloto(
                            votacao.escolha_piloto, votacao.corredores, pontos_usuario)
                        dicionario_contas[nome_cadastrado]['pontos'] = str(pontos_usuario)
                        banco_de_dados.atualizar_pontos_usuario(dicionario_contas, nome_cadastrado)
                    else:
                        print('Você deve estar logado para votar')
                time.sleep(2.5)

            case 4:
                if login.login_status is False:
                    _, nome_cadastrado = login.login_usuario(dicionario_contas)
                else:
                    print('Você já está logado')
                time.sleep(2.5)

            case 5:
                if login.login_status is False:
                    dicionario_contas, nome_cadastrado, _ = login.cadastrar_usuario(dicionario_contas)
                    banco_de_dados.adicionar_usuario(dicionario_contas, nome_cadastrado)
                else:
                    print('Não é possível se cadastrar, você já está logado')
                time.sleep(2)

            case 6:
                if not login.login_status:
                    print('Para deslogar, é preciso primeiro estar logado')
                else:
                    login.login_status = False
                    print('Deslogado com sucesso!')
                time.sleep(3)

            case 7:
                print('Saindo do programa...')
                time.sleep(2)
                break

            case _:
                print('Opção inválida. Por favor, escolha um número dentro das opções.')
                time.sleep(2)


menu()
