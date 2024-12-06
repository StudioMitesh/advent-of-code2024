import collections
inp = open('input5.txt', 'r').read()

# PART 1
splits, lists = inp.split('\n\n')
dct = collections.defaultdict(list)
revdct = collections.defaultdict(list)
for s in splits.split('\n'):
    x, y = s.split('|')
    x, y = int(x), int(y)
    dct[y].append(x)
    revdct[x].append(y)
sum = 0
sum2 = 0
nons = []
for l in lists.split('\n'):
    nums = list(map(int, l.split(',')))
    good = True
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i < j and y in dct[x]:
                good = False
                break
    if good:
        sum += nums[len(nums)//2]
    # PART 2
    else:
        # man why this gotta be kahn's algorithm come onnn
        goods = []
        indegree = {v: 0 for v in nums}
        for v in nums:
            for u in revdct[v]:
                if u in nums:
                    indegree[u] += 1
        bads = [v for v in nums if indegree[v] == 0]
        while bads:
            x = bads.pop()
            goods.append(x)
            for y in revdct[x]:
                if y in nums:
                    indegree[y] -= 1
                    if indegree[y] == 0:
                        bads.append(y)
        sum2 += goods[len(goods)//2] if goods else 0
print(sum)
print(sum2)
