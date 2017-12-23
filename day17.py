
spinlock = [0]

cur_pos = 0;

N = 2017;

steps = 354

for i in range(1,N+1):

    cur_pos = ((cur_pos + steps) % len(spinlock)) + 1

    spinlock.insert(cur_pos, i)


print(spinlock)
print(spinlock[cur_pos-3:cur_pos+3])



# part 2
# actually the 0 will always stay at positon 0, so we need to track the value in position 1
zero_plus_value = -1
cur_pos = 0;
spinlock_len = 1;

N = 50000000

for i in range(1,N+1):

    cur_pos = ((cur_pos + steps) % spinlock_len) + 1

    if cur_pos == 1:
        # new value after 0
        zero_plus_value = i

    spinlock_len += 1

print('Value after 0: {}'.format(zero_plus_value))