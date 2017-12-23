class Tablet:

    def getVal(self, data):

        if data >= 'a' and data <= 'z':
            # get register value
            return self.registers[data]
        else:
            return int(data)

    def __init__(self, id):
        self.registers = {}
        self.instructions = []
        self.pc = 0
        self.id = id
        self.wait = False
        self.n_mul = 0



        # load instructions
        with open('day23.data') as file:
            for instruction in file.readlines():
                self.instructions.append(instruction.split())


        for reg in range(ord('h') - ord('a') + 1):
            self.registers[chr(reg + ord('a'))] = 0

        self.registers['a'] = 1

        self.pc = 0


    def showRegs(self):
        for reg in range(len(self.registers)):
            print('reg[{}]: {} '.format(chr(reg + ord('a')), self.registers[chr(reg + ord('a'))]))


    def runInst(self):
        if self.pc < 0 or self.pc >= len(self.instructions):
            print('PC exceeds instruction space')
            return False


        inst = self.instructions[self.pc]

        #print('id: {} pc: {} inst: {}'.format(self.id, self.pc, inst))
        #self.showRegs()

        if inst[0] == 'set':
            self.registers[inst[1]] = self.getVal(inst[2])

        elif inst[0] == 'mul':
            self.n_mul += 1
            self.registers[inst[1]] = self.registers[inst[1]] * self.getVal(inst[2])

        elif inst[0] == 'sub':
            self.registers[inst[1]] = self.registers[inst[1]] - self.getVal(inst[2])

        elif inst[0] == 'mod':
            self.registers[inst[1]] = self.getVal(inst[1]) % self.getVal(inst[2])

        elif inst[0] == 'jnz':
            #print('jnz {}/{} {}/{}'.format(inst[1], self.getVal(inst[1]), inst[2], self.getVal(inst[2])))
            if self.getVal(inst[1]) != 0:
                self.pc += self.getVal(inst[2])
                return True
        else:
            print('Unknown instruction: {}'.format(inst))

        self.pc += 1

        return True


t1 = Tablet(0)


#for a in range(200):
while True:
    if not t1.runInst():
        break


print('#mul: {}'.format(getattr(t1, 'n_mul')))


print('#reg: {}'.format(getattr(t1, 'registers')))
