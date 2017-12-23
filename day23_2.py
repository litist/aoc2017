




n_mul = 0

a = 1
h = 0

#set b 65
b = 65
#set c b
c = b

#jnz a 2
if a != 0:
    #mul b 100
    b = b * 100
    #sub b -100000
    b -= -100000
    #set c b
    c = b
    #sub c -17000
    c -= -17000


# this is my fast implementation
for i in range(b,c+1,17):
    print('Looking for divided of {}'.format(i))

    for f in range(2, b):
        t = i/f
        if round(t) == t:
            print('Found first divider {} * {} = {}'.format(f, t, i))
            h += 1
            break

print('Found {} none primes in range {} {}'.format(h, b, c))
print('#############################')
exit()

while True:
    #set f 1
    f = 1
    #set d 106498 2
    d = 2

    print('Looking for divided of {}'.format(b))

    while True:
        #set e 2
        e = 2
        while True:
            #set g d
            g = d

            #mul g e
            g = g * e
            n_mul += 1
            #sub g b
            g -= b

            #jnz g 2
            if g == 0:
                if f==1:
                    print('Found first divider {} * {} = {}'.format(d,e,b))
                # d*e = b
                #set f 0
                f = 0
            #sub e -1
            e -= -1
            #set g e
            g = e
            #sub g b
            g -= b
            #jnz g -8
            if g == 0:
                break
        #sub d -1
        d -= -1
        #set g d
        g = d
        #sub g b
        g -= b

        #print('a:{} b:{} c:{} d:{} e:{} f:{} g:{} h:{}'.format(a,b,c,d,e,f,g,h))

        #jnz g -13
        # d == b
        if g == 0:
            break


    print('Finished checking {} and f is {}'.format(b, f))

    #jnz f 2
    if f == 0:
        #sub h -1
        h -= -1
    #set g b
    g = b
    #sub g c
    g -= c

    #jnz g 2
    # b == c
    if g == 0:
        #jnz 1 3
        # here we can finish
        print('Finished program')
        break

    #sub b -17
    b -= -17
    #jnz 1 -23

print(h)