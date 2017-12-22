file=open("day22.data",'r')

x = 0
y = 0

grid2 = {}

with open('day22.data') as file:
    for line in file.readlines():
        x = 0
        for c in line.strip():
            print('x: {} y: {} -> {}'.format(x,y,c))

            if c == '#':
                if y not in grid2:
                    grid2[y] = {}

                (grid2[y])[x] = 1
            x += 1
        y -= 1



def print_grid(g, c):
    # get dimensions
    y_min = min(min(g), c[1])
    y_max = max(max(g), c[1])

    x_min = c[0]
    x_max = c[0]

    print('GRID')
    print(g)
    for y in g:
        print(g[y])
        x_min = min(x_min, min(g[y]))
        x_max = max(x_max, max(g[y]))

    print('Dimensions: {} - {} | {} - {}'.format(y_min, y_max, x_min, x_max))
    print('Carrier: x: {} y: {} dir: {}'.format(c[0], c[1], c[2]))

    for y in range(y_max, y_min-1, -1):
        line = ''
        for x in range(x_min, x_max+1):
            if y == c[1] and x == c[0]:
                line += '['
            else:
                line += ' '


            if y in g and x in g[y]:
                line += ' # '
            else:
                line += ' . '

            if y == c[1] and x == c[0]:
                line += ']'
            else:
                line += ' '


        print(line)


def carrier_step(g, c, infect):

    if c[1] in g and c[0] in g[c[1]]:
        # decrease
        c[2] = (c[2] + 3) % 4
    else:
        # move left, i.e. increase direction
        c[2] =  (c[2] + 1) % 4

    # if node in infected it becomes clean, otherwise it gets infected
    if c[1] in g and c[0] in g[c[1]]:
        del((g[c[1]])[c[0]])
    else:
        if c[1] not in g:
            g[c[1]] = {}

        infect[0] += 1
        (g[c[1]])[c[0]] = 1

    # move scanner into facing direction
    # 0 - up
    # 1 - left
    # 2 - down
    # 3 - right

    if c[2] == 0:
        # move up
        c[1] += 1

    if c[2] == 1:
        # move left
        c[0] -= 1

    if c[2] == 2:
        # move down
        c[1] -= 1

    if c[2] == 3:
        # move right
        c[0] += 1



# this is a 25x25 gird so the center is 13/13, i.e. 12/12 with 0-based indexing
carrier = list((12,-12,0))


print_grid(grid2, carrier)

infections = [0]
for i in range(10000):
    carrier_step(grid2, carrier, infections)

print_grid(grid2, carrier)

print('There are {} Infections after {} bursts'.format(infections, i+1))
