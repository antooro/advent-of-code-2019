import numpy as np
from collections import defaultdict
import itertools

from time import sleep, perf_counter as pc
t0 = pc()


def lineFromPoints(P,Q): 
    
    a = Q[1] - P[1] 
    b = P[0] - Q[0]  
    c = a*(P[0]) + b*(P[1])  

    range_a = list(range(min(Q[1],P[1]),max(Q[1],P[1])+1))
    range_b = list(range(min(Q[0],P[0]),max(Q[0],P[0])+1))
    
    min_x = min(Q[0],P[0])
    min_y = min(Q[1],P[1])

    max_x = max(Q[0],P[0])
    max_y = max(Q[1],P[1])

    puntos = set()

    '''
    if(b<0):  
        print("The line passing through points P and Q is:", 
              a ,"x ",b ,"y = ",c ,"\n")  
    else: 
        print("The line passing through points P and Q is: ", 
              a ,"x + " ,b ,"y = ",c ,"\n")  
    '''
    # ax + by = c
    # x = (c-by)/a
    # y = (c-ax)/b

    for y_val in range_a:
        try:
            x = (c-b*y_val)/a
        except:
            x = 0.0
        if x.is_integer():
            if int(x) >= min_x and int(x) <= max_x and y_val <= max_y and y_val >= min_y:
                puntos.add((int(x),y_val))

    for x_val in range_b:
        try:
            y = (c-a*x_val)/b
        except:
            y = 0.0
        if y.is_integer():
            if int(y) >= min_y and int(y) <= max_y and x_val <= max_x and x_val >= min_x:
                puntos.add((x_val,int(y)))

    puntos.discard(P)
    puntos.discard(Q)
    return puntos

with open("ex1") as f:
    datos = [list(l.strip().replace(".","0").replace("#","1")) for l in f.readlines()]

#print(x)


arry = np.array(datos)
#arry = arry.transpose()

puntos = defaultdict()

for (x,y), value in np.ndenumerate(arry):
    puntos[str(str(x)+","+str(y))] = int(value)

contador = defaultdict(int)

coords = [i for i,j in puntos.items() if j == 1]

#CAMBIAR INDICE del dict
for (x,y), value in np.ndenumerate(arry):
    if value == "0":
        continue
    for c in coords:
        z,k = c.split(",")
        z,k = int(z) , int(k)

        
        if (z,k) == (x,y):
            continue
        

        #print((x,y),(int(z),int(k)))
        lista = lineFromPoints((x,y),(int(z),int(k)))  
        flag = 0
        for l in lista:
#            print(l == (x,y))
            c_clean = (str(l[0])+","+str(l[1]))
            x_temp = int(c_clean.split(",")[0])
            y_temp = int(c_clean.split(",")[1])

            if c_clean in coords:
                flag = 1
                break
        if flag == 0:
            contador[str(x)+","+str(y)] += 1


        
ind = (max(contador, key=contador.get))
x,y = ind.split(",")
print(contador[str(x)+','+str(y)])

print(pc()-t0)