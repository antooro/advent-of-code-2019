from collections import defaultdict

with open("input3") as f:
    lineas = f.read().splitlines()

dic = defaultdict(set)
puntos = defaultdict(list)
i = 0
for l in lineas:
    movimientos = l.split(",")
    x = 0
    y = 0
    puntos[i].append((x,y))

    for m in movimientos:
        unidad = int(m[1:])
        if   "R" in m:
            for u in range(1,unidad+1):
                x += 1
                dic[i].add((x,y))
                puntos[i].append((x,y))

        elif "L" in m:
            for u in range(1,unidad+1):
                x -= 1
                dic[i].add((x,y))
                puntos[i].append((x,y))


        elif "U" in m:
            for u in range(1,unidad+1):
                y += 1
                dic[i].add((x,y))
                puntos[i].append((x,y))


        elif "D" in m:
            for u in range(1,unidad+1):
                y -= 1
                dic[i].add((x,y))
                puntos[i].append((x,y))



    i = i + 1

res = dic[0]
for i in range(1, len(dic.values())):
    res = res & dic[i]

minx = 99999999999
for punto in res:
    #print(puntos[0].index(punto))
    #print(puntos[1].index(punto))
    suma = puntos[0].index(punto) + puntos[1].index(punto)
    if suma < minx:
        minx = suma
print(minx)
    
'''
part1
minx = 9999999
for punto in res:
    dis_x = abs(0-punto[0])
    dis_y = abs(0-punto[1])
    dist = dis_x+dis_y
    if dist < minx:
        minx = dist
print(minx) 
'''