with open('input6.txt', 'r') as file:
    damap = [list(line.strip()) for line in file.readlines()]

# PART 1
startx, starty = None, None
for x in range(len(damap)):
    for y in range(len(damap[x])):
        if damap[x][y] == '^':
            startx, starty = x, y
            break
    if startx is not None:
        break
dir = 0 # 0 for up, 1 for right, 2 for down, 3 for left
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
x, y = startx, starty
visited = set()
visited.add((x, y))
print(damap[startx][starty])
while 0 <= x < len(damap) and 0 <= y < len(damap[0]):
    new_x = x + dx[dir]
    new_y = y + dy[dir]
    if new_x < 0 or new_x >= len(damap) or new_y < 0 or new_y >= len(damap[0]):
        break
    if damap[new_x][new_y] == '#':
        dir = (dir + 1) % 4
    else:
        x, y = new_x, new_y
        visited.add((x, y))

print(len(visited))

# PART 2
def path(blockx, blocky):
    map2 = [row.copy() for row in damap]
    map2[blockx][blocky] = '#'
    dir = 0
    visited2 = set()
    visited2.add((startx, starty, dir))
    x, y = startx, starty
    while True:
        new_x = x + dx[dir]
        new_y = y + dy[dir]
        if new_x < 0 or new_x >= len(map2) or new_y < 0 or new_y >= len(map2[0]):
            return False
        if map2[new_x][new_y] == '#':
            dir = (dir + 1) % 4
        else:
            x, y = new_x, new_y
            if (new_x, new_y, dir) in visited2:
                return True
            visited2.add((new_x, new_y, dir))

positions = 0
for x in range(len(damap)):
    for y in range(len(damap[x])):
        if (x, y) == (startx, starty):
            continue
        if damap[x][y] == '#':
            continue
        if path(x, y):
            positions += 1
        print(f"Just checked {x}, {y}, num positions is {positions}")

print(positions)
