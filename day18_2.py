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
        self.recv_queue = []
        self.send_queue = []
        self.id = id
        self.wait = False
        self.n_send = 0


        # load instructions
        with open('day18.data') as file:
            for instruction in file.readlines():
                self.instructions.append(instruction.split())


        for reg in range(ord('z') - ord('a') + 1):
            self.registers[chr(reg + ord('a'))] = 0

        self.registers['p'] = id

        self.pc = 0

    def setSendQ(self, q):
        print('Id: {} add send queue {}'.format(self.id, q))
        self.send_queue = q


    def showRegs(self):
        for reg in range(ord('z') - ord('a') + 1):
            print('reg[{}]: {} '.format(chr(reg + ord('a')), self.registers[chr(reg + ord('a'))]))


    def runInst(self):
        inst = self.instructions[self.pc]

        print('id: {} pc: {} inst: {} snd: {} rcv: {}'.format(self.id, self.pc, inst, self.send_queue, self.recv_queue))

        if inst[0] == 'set':
            self.registers[inst[1]] = self.getVal(inst[2])

        elif inst[0] == 'mul':
            self.registers[inst[1]] = self.registers[inst[1]] * self.getVal(inst[2])

        elif inst[0] == 'add':
            self.registers[inst[1]] = self.registers[inst[1]] + self.getVal(inst[2])

        elif inst[0] == 'mod':
            self.registers[inst[1]] = self.getVal(inst[1]) % self.getVal(inst[2])

        elif inst[0] == 'jgz':
            if self.getVal(inst[1]) > 0:
                self.pc += self.getVal(inst[2])
                return

        elif inst[0] == 'snd':
            freq = self.getVal(inst[1])
            print('snd inst[1] : {}'.format(self.getVal(inst[1])))
            self.send_queue.insert(0, self.getVal(inst[1]))
            self.n_send += 1

        elif inst[0] == 'rcv':
            if len(self.recv_queue) == 0:
                # wait for items
                self.wait = True
                return
            else:
                self.wait = False
                self.registers[inst[1]] = self.recv_queue.pop(-1)

        else:
            print('Unknown instruction: {}'.format(inst))

        self.pc += 1


t1 = Tablet(0)
t2 = Tablet(1)

t1.setSendQ( getattr(t2, 'recv_queue'))
t2.setSendQ( getattr(t1, 'recv_queue'))



#for a in range(200):
while True:
    t1.runInst()
    t2.runInst()

    if getattr(t1, 'wait') and getattr(t2, 'wait'):
        print('Deadlock detected.')
        break


print('#send: {}'.format(getattr(t1, 'n_send')))
print('#send: {}'.format(getattr(t2, 'n_send')))
