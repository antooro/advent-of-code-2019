import random
import copy
from collections import defaultdict

lista = open("input5").read().split(",")
lista = [int(l) for l in lista]
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

i = 0
while True:
    value = lista[i]
    index = i
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
        lista[lista[index+1]] = input("introduce un numero")
        i+=2

    elif str(value).endswith("4"):
    
        if value == 4:
            print(lista[lista[index+1]])
        else:
            print(lista[index+1])

        i+=2
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
        break

