
max_manhattan_a = 0
max_a = None
max_id = -1

min_manhattan_a = 1000000
min_a = None
min_id = -1

particle_id = 0;


particles = {}


with open('day20.data') as file:
    for m in file.readlines():
        #print(m.split(', '))

        p, v, a = m.split(', ')

        p = list(map(lambda x:int(x), p.strip()[3:-1].split(',')))
        v = list(map(lambda x:int(x), v.strip()[3:-1].split(',')))
        a = list(map(lambda x:int(x), a.strip()[3:-1].split(',')))


        # add to list
        particles[particle_id] = [p, v, a]


        #print(p)
        #print(v)
        #print(a)



        a_tmp = sum(list(map(lambda x:abs(int(x)), a)))
        if a_tmp > max_manhattan_a:
            max_manhattan_a = a_tmp
            max_a = a
            print('id: {} max_a {} -> {}'.format(particle_id, max_a, a_tmp))

        if a_tmp <= min_manhattan_a:
            min_manhattan_a = a_tmp
            min_a = a
            min_id = particle_id
            print('id: {} min_a {} -> {}'.format(particle_id, min_a, a_tmp))

        particle_id += 1


print(max_manhattan_a)
print(max_a)

print(min_manhattan_a)
print(min_a)

print('id: {} min_a {} -> {}'.format(min_id, min_a, min_a))


print(particles)






for i in range(100):

    for part in particles:
        p, v, a = particles[part]

        #print('p: {} v: {} a:{}'.format(p,v,a))

        # update velocity
        v = list(map(lambda x, y: x + y, v, a))
        particles[part][1] = v

        # update position
        p = list(map(lambda x, y: x + y, p, v))
        particles[part][0] = p


    removes = {}
    # remove collisions
    for part in particles:
        for part2 in particles:

            if part == part2:
                continue

            if 0 == sum(list(map(lambda x, y: abs(x - y), particles[part][0], particles[part2][0]))):
                removes[part] = 1
                removes[part2] = 1

    print('Items to be removed:')
    for r in removes:
        p, v, a = particles[r]

        print('id: p: {} v: {} a:{}'.format(r, p,v,a))

        particles.pop(r)

    print('#particles: {}'.format(len(particles)))


    # print
    for part in particles:
        p, v, a = particles[part]

        #print('p: {} v: {} a:{}'.format(p,v,a))




