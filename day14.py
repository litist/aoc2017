import day10

def print_grid(g):
    for col in g:
        s = ''
        for r in col:
            s += '{:4}'.format(r)
        print(s)


input = 'flqrgnkx'
input = 'nbysizxe'

sq_used = 0

grid = []

for col in range(128):
    row = ''
    for c in day10.knot_hash('{}-{}'.format(input, col)):
        b_string = bin(int(c, base=16)+16)
        #print(b_string[-1-3:])
        row += b_string[-1-3:]

    print(row)

    grid.append([])

    for i in range(len(row)):
        if row[i] == '1':
            grid[col].append('#')
            sq_used += 1
        else:
            grid[col].append('.')

print_grid(grid)

print('Used squares: {}'.format(sq_used))


def rec_spread_groups(c, r, g, N):
    #print('{} {} g {} '.format(c, r, N))
    if c < 0 or c >= len(g) or r < 0 or r >= len(g[c]):
        return

    if g[c][r] == '.':
        return

    if g[c][r] == N:
        return

    if g[c][r] != '#':
        print('Error {} {}  {}'.format(c, r, g[c][r]))
        return

    g[c][r] = N

    rec_spread_groups(c-1, r, g, N)
    rec_spread_groups(c+1, r, g, N)
    rec_spread_groups(c, r-1, g, N)
    rec_spread_groups(c, r+1, g, N)



N_groups = 0

for c_idx in range(len(grid)):
    for r_idx in range(len(grid[c_idx])):
        if grid[c_idx][r_idx] == '#':
            N_groups += 1
            #print('Start rec {} {}  {}'.format(c_idx, r_idx, grid[c_idx][r_idx]))
            rec_spread_groups(c_idx, r_idx, grid, N_groups)

print_grid(grid)

print('Found {} groups'.format(N_groups))