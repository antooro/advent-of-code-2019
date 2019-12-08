import random
import copy
from collections import defaultdict
from itertools import permutations

try:
    clista = open("input7").read().split(",")
except:
    clista = open("day7/input7").read().split(",")

clista = [int(l) for l in clista]
opcodes = [1,2,3,4,5,6,7,8,99]



def safe_list_get (l, idx, default):
  try:
    return int(l[idx])
  except IndexError:
    return 0

def endCode(code):
    return code.endswith("01") or code.endswith("02") or code.endswith("03") or code.endswith("04") \
    or code.endswith("05") or code.endswith("06") or code.endswith("07") or code.endswith("08") 

def isOpcode(code):
    code = str(code)
    
    if int(code) in opcodes:
        return True, {}

    if endCode(code) or code == "99":
        for l in code[:-1]:
            if l not in ["0","1"]:
                return False, {}

        d = dict()
        d[0] = safe_list_get(code,-5,0)
        d[1] = safe_list_get(code,-4,0)
        d[2] = safe_list_get(code,-3,0)
        return True,d
    else:
        return False, []


'''
ABCDE
 1002

DE - two-digit opcode,      02 == opcode 2
 C - mode of 1st parameter,  0 == position mode
 B - mode of 2nd parameter,  1 == immediate mode
 A - mode of 3rd parameter,  0 == position mode,
                                  omitted due to being a leading zero
'''
dic = {}
estado = defaultdict(list)
lista = copy.deepcopy(clista)

vuelta = defaultdict(int)
for i in range(0,5):
    estado[str(i)] = [0,copy.deepcopy(lista),0,1]

indices = {
    "0":4,
    "1":0,
    "2":1,
    "3":2,
    "4":3
}

i = 0
n_amp = 0
for permutation in permutations(list(range(5,10))):
    resultados = 0
    output = 0
    while True:
        cont = 0
        while True:
            act_n_amp = n_amp
            activo =  estado[str(n_amp)][3]
            if (activo == 0):
                n_amp = (n_amp+ 1)%5
                continue
            
            lista = estado[str(n_amp)][1]
            index = estado[str(n_amp)][2]
            value = estado[str(n_amp)][1][index]
            i = index

            paramet = dict()
            if value not in [3,4]:
                
                escodigo, paramet = isOpcode(value)

                    

            valor1 = 0
            valor2 = 0
            if paramet:
                
                if paramet[2] == 1:
                    valor1 = lista[index+1]
                else:
                    valor1 = lista[lista[index+1]]

                if paramet[1] == 1:
                    valor2 = lista[index+2]
                else:
                    valor2 = lista[lista[index+2]]

            elif str(value).endswith("1") or str(value).endswith("2") or str(value).endswith("5") or str(value).endswith("6") or str(value).endswith("7") or str(value).endswith("8") :
                valor1 = lista[lista[index+1]]
                valor2 = lista[lista[index+2]]
            
            #CODES
            if str(value).endswith("1"):
            
                lista[lista[index+3]] = int(valor1) + int(valor2)
                i+=4

            elif str(value).endswith("2"):
                lista[lista[index+3]] = int(valor1) * int(valor2)
                i+=4

            elif value == 3:
                #lista[lista[index+1]] = input("introduce un numero")
                if cont == 0 and vuelta[str(n_amp)] == 0:
                    lista[lista[index+1]] = permutation[n_amp]
                    vuelta[str(n_amp)] = 1
                    cont += 1
                else:
                    indi = indices[str(n_amp)]
                    lista[lista[index+1]] = estado[str(indi)][0]


                i+=2

            elif str(value).endswith("4"):
                valor = 0
                if value == 4:
                    valor = (lista[lista[index+1]])
                else:
                    valor = (lista[index+1])
                output = valor
                key = (''.join(str(p) for p in permutation ))
                dic[key] = valor

                i+=2
                estado[str(n_amp)] = [output, copy.deepcopy(lista),i,1]
                n_amp = (n_amp+ 1)%5
                cont = 0

            elif str(value).endswith("5"):

                if int(valor1) != 0:
                    i = int(valor2)
                else:
                    i += 3 

            elif str(value).endswith("6"):
                if int(valor1) == 0:
                    i = int(valor2)
                else:
                    i += 3

            elif str(value).endswith("7"):
                if int(valor1) < int(valor2):
                    lista[lista[index+3]] = 1
                else:
                    lista[lista[index+3]] = 0
                i += 4

            elif str(value).endswith("8"):
                if int(valor1) == int(valor2):
                    lista[lista[index+3]] = 1
                else:
                    lista[lista[index+3]] = 0
                i += 4

            elif value == 99:
                estado[str(act_n_amp)][3] = 0
                resultados +=1
                if(resultados == 5):
                    resultados == 0
                    for i in range(0,5):
                        estado[str(i)] = [0,copy.deepcopy(clista),0,1]
                        vuelta[str(i)] = 0

                    break


            estado[str(act_n_amp)][2] = i
        i = 0
        break

    n_amp = 0

print(dic)
print(max(dic.values()))