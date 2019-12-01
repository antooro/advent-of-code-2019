import math

lista = open("input1").read().splitlines()

suma_1 = 0
suma_2 = 0

for l in lista:
    parc = int(l)
    suma_1 += math.floor((parc)/3) - 2
    while parc > 0:
        parc = max ( 0 ,math.floor((parc)/3) - 2)
        suma_2 += parc
        
print(suma_1)
print(suma_2)