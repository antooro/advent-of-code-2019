import math

with open("input12") as f:
    datos = f.read().splitlines()

class Moon():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
        self.x_speed = 0
        self.y_speed = 0
        self.z_speed = 0

    def update_speed(self,inc_x = 0,inc_y = 0,inc_z = 0):
        self.x_speed += inc_x
        self.y_speed += inc_y
        self.z_speed += inc_z

    def update_pos(self):
        self.x += self.x_speed
        self.y += self.y_speed
        self.z += self.z_speed

    def __str__(self):
        return f"Position: {self.x} {self.y} {self.z}\nVel: {self.x_speed} {self.y_speed} {self.z_speed}"
    
    def getCoords(self):
        return f"Position: {self.x} {self.y} {self.z}"
    
    def getDatos(self):
        return f"{str(self.x)}{str(self.y)}{str(self.z)}{str(self.x_speed)}{str(self.y_speed)}{str(self.z_speed)}"
    def getEnergy(self):
        #pot: 2 + 1 + 3 =  6;   kin: 3 + 2 + 1 = 6;   total:  6 * 6 = 36
        return (abs(self.x)+abs(self.y)+abs(self.z)) * \
            (abs(self.x_speed)+abs(self.y_speed)+abs(self.z_speed))
    def miHash(self):
        return f"{hash(str(self.x))}{hash(str(self.y))}{hash(str(self.z))}{hash(str(self.x_speed))} \
            {hash(str(self.y_speed))}{hash(str(self.z_speed))}"
lista_lunas = []
for d in datos:
    d = d.replace("=","--").replace(",","--").replace(">","").split("--")
    params = []
    for datin in d:
        try:
            params.append(int(datin))
        except:
            pass

    x,y,z = (params)
    lista_lunas.append(Moon(x,y,z))

import itertools
combi = (list(itertools.combinations(lista_lunas,2)))

step = 0

datosx = set()
datosy = set()
datosz = set()

def lcm(x, y):
    a, b = x, y
    while a:
        a, b = b % a, a
    return x // b * y

run  = True
while run:
    for c in combi:
        moon1 = c[0]
        moon2 = c[1]
        
        list_x = []
        list_y = []
        list_z = []

            

        if moon1.x > moon2.x:
            moon1.update_speed(-1)
            moon2.update_speed(1)
        elif moon2.x > moon1.x:
            moon1.update_speed(1)
            moon2.update_speed(-1)

        if moon1.y > moon2.y:
            moon1.update_speed(inc_y = -1)
            moon2.update_speed(inc_y = 1)
        elif moon2.y > moon1.y:
            moon1.update_speed(inc_y = 1)
            moon2.update_speed(inc_y = -1)

        if moon1.z > moon2.z:
            moon1.update_speed(inc_z = -1)
            moon2.update_speed(inc_z = 1)
        elif moon2.z > moon1.z:
            moon1.update_speed(inc_z = 1)
            moon2.update_speed(inc_z = -1)
    
    
        

    for moon in lista_lunas:
        moon.update_pos()
        list_x.append((moon.x,moon.x_speed))
        list_y.append((moon.y,moon.y_speed))
        list_z.append((moon.z,moon.z_speed))



    if tuple(list_x) in datosx and tuple(list_y) in datosy and tuple(list_z) in datosz:
        print(lcm(len(datosx), lcm(len(datosy), len(datosz))))
        run = False
        break
    else:
        datosx.add(tuple(list_x))
        datosy.add(tuple(list_y))
        datosz.add(tuple(list_z))
    step += 1


'''
pART 1
total_energy = 0
for moon in lista_lunas:
    total_energy += moon.getEnergy()
print(total_energy)
'''