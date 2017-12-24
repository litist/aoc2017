
pieces = []

# load instructions
with open('day24.data') as file:
    for p in file.readlines():
        pieces.append(p.strip())





def getMaxBLen(set, end_number, strength, length):

    if len(set) == 0:
        return (strength, length)

    candidates = {}
    candidates_str = {}

    #print('getMaxBLen({}, {}, {}, {})'.format(set, end_number, strength, length))
    for i in set:
        a,b = map(lambda x: int(x), i.split('/'))

        if a == end_number:
            tmp = (set[:])
            tmp.remove(i)
            candidates[i], candidates_str[i] = getMaxBLen( tmp, b, strength + a + b, length + 1 )

        if b == end_number:
            tmp = (set[:])
            tmp.remove(i)
            candidates[i], candidates_str[i] = getMaxBLen( tmp, a, strength + a + b, length + 1 )

    #print(candidates)
    mlen = strength
    mstr = length
    for i in candidates:
        #print('clen {} {}'.format(candidates[i], candidates_str[i]))
        if candidates_str[i] == mstr and candidates[i] > mlen:
            mlen = candidates[i]
            mstr = candidates_str[i]

        if candidates_str[i] > mstr:
            mlen = candidates[i]
            mstr = candidates_str[i]


    return (mlen, mstr)


print('max: {}'.format(getMaxBLen(pieces, 0, 0, 0)))