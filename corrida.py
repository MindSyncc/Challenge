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
vel_carro = [vel_nick, vel_pascal, vel_oliver]
nick, pascal, oliver = 0, 0, 0
pontos_nick, pontos_pascal, pontos_oliver = [], [], []

# Número de curvas e tamanho da corrida
num_curvas = random.randint(10, 20)
tamanho_corrida = random.randint(2500, 3000)  # Tamanho da corrida entre 2.5 e 3.0 km
tamanho_reta = 3 * (tamanho_corrida / num_curvas) / 4
tamanho_curva = 1 * (tamanho_corrida / num_curvas) / 4
lista_curva_reta = []
soma_corrida = 0
print(f'O número de curvas na corrida é {num_curvas}')
# Criando a lista de curvas e retas
while soma_corrida < tamanho_corrida:
    lista_curva_reta.append(soma_corrida)
    soma_corrida += tamanho_curva
    lista_curva_reta.append(soma_corrida)
    soma_corrida += tamanho_reta    
    
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

# Função para atualizar a posição dos carros
def posicao_carro():
    global vel_carro
    global posicao
    global tamanho_corrida
    while True:        
        for i in range(3):
            posicao[i] += vel_carro[i]
            if posicao[i] >= tamanho_corrida:
                posicao[i] -= tamanho_corrida
                voltas_lista[i] += 1
                nick = voltas_lista[0]
                pascal = voltas_lista[1]
                oliver = voltas_lista[2]                 
        time.sleep(1)
        if tempo < 2:
            break
def pontos(): #sistema de pontos
    global nick, pascal, oliver
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


            
