import random
import time
def tempo_corrida(minutos): #tempo corrida devera ser = 45
    segundos = 60 * minutos
    while segundos:
        mins, secs = divmod(segundos, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        segundos -= 1
    print('Acabou a corrida')


tamanho_corrida = random.uniform(2.5, 3.0)
attack_mode_posicao = random.uniform(0, tamanho_corrida)
vel_carro = 0.1
posicao = 0
def curvas():
    global tempo
    num_curvas = random.randint(10, 20)
    curvas_total = tempo * num_curvas
def posicao_carro():
    while True:
        global posicao
        global tamanho_corrida
        posicao += vel_carro

        if posicao == tamanho_corrida:
            posicao == 0
