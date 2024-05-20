import random

def adicao_pontos():
    lista_media = [20, 16, 10] #sistema de ponto, eu nao acabei
    nick_cassady = []
    pascal_wehrlein = []
    oliver_rowland = []
    lista = [nick_cassady, pascal_wehrlein, oliver_rowland]
    for i in range(len(lista)):
        lista_maxima = [26, 26, 15]
        for j in range(4):                                             
            lista[i].append(random.randint(lista_media[i], lista_maxima[i]))
            
def media_pontos():
    adicao_pontos()

    
    
    
    