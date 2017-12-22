# get next generator number
def get_next(prev, factor, modulo):

    while True:
        prev = (prev*factor) % 2147483647

        if (prev % modulo) == 0:
            return prev


    return None

# gen
genA = 16807;
genB = 48271;

modA = 4;
modB = 8;

valA = 883#65;
valB = 879#8921;

judge = 0

N = 5000000
for a in range(N):
    valA = get_next(valA, genA, modA)
    valB = get_next(valB, genB, modB)

    if valA & 0xFFFF == valB & 0xFFFF:
        judge += 1

    #print('{:10d} {:10d}'.format(valA, valB))
    #print('{:10d} {:10d}'.format(valA & 0xFFFF, valB & 0xFFFF))

print('Judge: {}'.format(judge))
