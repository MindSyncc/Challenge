import random
import time
import threading
'''
Todos os valores usados abaixo ainda não são baseados em dados coletados de corrida, apenas do site da Formula E.
Em versões futuras os códigos serão melhorados e baseados em dados muito mais consistentes.
Versão 1.0.2
'''
posi_nick, posi_pascal, posi_oliver = 0, 0, 0  # Variáveis de posição de cada piloto
posicao = [posi_nick, posi_pascal, posi_oliver]  # Lista que guarda as posições
voltas_nick, voltas_pascal, voltas_oliver = 0, 0, 0  # Voltas de cada piloto
voltas_lista = [voltas_nick, voltas_pascal, voltas_oliver]  # Lista que guarda o número de voltas
vel_nick, vel_pascal, vel_oliver = 0, 0, 0  # Velocidade inicial de cada piloto
vel_carro = []
nick, pascal, oliver = 0, 0, 0
pontos_nick, pontos_pascal, pontos_oliver = [], [], []

# Número de curvas e tamanho da corrida
# Obs: Vale ressaltar que os valores abaixos são estimados, pois como as corridas da Formula E são realizadas em  circuitos temporários montados em ruas e avenidas de grandes cidades ao redor do mundo, as pistas terão diferentes formatos e traçados

num_curvas = random.randint(10, 20) # Normalmente as corridas da Formula E geralmente possuem de 10 a 20 curvas 
tamanho_corrida = random.randint(2500, 3000)  # Tamanho da corrida entre 2.5 e 3.0 km
tamanho_reta = 3 * (tamanho_corrida / num_curvas) / 4
tamanho_curva = 1 * (tamanho_corrida / num_curvas) / 4
lista_curva_reta = []
soma_corrida = 0
print(f'O número de curvas na corrida é {num_curvas}')

# A fim encontrar a distância aproximada de cada curva em uma corrida, a expressão (tamanho_corrida / num_curvas) utilizará o tamanho da corrida e irá dividi-lá pelo número de curvas
# Obs: o valor da distância de uma curva será correspondente ao início de uma curva em uma corrida até o começo de outra

tamanho_reta = 3 * (tamanho_corrida / num_curvas) / 4 # Estimamos que o tamanho de uma reta receberá 3/4 do valor da expressão (tamanho_corrida / num_curvas)

tamanho_curva = 1 * (tamanho_corrida / num_curvas) / 4 # Estimamos que o tamanho da curva receberá 1/4 do valor da expressão (tamanho_corrida / num_curvas)

lista_curva_reta = [] # Lista que armazenará as distâncias das curvas e retas da corrida
soma_corrida = 0 # Variável somadora que irá ser utilizada para parar a estrutura de repetição quando todas as distâncias de curvas e retas forem armazenadas na lista

corrida = 0
print(f'O número de curvas na corrida é {num_curvas}') #Imprime o número de curvas da corrida

# Criando a lista de curvas e retas
while soma_corrida < tamanho_corrida:
    soma_corrida += tamanho_curva
    lista_curva_reta.append(tamanho_curva)
    soma_corrida += tamanho_reta 
    lista_curva_reta.append(tamanho_reta)
    
print(f'O tamanho da corrida é {soma_corrida}')        

tempo = 60    
# Posição para o modo de ataque
attack_mode_posicao = random.randint(0, num_curvas)

# Função de temporizador
def temporizador(segundos):
    global tempo
    start_time = time.time()
    while segundos >= 1:
        mins, secs = divmod(segundos, 60)
        time.sleep(1)
        segundos -= 1
        tempo -= 60
        print(f'segundos restantes {segundos}')
    print('Tempo acabou')       

# Inicia a thread do temporizador
thread_temporizador = threading.Thread(target=temporizador, args=(1 * 60,))
thread_temporizador.start()

# Função para o modo de ataque
def attack_mode():
    ganho_vel = random.randint(10, 15)  # Ganho de velocidade devido ao modo de ataque
    time.sleep(1)

curva = 0
cont = 0

# Função para calcular a velocidade dos pilotos
def velocidade_corredores():
    global cont
    global vel_carro
    global lista_curva_reta
    #for x in range(len(vel_carro)):
    for j in range(3):
        if curva % 2 == 0:  # Curva
            vel_carro.append(int(random.randint(70, 130) / 3.6))  # Conversão de km/h para m/s
            print(f'A velocidade nesse segundo é {vel_carro[j]}')
        else:  # Reta
            vel_carro.append(int(random.randint(200, 250) / 3.6))
            print(f'A velocidade nesse segundo é {vel_carro[j]}')
            #time.sleep(1)
        cont += 1
    print(vel_carro, cont)

# Função para atualizar a posição dos carros
def posicao_carro():
    global cont
    global curva
    global vel_carro
    global posicao
    global tamanho_corrida
    while True:
        velocidade_corredores()
        for i in range(len(posicao)):
            posicao[i] += vel_carro[i]
            if posicao[i] >= tamanho_corrida:
                posicao[i] -= tamanho_corrida
                voltas_lista[i] += 1
                nick = voltas_lista[0]
                pascal = voltas_lista[1]
                oliver = voltas_lista[2]
        if cont >= 10:
            break
        vel_carro = []
        curva += 1
        #time.sleep(1)
    print(voltas_lista)


def pontos(): #sistema de pontos
    if nick > pascal and nick > oliver and pascal > oliver:
        pontos_nick.append(25)
        pontos_pascal.append(18)
        pontos_oliver.append(15)
    elif nick > pascal and nick > oliver and oliver > pascal:
        pontos_nick.append(25)
        pontos_pascal.append(15)
        pontos_oliver.append(18)          
    elif pascal > nick and pascal > oliver and nick > oliver:
        pontos_nick.append(18)
        pontos_pascal.append(25)
        pontos_oliver.append(15)
    elif pascal > nick and pascal > oliver and oliver > nick:
        pontos_nick.append(15)
        pontos_pascal.append(25)
        pontos_oliver.append(18)
    elif oliver > nick and oliver > pascal and nick > pascal:
        pontos_nick.append(18)
        pontos_pascal.append(15)
        pontos_oliver.append(25)
    elif oliver > nick and oliver > pascal and pascal > nick:
        pontos_nick.append(15)
        pontos_pascal.append(18)
        pontos_oliver.append(25)       
    
# Iniciar a corrida        
posicao_carro()
if tempo == 1:
    pontos()
    print(f'nick = {pontos_nick}')
    print(f'pascal = {pontos_pascal}')
    print(f'oliver = {pontos_oliver}')

