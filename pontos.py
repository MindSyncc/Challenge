import random
def adicao_pontos():
    lista_media = [20, 16, 10]
    nick_cassady = []
    pascal_wehrlein = []
    oliver_rowland = []
    lista = [nick_cassady, pascal_wehrlein, oliver_rowland]
    for i in range(len(lista)):
        lista_random = []
        for j in range(4):                        
            lista_random.append(random.randint(8, 11))            
            lista[i].append(random.randint(lista_random[i], lista_media[i]))
def media_pontos():
    adicao_pontos()

    
    
    