with open("input8") as f:
    data = f.readline()


tall = 6
width = 25

#tall = width = 2

datsxlayer = len(data)/width/tall
print(datsxlayer)
c = 0
numero = 0
acum = ""
datos = {}
zeros = {}
#0 is black, 1 is white, and 2 is transparent.
for index,d in enumerate(data):
    if c == 0:
        print(f"Layer {numero}")

    acum += d
    c += 1
    if ((index+1) % width == 0):
        if c == width*tall:
            c = 0
            datos[str(numero)] = acum
            zeros[str(numero)] = acum.count("0")
            numero = numero +1
            print(acum)
            acum = ""

        print()

print(datos)
index = min(zeros, key=zeros.get)

print(datos[str(index)].count("1") * datos[str(index)].count("2"))

from collections import defaultdict
comparaciones = defaultdict(list)
for d in datos.values():
    for index,dat in enumerate(d):
        comparaciones[str(index)].append(dat)

for k,v in comparaciones.items():
    for val in v:
        if val in ["0","1"]:
            comparaciones[k] = val
            break

print(list(comparaciones.values()))

for index,c in enumerate(list(comparaciones.values())):
    c = c.replace("0"," ")
    print(c,end="")
    
    if ((index+1) % width == 0):
        print()