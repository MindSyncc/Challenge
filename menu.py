'''Versão 1.0.4'''
import time

time.sleep(1)
def menu():
    print('''Deseja iniciar a corrida
    1-Sim
    2-Não''')
    inicio_corrida = int(input(''))
    if inicio_corrida == 1:
        import corrida 
        import pontos
    elif inicio_corrida == 2:
        menu()
menu()

