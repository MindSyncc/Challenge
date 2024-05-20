import random
import time
import threading
'''
Todos os valores usados abaixo ainda não são baseados em dados coletados de corrida, apenas do site da Formula E.
Em versões futuras os códigos serão melhorados e baseados em dados muito mais consistentes.
Versão 1.0.0
'''
posi_nick, posi_pascal, posi_oliver = 0, 0, 0  # Variáveis de posição de cada piloto
posicao = [posi_nick, posi_pascal, posi_oliver]  # Lista que guarda as posições
voltas_nick, voltas_pascal, voltas_oliver = 0, 0, 0  # Voltas de cada piloto
voltas_lista = [voltas_nick, voltas_pascal, voltas_oliver]  # Lista que guarda o número de voltas
vel_nick, vel_pascal, vel_oliver = 0, 0, 0  # Velocidade inicial de cada piloto
vel_carro = [vel_nick, vel_pascal, vel_oliver]

# Número de curvas e tamanho da corrida
num_curvas = random.randint(10, 20)
tamanho_corrida = random.randint(2500, 3000)  # Tamanho da corrida entre 2.5 e 3.0 km
tamanho_reta = 3 * (tamanho_corrida / num_curvas) / 4
tamanho_curva = 1 * (tamanho_corrida / num_curvas) / 4
lista_curva_reta = []
soma_corrida = 0

# Criando a lista de curvas e retas
while soma_corrida < tamanho_corrida:
    lista_curva_reta.append(soma_corrida)
    soma_corrida += tamanho_curva
    lista_curva_reta.append(soma_corrida)
    soma_corrida += tamanho_reta

# Posição para o modo de ataque
attack_mode_posicao = random.randint(0, num_curvas)

# Função de temporizador
def temporizador(segundos):
    start_time = time.time()
    while time.time() - start_time < segundos:
        mins, secs = divmod(segundos, 60)
        time.sleep(1)
        segundos -= 1
    print('Tempo acabou')

# Inicia a thread do temporizador
thread_temporizador = threading.Thread(target=temporizador, args=(45 * 60,))
thread_temporizador.start()

# Função para o modo de ataque
def attack_mode():
    ganho_vel = random.randint(10, 15)  # Ganho de velocidade devido ao modo de ataque
    time.sleep(1)

# Função para calcular a velocidade dos pilotos
def velocidade_corredores():
    global vel_carro
    for i in range(len(vel_carro)):
        for j in range(len(lista_curva_reta)):
            if j % 2 == 0:  # Reta
                vel_carro[i] = random.randint(200, 250) / 3.6  # Conversão de km/h para m/s
            else:  # Curva
                vel_carro[i] = random.randint(70, 130) / 3.6
            time.sleep(1)

# Função para atualizar a posição dos carros
def posicao_carro():
    while True:
        velocidade_corredores()
        global posicao
        global tamanho_corrida
        for i in range(3):
            posicao[i] += vel_carro[i]
            if posicao[i] >= tamanho_corrida:
                posicao[i] -= tamanho_corrida
                voltas_lista[i] += 1
        time.sleep(1)

# Iniciar a corrida
posicao_carro()

            
