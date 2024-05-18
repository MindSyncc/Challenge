
def media_pontos():
    nick_cassady = []
    pascal_wehrlein = []
    oliver_rowland = []
    nick_cassady = [15, 19, 26, 19]
    pascal_wehrlein = [26, 13, 10, 12]
    oliver_rowland = [0, 8, 15, 15]
    lista_pontos_participantes = [nick_cassady, pascal_wehrlein, oliver_rowland]
    lista_pontos_total = []
    for i in range(len(lista_pontos_participantes)):
        lista_pontos_total.append(sum(lista_pontos_participantes[i]))        
    nick_total = [lista_pontos_total[0]]
    pascal_total = [lista_pontos_total[1]]
    oliver_total = [lista_pontos_total[2]]
    
    