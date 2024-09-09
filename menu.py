'''Versão 1.0.6'''
import corrida
import pontos
import votacao


def menu() -> None:
    "Função do menu"
    mensagem = '''Opções do Cartola Formula
    1-Exibir informações da pista?
    2-Simular uma corrida
    3-Estatisticas do piloto
    4-Votacao do piloto
    5-Sair      
    '''
    opcoes = int(input('Escolha sua opção '))
    tupla_corrida = corrida.estruturar_corrida()
    while True:
        print(mensagem)
        match opcoes:
            case 1:
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
            case 2:
                percurso_corrida = corrida.curva_reta(tupla_corrida[1],
                                                    tupla_corrida[2],
                                                    tupla_corrida[0])
                num_voltas = corrida.voltas_corredores(percurso_corrida)
                print(num_voltas)
                pontos.definir_ganhador(num_voltas)
            case 4:
                if corrida.corrida_estruturada is True:
                    print('Tá tentando votar depois que a corrida aconteceu? Boa sorte nessa')
                else:
                    votacao.votar_piloto()
            case 5:
                print('Saindo do programa...')
                break
            case _:
                print('Digite algum número dentro das opções')


menu()
