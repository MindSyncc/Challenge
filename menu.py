'''Versão 1.0.5'''


def menu():
    print('''Deseja iniciar a corrida
    1-Sim
    2-Não''')
    inicio_corrida = int(input(''))
    if inicio_corrida == 1:
        import corrida
        import pontos
    elif inicio_corrida == 2:
        return menu()


menu()
