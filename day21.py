


image = [['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']]

rules = {}

with open('day21.data') as file:
    for m in file.readlines():
        print(m)

        a, b = map(lambda x: ''.join(x.strip()), m.strip().split('=>'))

        rules[a] = b




print(image)

print(rules)


def printPattern(pattern):
    print(pattern)
    s = ''
    for row in pattern:
        s += ''.join(row)
        s += '\n'
    print(s)

def flipPattern(pattern, n = 0):

    if(n==0):
        return pattern

    N = len(pattern)

    res = []
    for col in range(N-1,-1,-1):
        res.append(pattern[col])

    return res

def rotate(pattern, n):

    if n <= 0:
        return pattern

    N = len(pattern)
    result = []
    for row in range(N):
        result.append([])
        for col in range(N):
            #print('{}x{} -> {}x{}'.format(row,col,N-row-1,row ))
            (result[row]).append( pattern[N-col-1][row] )

    return rotate(result, n -1)


def mat2pat(mat):

    t = []
    for r in mat:
        t.append(''.join(r))


    return '/'.join(t)


def enhance(mat):
    new_pat = None

    print('Enhance in: {}'.format(mat))

    for flip in range(2):
        for rot in range(4):
            a = mat2pat(rotate(flipPattern(mat, flip), rot))

            if a in rules:
                print('Found pattern wiht flip: {} rot: {}'.format(flip, rot))
                new_pat = a
                break

    if new_pat == None:
        print('Pattern not found inside our ruleset. need to check variations')
        return

    np = (rules[(new_pat)]).split('/')

    for r in np:
        r = list(r.strip())

    print('New pattern: {}'.format(np))
    return np



printPattern(image)

print('Starting segmentation')

for iter in range(18):

    if len(image) % 2 == 0:
        INPUT_PAT = 2
        OUTPUT_PAT = 3
    else:
        INPUT_PAT = 3
        OUTPUT_PAT = 4



    print('--------   {}-{} >>>>>>> {}-{}  --------------'.format(INPUT_PAT, INPUT_PAT, OUTPUT_PAT, OUTPUT_PAT))
    # build new grid
    grid2 = []
    for y in range(int(OUTPUT_PAT*len(image)/INPUT_PAT)):
        grid2.append([])
        for x in range(int(OUTPUT_PAT*len(image)/INPUT_PAT)):
            grid2[y].append('.')

    print('new grid {}'.format(grid2))

    # split into INxIN pattern
    for y in range(int((len(image)/INPUT_PAT))):
        for x in range(int(len(image)/INPUT_PAT)):
            print('sliced mat')
            print('split: y {} x {} '.format(y,x))

            tmp = []
            for y_ in range(INPUT_PAT):
                tmp.append([])
                for x_ in range(INPUT_PAT):
                    tmp[y_].append( image[y*INPUT_PAT + y_][x*INPUT_PAT + x_])

            printPattern(tmp)


            # check if this pattern is in our list
            print(mat2pat(tmp))

            np = enhance(tmp)

            for y_ in range(OUTPUT_PAT):
                for x_ in range(OUTPUT_PAT):
                    grid2[y*OUTPUT_PAT + y_][x*OUTPUT_PAT + x_] = np[y_][x_]

    print('np')
    printPattern(grid2)


    image = grid2


sum = 0
for r in image:
    for c in r:
        if c == '#':
            sum += 1

print('on_pixels after {} iterations:  {}'.format(iter, sum))