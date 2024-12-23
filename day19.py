towels, stacks = open('input19.txt').read().strip().split('\n\n')

towels = [str(t) for t in towels.split(', ')]
stacks = [str(s) for s in stacks.split('\n')]

max_towel = max([len(t) for t in towels])

from functools import lru_cache
@lru_cache(None)
def check(stack):
    if not stack:
        return 1
    for t in towels:
        if stack.startswith(t):
            if check(stack[len(t):]):
                return 1
    return 0
    

total = 0
for s in stacks:
    total += check(s)
print(total)