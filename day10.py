

def knot_hash(input_string):

    input = [3,4,1,5]
    input = [157,222,1,2,177,254,0,228,159,140,249,187,255,51,76,30]

    #print('knot_hash({})'.format(input_string))

    input = []
    for c in input_string:
        input.append(ord(c))


    input.extend((17, 31, 73, 47, 23))



    N = 256;
    N_rounds = 64;


    L = list(range(N))

    cur_pos = 0;
    skip = 0;


    for nr in range(N_rounds):
        for il in input:

            tl = []

            # reverse input length
            for tlc in range(il):
                tl.insert(0, L[(cur_pos + tlc) % len(L)])

            # insert reversed list
            for tlc in range(il):
                L[(cur_pos + tlc) % len(L)] = tl[tlc]

            # move current pos by length and skip
            cur_pos = (cur_pos + il + skip) % len(L)
            skip += 1



    #print('Result P1: {}'.format(L[0]*L[1]))


    # make xor hash
    hex_hash = ''
    for a in range(16):
        res = 0
        for b in range(16):
            res = res ^ L[a*16 + b]

        hex_hash += '{:02x}'.format(res)

    #print('Knot hash: {}'.format(hex_hash))

    return hex_hash

if __name__=='__main__':
    print(knot_hash('157,222,1,2,177,254,0,228,159,140,249,187,255,51,76,30'))
    print(knot_hash(''))