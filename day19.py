maze = []

solution = []

with open('day19.data') as file:
    for m in file.readlines():

        maze.append(m.strip('\n'))

print(maze)


pos_row = 0;
pos_col = 0;
pos_dir = 'S'

for c in range(len(maze[pos_row])):
    if (maze[pos_row])[c] == '|':
        print(c)
        pos_col = c
        break

steps = 1

for i in range(100000):
    # step forward
    if pos_dir == 'S':
        pos_row += 1
    elif pos_dir == 'N':
        pos_row -= 1
    elif pos_dir == 'W':
        pos_col -= 1
    elif pos_dir == 'E':
        pos_col += 1
    else:
        print('unkwnown direction')

    #if pos_dir == 'N' and (maze[pos_row])[pos_col] == '|':
    # okay

    #if pos_dir == 'N' and (maze[pos_row])[pos_col] == '-':
    # crossing


    if (maze[pos_row])[pos_col] == ' ':
        print('Empty position:')
        break


    if ord((maze[pos_row])[pos_col]) >= ord('A') and ord((maze[pos_row])[pos_col]) <= ord('Z'):
        solution.append((maze[pos_row])[pos_col])


    if (maze[pos_row])[pos_col] == '+':
        # dir change

        # check upper
        if pos_dir != 'N' and pos_dir != 'S' and len(maze[pos_row-1]) > pos_col and (maze[pos_row-1])[pos_col] == '|':
            pos_dir = 'N'
        elif pos_dir != 'N' and pos_dir != 'S' and (maze[pos_row + 1])[pos_col] == '|':
            pos_dir = 'S'
        elif pos_dir != 'E' and pos_dir != 'W' and len(maze[pos_row]) > (pos_col+1) and (maze[pos_row])[pos_col+1] == '-':
            pos_dir = 'E'
        elif pos_dir != 'E' and pos_dir != 'W' and (maze[pos_row])[pos_col-1] == '-':
            pos_dir = 'W'
        else:
            print('cant direct bew direction')

    print('step: {} row: {} col:{} dir: {}'.format(i, pos_row, pos_col, pos_dir))

    steps += 1

print(''.join(solution))
print(steps)