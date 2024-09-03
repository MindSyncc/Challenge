'''Versão 1.0.6'''
import corrida
import pontos
import votacao


def menu():
    "Função do menu"
    print('''Opções do Cartola Formula
    1-Exibir informações da pista?
    2-Simular uma corrida
    3-Estatisticas do piloto
    4-Votacao do piloto
    5-Sair      
    ''')
    opcoes = int(input('Escolha sua opção '))
    tupla_corrida = corrida.estruturar_corrida()
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
                        print(f'Cada curva tem  {tupla_corrida[estrutura]} metros ')
            print('=' * 37)
            menu()
        case 2:
            if corrida.corrida_estruturada is False:
                print("Crie o tamanho da corrida primeiro para ela ser avaliada")
                menu()
            else:
                percurso_corrida = corrida.curva_reta(tupla_corrida[1],
                                                      tupla_corrida[2],
                                                      tupla_corrida[0])
                num_voltas = corrida.voltas_corredores(percurso_corrida)
                print(num_voltas)
                pontos.definir_ganhador(num_voltas)
                menu()
        case 4:
            votacao.votar_piloto()
        case 5:
            print('Saindo do programa...')
            exit()
        case _:
            print('Digite algum número dentro das opções')
            return menu()


menu()
