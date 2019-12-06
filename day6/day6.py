from collections import defaultdict
import networkx as nx

with open("input6") as f:
    datos = f.read().splitlines()

#print(datos)

diccionario = defaultdict(list)

for d in datos:
    linea = d.split(")")

    diccionario[linea[0]].append(linea[1])



g = nx.Graph()
g.add_nodes_from(diccionario.keys())
for k, v in diccionario.items():
    g.add_edges_from(([(k, t) for t in v]))



print("PART 1") 
valores = set()

for k,v in diccionario.items():
    valores.add(k)
    valores.update(v)

contador = 0
for value in valores:
    contador +=(nx.shortest_path_length(g,source="COM",target=value))

print(contador)


print("PART 2") 
print(   nx.shortest_path_length(g,source="SAN",target="YOU") -2)
