# USING BASE DAY 5 CODE FROM @DVRODRI8
# 
# https://raw.githubusercontent.com/DVRodri8/advent-of-code-2019/master/5/main.py

import sys
from collections import defaultdict

class Opcode():
    def __init__(self, full_opcode):
        self.full_opcode = "{:05d}".format(int(full_opcode))
        self.op_code = int(self.full_opcode[-2:])
        self.modes   = list(map(int, self.full_opcode[:3]))

    def getOC(self):
        return self.op_code
    
    def getModes(self):
        return self.modes

class intMachine():
    def __init__(self, program):
        self.program = program
        self.p = 0
        self.ter = set([1,2,7,8])
        self.bin = set([5,6])
        self.offset = 0
        self.cont = 0
        self.coord = [0,0]
        self.dic = defaultdict(list)
        self.res = 0
    def run(self):
        while True:
            foc = self.readOC()
            if foc.getOC() == 99:
                print(f"Resultado {self.res}")
                break
            a,b,c = foc.getModes()
            
            if foc.getOC() in self.ter:
                op1 = self.readNext(c)
                op2 = self.readNext(b)
                if a == 0: a +=1
                op3 = self.readNext(a,w=1)
                self.writeTo(op3, self.calc2(foc.getOC(), op1, op2))
            elif foc.getOC() in self.bin:
                op1 = self.readNext(c)
                op2 = self.readNext(b)
                self.p = self.calc(foc.getOC(), op1, op2)
            else:
                self.io(foc.getOC(),c)
            
    def readOC(self):
        raw = self.readNext(1)
        return Opcode(raw)
    
    def readNext(self, mode=1 ,w=0):
        r = self.program[self.p]
        self.p += 1
        if mode == 0: r = self.program[r]
        elif mode == 2: 
            r = self.offset + int(r)
            if w==0:
                r = self.program[r]
        return int(r)
    
    def calc(self, mode, a, p):
        if (mode == 5):  return p if a!=0 else self.p
        elif(mode == 6): return p if a==0 else self.p
        else:            print("Algo ha ido mal", file = sys.stderr)


    def calc2(self, mode, a, b):
        if(mode == 1):   return a+b
        elif(mode == 2): return a*b
        elif(mode == 7): return 1 if a<b else 0
        elif(mode == 8): return 1 if a==b else 0
        else:            print("algo ha ido mal",file=sys.stderr)
    
    def writeTo(self, d, v):
        self.program[d] = v

    def io(self, mode, c):
        if mode == 3:
            d = self.readNext(c,w=1)
            import random
            a = random.choice([0,1,-1])
            self.writeTo(d, a) 
        elif mode == 4:
            self.cont += 1
            d = self.readNext(c) 
            if self.cont % 3 == 0:
                if self.coord == [-1,0]:
                    self.res = d
                else:
                    self.dic[d].append(self.coord)
                    self.coord = [0,0]
            else:
                self.coord[(self.cont%3) - 1] = d
                
            #print("Salida:", d)
        elif mode == 9:
            self.offset += self.readNext(c)
        else:
            print("algo ha ido mal en io",file=sys.stderr)

#nums = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,91,92,225,1102,85,13,225,1,47,17,224,101,-176,224,224,4,224,1002,223,8,223,1001,224,7,224,1,223,224,223,1102,79,43,225,1102,91,79,225,1101,94,61,225,1002,99,42,224,1001,224,-1890,224,4,224,1002,223,8,223,1001,224,6,224,1,224,223,223,102,77,52,224,1001,224,-4697,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1101,45,47,225,1001,43,93,224,1001,224,-172,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,1102,53,88,225,1101,64,75,225,2,14,129,224,101,-5888,224,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,101,60,126,224,101,-148,224,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1102,82,56,224,1001,224,-4592,224,4,224,1002,223,8,223,101,4,224,224,1,224,223,223,1101,22,82,224,1001,224,-104,224,4,224,1002,223,8,223,101,4,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,677,224,102,2,223,223,1005,224,329,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,344,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,359,1001,223,1,223,107,226,677,224,102,2,223,223,1006,224,374,101,1,223,223,8,677,677,224,102,2,223,223,1006,224,389,1001,223,1,223,1008,226,677,224,1002,223,2,223,1006,224,404,101,1,223,223,7,677,677,224,1002,223,2,223,1005,224,419,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,434,101,1,223,223,1108,226,226,224,102,2,223,223,1005,224,449,1001,223,1,223,107,226,226,224,102,2,223,223,1005,224,464,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,479,101,1,223,223,1007,226,677,224,102,2,223,223,1005,224,494,1001,223,1,223,1008,226,226,224,1002,223,2,223,1005,224,509,1001,223,1,223,1108,677,226,224,1002,223,2,223,1006,224,524,1001,223,1,223,108,677,677,224,1002,223,2,223,1005,224,539,101,1,223,223,108,226,677,224,1002,223,2,223,1005,224,554,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,569,1001,223,1,223,1107,677,677,224,102,2,223,223,1005,224,584,1001,223,1,223,7,677,226,224,102,2,223,223,1005,224,599,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,614,1001,223,1,223,7,226,677,224,1002,223,2,223,1006,224,629,101,1,223,223,1107,677,226,224,1002,223,2,223,1005,224,644,1001,223,1,223,1107,226,677,224,102,2,223,223,1006,224,659,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226]

with open("input13") as f:
    text = f.read()

s_t = "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"

text = (text.replace(s_t,s_t.replace("0","3")))

nums = [int(n) for n in text.split(",")]

print("Part 2")
maquina = intMachine(nums+ [0]*900000)
maquina.run()

print("Part 1")
print(len(maquina.dic[2]))
