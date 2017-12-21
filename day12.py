


def rec_find_group(key, list):
    print('check {} in list {}'.format(key ,list))
    if key in list:
        return

    # add to list
    list[key] = key

    for k in pipes[key]:
        rec_find_group(k, list)


file=open("day12.data",'r')

row = file.readlines()

pipes = {}

for line in row:
    print(line)

    (src, dst) = line.split('<->')

    src = src.strip()

    print('{} ---- {}'.format(src, dst))

    if src not in pipes:
        pipes[src] = []

    for dest in dst.split(','):
        print('{} '.format(dest.strip()))

        pipes[src].append(dest.strip())


print(pipes)



group = {}

rec_find_group('0', group)

print(group)


print('Entries in group for 0: {}'.format(len(group)))


reduce_pipes = {}

for k in pipes:
    reduce_pipes[k] = k


print(reduce_pipes)

n_groups = 0
while(len(reduce_pipes)):
    group = {}
    k = list(reduce_pipes.keys())[0]


    rec_find_group(k, group)


    print('Entries in group for {}: {} [{}]'.format(k, len(group), group))

    # remove from list
    for l in group:
        reduce_pipes.pop(l)

    n_groups += 1


print('Found {} closed groups.'.format(n_groups))