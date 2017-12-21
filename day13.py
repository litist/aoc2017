

file=open("day13.data",'r')

row = file.readlines()

firewall = []

fw_range = {}


for line in row:
    print(line.strip())

    (src, dst) = line.split(':')

    src = int(src.strip())
    dst = int(dst.strip())

    for i in range(len(firewall), src):
        firewall.append(0)

    #range.insert(src, dst)
    firewall.append(dst)

    fw_range[src] = [dst, 1, 0]

print(firewall)
print(fw_range)

severity = 0;

print('Starting Firewall run')
for w in range(96+2):

    # make step

    if w in fw_range:
        if fw_range[w][2] == 0:
            # we are caught
            print('fw caught us at {} {}'.format(w, fw_range[w]))
            severity += w*fw_range[w][0]



    # move scanner
    for a in fw_range:
        m = fw_range[a][0]
        i = fw_range[a][1]
        c = fw_range[a][2]

        #print('{}: {} {} {}'.format(a,m,c,i))

        c += i


        if c == (m-1):
            i = -1

        if c == 0:
            i = 1
        #print('{}: {} {} {}'.format(a,m,c,i))

        #fw_range[a] = (m, c, i)
        fw_range[a][1] = i
        fw_range[a][2] = c

    print(fw_range)

# 1298 wrong
# 1182 too small
print('Severity: {}'.format(severity))



def find_delay():
    severity = 0;
    mm = ''

    print('Find delay')

    fw_catch = {}
    # reset fw
    for a in fw_range:
        fw_range[a][1] = 1
        fw_range[a][2] = 0

    fw_catch = {}
    for a in range(98,-1, -1):
        print(a)
        fw_catch[a] = 1



    # check if we have a match at each position

    print(fw_catch)

    #while True:
    for bb in range(5000000):
        # make step



        # shift acculated errors on step forward and reset last position
        for a in range(98, 0, -1):
            fw_catch[a] = fw_catch[a - 1]
        fw_catch[0] = 0;

        # add current error to accumulated and shifted errors
        for a in range(97, -1, -1):
            if a in fw_range:
                if fw_range[a][2] == 0:
                    fw_catch[a] += 1;

#        print(fw_catch)

        # fw_catch[98]==0 -->
        # delay == 0 --> fw_catch[0] == 1 ... delay == 1 --> fw_catch[1] == 1 ... fw_catch[98] == 1 <--
        # delay == x --> fw_catch[0] == 0 ... delay == x+1 --> fw_catch[1] = fw_catch[x] && nohit


        if fw_catch[98] == 0:
            print('Found 0 error walk: {}'.format(bb))
            return


        s = '{}'.format(w)
        # move scanner
        for a in fw_range:
            m = fw_range[a][0]
            i = fw_range[a][1]
            c = fw_range[a][2]

            # print('{}: {} {} {}'.format(a,m,c,i))

            c += i

            if c == (m - 1):
                i = -1

            if c == 0:
                i = 1
            # print('{}: {} {} {}'.format(a,m,c,i))

            # fw_range[a] = (m, c, i)
            fw_range[a][1] = i
            fw_range[a][2] = c

            s = '{}.'.format(s)
        #print(s)

    else:
        print('Found no error free walk after {} delay'.format(bb))

    s = ''
    for i in range(98):
        if i in fw_range:
            s='{} {}'.format(s, fw_range[i])
    print(s)
    print('mm: {}'.format(mm))

    return severity


# 176702 too low
# 176802 too low
# 3870480 - 98 = 3870382 correct
find_delay()

exit()













def get_severity(delay):
    severity = 0;
    mm = ''

    # reset fw
    for a in fw_range:
        fw_range[a][1] = 1
        fw_range[a][2] = 0

    #print('Starting Firewall run')
    for w in range(delay):
        # move scanner
        for a in fw_range:
            m = fw_range[a][0]
            i = fw_range[a][1]
            c = fw_range[a][2]

            c += i

            if c == (m - 1):
                i = -1

            if c == 0:
                i = 1

            fw_range[a][1] = i
            fw_range[a][2] = c

    #print(fw_range)
    for w in range(0, 96 + 2):
        # make step
        if w in fw_range:
            mm = '{} {}'.format(mm, fw_range[w][2])
            if fw_range[w][2] == 0:
                # we are caught
                print('fw caught us at {} {}'.format(w, fw_range[w]))
                severity += w * fw_range[w][0]
                return 1

        s = '{}'.format(w)
        # move scanner
        for a in fw_range:
            m = fw_range[a][0]
            i = fw_range[a][1]
            c = fw_range[a][2]

            # print('{}: {} {} {}'.format(a,m,c,i))

            c += i

            if c == (m - 1):
                i = -1

            if c == 0:
                i = 1
            # print('{}: {} {} {}'.format(a,m,c,i))

            # fw_range[a] = (m, c, i)
            fw_range[a][1] = i
            fw_range[a][2] = c

            s = '{}.'.format(s)
        #print(s)

    s = ''
    for i in range(98):
        if i in fw_range:
            s='{} {}'.format(s, fw_range[i])
    print(s)
    print('mm: {}'.format(mm))

    return severity



for i in range(4000, 5000):
    print('\n\n')
    s = get_severity(i)
    print('Severity({}): {}'.format(i, s))

    if s==0:
        break
else:
    print('No successful way found')

