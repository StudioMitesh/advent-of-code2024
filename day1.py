# PART 1
inp = open('input1.txt', 'r').read().split('\n')
l1 = []
l2 = []
for x in inp:
    ints = x.split('  ')
    l1.append(int(ints[0]))
    l2.append(int(ints[1]))
l1og = l1.copy()
l2og = l2.copy()
l1.sort()
l2.sort()
sum = 0
for i in range(len(l1)):
    sum += abs(l1[i] - l2[i])
print(sum)

# PART 2
l2dict = {}
for x in l2og:
    if x not in l2dict:
        l2dict[x] = 1
    else:
        l2dict[x] += 1
sum2 = 0
for y in l1og:
    if y in l2dict:
        sum2 += y * l2dict[y]
print(sum2)
