


tape = {}


tape [0] = 0;

cursor = 0;
state = 'A'
N = 12425180


for i in range(N):



    if state == 'A':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor += 1
            state = 'B'
        elif tape[cursor] == 1:
            tape[cursor] = 0
            cursor += 1
            state = 'F'
        else:
            print('Undefined value')

    elif state == 'B':
        if tape[cursor] == 0:
            tape[cursor] = 0
            cursor -= 1
            state = 'B'
        elif tape[cursor] == 1:
            tape[cursor] = 1
            cursor -= 1
            state = 'C'
        else:
            print('Undefined value')

    elif state == 'C':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'D'
        elif tape[cursor] == 1:
            tape[cursor] = 0
            cursor += 1
            state = 'C'
        else:
            print('Undefined value')

    elif state == 'D':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'E'
        elif tape[cursor] == 1:
            tape[cursor] = 1
            cursor += 1
            state = 'A'
        else:
            print('Undefined value')

    elif state == 'E':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'F'
        elif tape[cursor] == 1:
            tape[cursor] = 0
            cursor -= 1
            state = 'D'
        else:
            print('Undefined value')

    elif state == 'F':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor += 1
            state = 'A'
        elif tape[cursor] == 1:
            tape[cursor] = 0
            cursor -= 1
            state = 'E'
        else:
            print('Undefined value')

    else:
        print('unknown state')

    # if cursor not in tape add default
    if cursor not in tape:
        tape[cursor] = 0


checksum = 0;
for i in tape:
    checksum += tape[i]

print('Checksum: {}'.format(checksum))