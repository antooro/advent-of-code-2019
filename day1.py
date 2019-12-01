import math

lista = open("input1").read().splitlines()

suma = 0
for l in lista:
    parc = int(l)

    while parc > 0:
        parc = max ( 0 ,math.floor((parc)/3) - 2)
        suma += parc
        
print(suma)