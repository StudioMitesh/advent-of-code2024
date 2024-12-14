stones = open('input11.txt').read().strip()
stones = stones.split(' ')
stones = [int(x) for x in stones]
ogstones = stones.copy()
print(stones)



# PART 1
for _ in range(25):
    s = 0
    while s < len(stones):
        match stones[s]:
            case 0:
                stones[s] = 1
            case x if len(str(stones[s])) % 2 == 0:
                strx = str(stones[s])
                left = int(strx[:len(strx)//2])
                right = int(strx[len(strx)//2:])
                stones[s:s+1] = [left, right]
                s += 1
            case _:
                stones[s] *= 2024
        s += 1
print(len(stones))

# PART 2
def blink2(stone):
    match stone:
        case 0:
            return [1]
        case x if len(str(x)) % 2 == 0:
            strx = str(stone)
            left = int(strx[:len(strx)//2])
            right = int(strx[len(strx)//2:])
            return [left, right]
        case _:
            return [stone * 2024]

from functools import lru_cache
@lru_cache(maxsize=None)
def recurse(stone, blinks):
    if blinks == 0:
        return 1
    count = 0
    stones_new = blink2(stone)
    for s in stones_new:
        count += recurse(s, blinks-1)
    return count

total = 0
for s in ogstones:
    total += recurse(s, 75)
    print(f"recursed {s} to {total}")
print(total)