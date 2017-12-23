registers = {}

for reg in range(ord('z') - ord('a') + 1):
    registers[chr(reg + ord('a'))] = 0

def getVal(data):

    if data >= 'a' and data <= 'z':
        # get register value
        return registers[data]
    else:
        return int(data)


instructions = []

with open('day18.data') as file:
    for instruction in file.readlines():
        instructions.append(instruction.split())


pc = 0
freq = -1

while pc<len(instructions):
    inst = instructions[pc]

    print('pc: {} inst: {}'.format(pc, inst))

    if inst[0] == 'set':
        registers[inst[1]] = getVal(inst[2])

    elif inst[0] == 'mul':
        print(inst)
        registers[inst[1]] = registers[inst[1]] * getVal(inst[2])

    elif inst[0] == 'add':
        registers[inst[1]] = registers[inst[1]] + getVal(inst[2])

    elif inst[0] == 'mod':
        registers[inst[1]] = getVal(inst[1]) % getVal(inst[2])

    elif inst[0] == 'jgz':
        if getVal(inst[1]) > 0:
            pc += getVal(inst[2])
            continue

    elif inst[0] == 'snd':
        freq = getVal(inst[1])

    elif inst[0] == 'rcv':
        if getVal(inst[1]) != 0:
            break

    else:
        print('Unknown instruction: {}'.format(inst))

    pc += 1

print(freq)
print(registers)



