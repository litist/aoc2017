N = 16


def dance(N_dance):
    memory = []
    programs = []
    for i in range(N):
        programs.append(chr(ord('a') + i))

    with open('day16.data') as file:
        for line in file.readlines():
            for d in range(N_dance):

                memory.append(''.join(programs))

                for com in line.strip().split(','):

                    if com[0] == 's':
                        # spin
                        for s in range(int(com[1:])):
                            programs.insert(0, programs.pop())

                    elif com[0] == 'x':
                        # exchange at positions A/B : xA/B
                        A, B = map(lambda x: int(x), com[1:].split('/'))

                        tmp = programs[A]
                        programs[A] = programs[B]
                        programs[B] = tmp


                    elif com[0] == 'p':
                        A, B = com[1:].split('/')

                        # swap programs named A and B pA/B
                        for i in range(N):
                            if programs[i] == A:
                                programs[i] = B
                            elif programs[i] == B:
                                programs[i] = A
                    else:
                        print('Unknonw operation')


                if ''.join(programs) in memory:
                    print('found match {} in memory after {}'.format(''.join(programs), d))
                    print(memory)

                    for i in range(len(memory)):
                        if memory[i] == ''.join(programs):
                            print('diff: {}'.format(d - i + 1))

                            # if we found the repeat sequence
                            return dance(N_dance % (d - i + 1))




    print('dance({}) -> {}'.format(N_dance, programs))
    return programs





print(''.join(dance(1)))
print(''.join(dance(10000000)))
