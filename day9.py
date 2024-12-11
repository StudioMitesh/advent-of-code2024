inp = open('input9.txt', 'r').read()
disk = []
for i in range(len(inp)):
    num = int(inp[i])
    if i % 2 == 0:
        for j in range(num):
            disk.append(str(i//2))
    else:
        for j in range(num):
            disk.append(".")
disk2 = disk.copy()

# PART 1
l, r  = 0, len(disk) - 1
while l < r:
    while disk[l] != ".":
        l += 1
    while disk[r] == ".":
        r -= 1
    if l < r:
        disk[l], disk[r] = disk[r], disk[l]
def checked(d):
    checksum = 0
    for i in range(len(d)):
        if d[i] == ".":
            continue
        checksum += int(d[i]) * i
    return checksum
checksum1 = checked(disk)

# PART 2
nums = sorted(set(disk) - {"."}, reverse=True)
for n in nums:
    poses = [i for i in range(len(disk2)) if disk2[i] == n]
    if not poses:
        continue
    size = len(poses)
    moved = False
    for i in range(len(disk2) - size + 1):
        if i >= poses[0]:
            break
        if all(disk2[j] == "." for j in range(i, i + size)):
            for j in poses:
                disk2[j] = "."
            for j in range(i, i + size):
                disk2[j] = n
            moved = True
            break
    if not moved:
        continue
checksum2 = checked(disk2)

print(checksum1)
print(checksum2)