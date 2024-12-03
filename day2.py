reports = open("input2.txt", "r").read().split("\n")

def checker(levels):
    go = True
    inc = (levels == sorted(levels)) or (levels == sorted(levels, reverse=True))
    for j in range(len(levels)-1):
        diff = abs(levels[j+1] - levels[j])
        if diff < 1 or diff > 3:
            go = False
            break
    return go and inc

# PART 1
safe = 0
for levels in reports:
    levels = levels.split(" ")
    for i in range(len(levels)):
        levels[i] = int(levels[i])
    if checker(levels):
        safe += 1
print(safe)

# PART 2
safe2 = 0
for levels in reports:
    levels = levels.split(" ")
    for i in range(len(levels)):
        levels[i] = int(levels[i])
    ok = False
    if checker(levels):
        safe2 += 1
        continue
    for k in range(len(levels)):
        level = levels[:k] + levels[k+1:]
        if checker(level):
            ok = True
    if ok:
        safe2 += 1
print(safe2)
