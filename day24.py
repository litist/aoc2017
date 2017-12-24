
pieces = []


# load instructions
with open('day24.data') as file:
    for p in file.readlines():
        print(p)
        pieces.append(p.strip())





def getMaxBLen(set, end_number, strength):

    if len(set) == 0:
        return strength

    candidates = {}

    print('getMaxBLen({}, {}, {})'.format(set, end_number, strength))
    for i in set:
        a,b = map(lambda x: int(x), i.split('/'))

        if a == end_number:
            tmp = (set[:])
            tmp.remove(i)
            candidates[i] = getMaxBLen( tmp, b, strength + a + b )

        if b == end_number:
            tmp = (set[:])
            tmp.remove(i)
            candidates[i] = getMaxBLen( tmp, a, strength + a + b )

    print(candidates)
    mlen = strength
    for i in candidates:
        print('clen {}'.format(candidates[i]))
        if candidates[i] > mlen:
            mlen = candidates[i]
    print()

    return mlen


print('max: {}'.format(getMaxBLen(pieces, 0, 0)))