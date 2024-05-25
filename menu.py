import time

time.sleep(2)
def menu():
    print('''Deseja iniciar a corrida
    1-Sim
    2-Não''')
    inicio_corrida = int(input(''))
    if inicio_corrida == 1:
        import corrida 
    elif inicio_corrida == 2:
        menu()
menu()
