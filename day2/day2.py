import random
import copy
clista = open("input2").read().split(",")
clista = [int(l) for l in clista]
opcodes = [1,2,99]

for i in range(0,100):
    for z in range(0,100):

    
        lista = copy.deepcopy(clista)
        clista[1] = i
        clista[2] = z
        for index,value in enumerate(lista):
            if index%4 is not 0:
                continue
            if value in opcodes:
                if value == 1:

                    lista[lista[index+3]] = lista[lista[index+1]] + lista[lista[index+2]]

                elif value == 2:

                    lista[lista[index+3]] = lista[lista[index+1]] * lista[lista[index+2]]

                elif value == 99:
                    break
                

        print(lista[0], lista[1],lista[2])
        if lista[0] - 19690720 == 0:
            print("WIN")
            print(100*lista[1] + lista[2])
            exit()