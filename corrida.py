import random
import time
import threading
posi_nick, posi_pascal, posi_oliver = 0
posicao = [posi_nick, posi_pascal, posi_oliver]

def temporizador(minutos): #tempo corrida devera ser = 45
    segundos = 60 * minutos
    while segundos:
        mins, secs = divmod(segundos, 60)        
        time.sleep(1)
        segundos -= 1
    print('Tempo acabou')
thread_temporizador = threading.Thread(target=temporizador, args=(45,))
thread_temporizador.start()

num_curvas = random.randint(10, 20)
tamanho_corrida = random.randint(2500, 3000)
attack_mode_posicao = random.randint(0, num_curvas)

def attack_mode():
    ganho_vel = random.randint(10, 15)
    temporizador(1)

voltas_nick = 0
voltas_pascal = 0
voltas_oliver = 0
voltas_lista = [voltas_nick, voltas_pascal, voltas_oliver]

vel_nick, vel_pascal, vel_oliver = 0
vel_carro = [vel_nick, vel_pascal, vel_oliver]
def velocidade_corredores():
    while True:
        temporizador(0.12)            
        vel_nick = random.randint(200, 250)
        vel_pascal = random.randint(200, 250)
        vel_oliver = random.randint(200, 250)

        
                  

    
'''
é preciso adicionar as condições de velocidade na curva, para isso preciso mexer em como as retas
e as curvas irão se comportar
'''

'''
o numero de curvas randomizado vai determinar a distância possível entre cada uma para que seja possível 
alterar a velocidade de cada um e guardar num banco de dados(talvez seja necessário média móvel para mais
consistência nos resultados)
'''
'''
criar velocidades dos pilotos que deveriam varias conforme o tempo, é necessário supor alguns dados
envolvendo velocidade e sua variação. Por isso irei criar uma randomização envolvendo a velocidade dos três pilotos principais
da temporada
'''
def posicao_carro():
    while temporizador(45) == True:
        velocidade_corredores()
        global posicao
        global tamanho_corrida
        for i in range(3):
            posicao[i] += vel_carro[i]
        for i in range(3):

            if posicao[i] == tamanho_corrida:
                posicao[i] = 0
                voltas_lista[i] += 1

posicao_carro()

            
