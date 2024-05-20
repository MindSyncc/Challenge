import random
import time
import threading
posi_nick, posi_pascal, posi_oliver = 0 #variavel posição de cada jogador
posicao = [posi_nick, posi_pascal, posi_oliver] #lista que guarda as posições

def temporizador(segundos): #função que vai servir para temporizar    
    while segundos:
        mins, secs = divmod(segundos, 60)        
        time.sleep(1)
        segundos -= 1
    print('Tempo acabou')
thread_temporizador = threading.Thread(target=temporizador, args=(45 * 60,)) #para que a contagem continue enquanto as outras funções tambem funcionam
thread_temporizador.start()

num_curvas = random.randint(10, 20) #numero de curvas baseado nas ultimas corridas
tamanho_corrida = random.randint(2500, 3000) #tamanho da corrida que varia de 2.5 a 3.0km
tamanho_reta = 3 * (tamanho_corrida / num_curvas) / 4 
tamanho_curva = 1 * (tamanho_corrida / num_curvas) / 4
lista_curva_reta = []
soma_corrida = 0
cont = 1
while  soma_corrida < tamanho_corrida:
    lista_curva_reta.append(soma_corrida) 
    soma_corrida += tamanho_curva
    lista_curva_reta.append(soma_corrida)
    soma_corrida += tamanho_reta        
    cont += 1    
attack_mode_posicao = random.randint(0, num_curvas) #onde o attack mode pode ser usado

def attack_mode():
    ganho_vel = random.randint(10, 15) #o tanto de velocidade que ganha geralmente, a potencia é 35kw. O que dá em torno de 10 a 15km/h
    temporizador(1)

voltas_nick = 0 #voltas de cada corredor
voltas_pascal = 0
voltas_oliver = 0
voltas_lista = [voltas_nick, voltas_pascal, voltas_oliver]#lista que guarda o numero de voltas

vel_nick, vel_pascal, vel_oliver = 0 #a velocidade começa no zero
vel_carro = [vel_nick, vel_pascal, vel_oliver]
def velocidade_corredores(vel_nick):
    global posi_nick
    global posi_pascal
    global posi_oliver
    for i in range(len(lista_curva_reta)):  
        if (i % 2 == 0):   #linha reta      
            vel_nick = random.randint(200, 250)
            vel_nick /= 3.6 #conversao de velocidade                                  
            temporizador(1)
        else:   #curva
            vel_nick = random.randint(70, 130)
            vel_nick /= 3.6            
    for i in range(len(lista_curva_reta)):  
        if (i % 2 == 0):   #linha reta      
            vel_pascal = random.randint(200, 250)
            vel_pascal /= 3.6 #conversao de velocidade                                  
            temporizador(1)
        else:   #curva
            vel_pascal = random.randint(70, 130)
            vel_pascal /= 3.6      
    for i in range(len(lista_curva_reta)):  
        if (i % 2 == 0):   #linha reta      
            vel_oliver = random.randint(200, 250)
            vel_oliver /= 3.6 #conversao de velocidade                                  
            temporizador(1)
        else:   #curva
            vel_oliver = random.randint(70, 130)
            vel_oliver /= 3.6              
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
        temporizador(1)

posicao_carro()

            
