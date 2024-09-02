'''Versão 1.0.5'''
import corrida


def menu():
    print('''Opções do Cartola Formula
    1-Exibir informações da pista?
    2-Simular uma corrida
    3-Estatisticas do piloto
    4-Votacao do piloto
    5-Sair      
    ''')
    opcoes = int(input(''))
    tupla_corrida = corrida.estruturar_corrida()
    match opcoes:
        case 1:
            for estrutura in range(len(tupla_corrida)):
                match estrutura:
                    case 0:
                        print(f'O número de curvas será {tupla_corrida[estrutura]}')
                        print('='*37)
                    case 1:
                        print(f'Uma volta tem {tupla_corrida[estrutura]} metros')
                        print('='*37)
                    case 2:
                        print(f'O tamanho de cada reta é {tupla_corrida[estrutura]} metros')
                        print('='*37)
                    case 3:
                        print(f'Cada curva tem  {tupla_corrida[estrutura]} metros ')
                        print('='*37)
            menu()
        case 2:
            if corrida.corrida_estruturada is False:
                print("Crie o tamanho da corrida primeiro para ela ser avaliada")
                menu()
            else:
                percurso_corrida = corrida.curva_reta(tupla_corrida[1],
                                                      tupla_corrida[2],
                                                      tupla_corrida[0])
                print(corrida.voltas_corredores(percurso_corrida))
        case _:
            print('Digite algum número')
            return menu()


menu()
