from operator import eq
from itertools import cycle, islice

contador = 0
for num in range(123257,647015):
    if  (any(map(eq, str(num), str(num)[1:]))):
        v = 0
        mem = [288,288]
        #print(num)
        lista = set()
        for i,n in enumerate(str(num)):
            

            if int(n)>=v:
                v = int(n)
                if i > 0:
                    if mem[1] == v :
                        lista.add(mem[1])
                    if mem[0] == mem[1] and mem[1] == v:
                        lista.remove(mem[0])

                if (i == len(str(num)) -1 ) and len(lista)>0:
                    contador +=1
                if i != 0:
                    mem[0] = int(str(num)[i-1])
                mem[1] = int(str(num)[i])

            else:
                break
print(contador)

