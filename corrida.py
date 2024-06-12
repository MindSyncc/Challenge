import random
import math
'''
Todos os valores usados abaixo ainda não são baseados em dados coletados de corrida, apenas do site da Formula E.
Em versões futuras os códigos serão melhorados e baseados em dados muito mais consistentes.
Versão 1.0.5
'''
    

# Inicia a thread do temporizador

# Função para o modo de ataque

cont = 0  # serve como variavel contadora de tempo (45 min * 60) = 2700s
curva = 0


# Função para calcular a velocidade dos pilotos
def velocidade_corredores():
    global cont, vel_carro, lista_curva_reta
    for j in range(3):
        if curva % 2 == 0:  # Curva
            vel_carro.append(int(random.randint(70, 130) / 3.6))  # Conversão de km/h para m/s            
        else:  # Reta
            vel_carro.append(int(random.randint(200, 250) / 3.6))                                    


# Função para atualizar a posição dos carros
def posicao_carro():
    global cont, curva, vel_carro, posicao, tamanho_corrida
    while True:
        velocidade_corredores()
        for i in range(len(posicao)):
            posicao[i] += vel_carro[i]
            if posicao[i] >= math.ceil(soma_corrida):
                posicao[i] -= math.ceil(soma_corrida)
                voltas_lista[i] += 1
                
        if cont >= 60:
            break
        vel_carro = []
        cont += 1
        curva += 1
    for k in range(3):        
        voltas_lista[k] += (posicao[k] / 10000)    


posi_nick, posi_pascal, posi_oliver = 0, 0, 0  # Variáveis de posição de cada piloto
posicao = [posi_nick, posi_pascal, posi_oliver]  # Lista que guarda as posições
# Voltas de cada piloto
voltas_lista = [0, 0, 0]  # Lista que guarda o número de voltas
vel_nick, vel_pascal, vel_oliver = 0, 0, 0  # Velocidade inicial de cada piloto
vel_carro = []


# Número de curvas e tamanho da corrida
# Obs: Vale ressaltar que os valores abaixos são estimados, pois como as corridas da Formula E são realizadas em  circuitos temporários montados em ruas e avenidas de grandes cidades ao redor do mundo, as pistas terão diferentes formatos e traçados

num_curvas = random.randint(10, 20) # Normalmente as corridas da Formula E geralmente possuem de 10 a 20 curvas 
tamanho_corrida = random.randint(2500, 2950) # Tamanho da corrida entre 2.5 e 3.0 km
tamanho_reta = 3 * (tamanho_corrida / num_curvas) / 4
tamanho_curva = 1 * (tamanho_corrida / num_curvas) / 4
lista_curva_reta = []
soma_corrida = 0


# A fim encontrar a distância aproximada de cada curva em uma corrida, a expressão (tamanho_corrida / num_curvas) utilizará o tamanho da corrida e irá dividi-lá pelo número de curvas
# Obs: o valor da distância de uma curva será correspondente ao início de uma curva em uma corrida até o começo de outra

tamanho_reta = 3 * (tamanho_corrida / num_curvas) / 4 # Estimamos que o tamanho de uma reta receberá 3/4 do valor da expressão (tamanho_corrida / num_curvas)
tamanho_curva = 1 * (tamanho_corrida / num_curvas) / 4 # Estimamos que o tamanho da curva receberá 1/4 do valor da expressão (tamanho_corrida / num_curvas)
lista_curva_reta = []  # Lista que armazenará as distâncias das curvas e retas da corrida
soma_corrida = 0  # Variável somadora que irá ser utilizada para parar a estrutura de repetição quando todas as distâncias de curvas e retas forem armazenadas na lista

# Imprime o número de curvas da corrida

# Criando a lista de curvas e retas
while soma_corrida < tamanho_corrida:
    soma_corrida += tamanho_curva
    lista_curva_reta.append(tamanho_curva)
    soma_corrida += tamanho_reta 
    lista_curva_reta.append(tamanho_reta)
    
tempo = 60    
# Posição para o modo de ataque
attack_mode_posicao = random.randint(0, num_curvas)

# Iniciar a corrida        
posicao_carro()
