warehouseinp, motion = open('test.txt', 'r').read().strip().split('\n\n')
warehouse = [list(line.strip()) for line in warehouseinp.split('\n')]

startx, starty = None, None
for x in range(len(warehouse)):
    for y in range(len(warehouse[x])):
        if warehouse[x][y] == '@':
            startx, starty = x, y
            break
    if startx is not None:
        break

directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

walls = set()
for x in range(len(warehouse)):
    for y in range(len(warehouse[x])):
        if warehouse[x][y] == '#':
            walls.add((x, y))

boxes = set()
for x in range(len(warehouse)):
    for y in range(len(warehouse[x])):
        if warehouse[x][y] == 'O':
            boxes.add((x, y))

# PART 1
def move(x, y, dir):
    nx = x + directions[dir][0]
    ny = y + directions[dir][1]
    if 0 <= nx < len(warehouse) and 0 <= ny < len(warehouse[0]) and (nx, ny) not in walls:
        if (nx, ny) in boxes:
            box_locs = [(nx, ny)]
            bx, by = nx, ny
            while (bx + directions[dir][0], by + directions[dir][1]) in boxes:
                bx += directions[dir][0]
                by += directions[dir][1]
                box_locs.append((bx, by))
            bx += directions[dir][0]
            by += directions[dir][1]
            if 0 <= bx < len(warehouse) and 0 <= by < len(warehouse[0]) and (bx, by) not in walls and (bx, by) not in boxes:
                for bx, by in reversed(box_locs):
                    boxes.remove((bx, by))
                    boxes.add((bx + directions[dir][0], by + directions[dir][1]))
            else:
                return x, y
        return nx, ny
    return x, y
x = startx
y = starty
for m in motion:
    if m == '\n':
        continue
    x, y = move(x, y, m)
    print('moved to', x, y, 'in direction', m)
print(boxes)
gps = 0
for box in boxes:
    boxx = box[0]
    boxy = box[1]
    gps += (100*boxx + boxy)

print(gps)


# PART 2
def scaleup(warehouse):
    warehouse2 = []
    for row in warehouse:
        new_row = ""
        for char in row:
            if char == '#':
                new_row += "##"
            elif char == 'O':
                new_row += "[]"
            elif char == '.':
                new_row += ".."
            elif char == '@':
                new_row += "@."
        warehouse2.append(new_row)
    return warehouse2
warehouse2 = scaleup(warehouse)
for x in warehouse2:
    print(x)

startx2, starty2 = None, None
for x in range(len(warehouse2)):
    for y in range(len(warehouse2[x])):
        if warehouse2[x][y] == '@':
            startx2, starty2 = x, y
            break
    if startx2 is not None:
        break

def move2(x, y, dir):
    nx = x + directions[dir][0]
    ny = y + directions[dir][1]
    if 0 <= nx < len(warehouse2) and 0 <= ny < len(warehouse2[0]) and warehouse2[nx][ny] in '.@':
        if warehouse2[nx][ny] in '.[]':
            if warehouse2[nx][ny] in '[]':
                box_locs = [(nx, ny)]
                bx, by = nx, ny
                while warehouse2[bx][by] in '[]':
                    bx += directions[dir][0]
                    by += directions[dir][1]
                    box_locs.append((bx, by))
                bx = nx + directions[dir][0]
                by = ny + directions[dir][1]
                if 0 <= bx < len(warehouse2) and 0 <= by < len(warehouse2[0]) and warehouse2[bx][by] == '.':
                    warehouse2[nx] = warehouse2[nx][:ny] + '..' + warehouse2[nx][ny+2:]
                    warehouse2[bx] = warehouse2[bx][:by] + '[]' + warehouse2[bx][by+2:]
                else:
                    return x, y
            warehouse2[x] = warehouse2[x][:y] + '..' + warehouse2[x][y+2:]
            warehouse2[nx] = warehouse2[nx][:ny] + '@.' + warehouse2[nx][ny+2:]
            return nx, ny
    return x, y
        
x2, y2 = startx2, starty2
for m in motion:
    if m == '\n':
        continue
    x2, y2 = move2(x2, y2, m)
    print('moved to', x2, y2, 'in direction', m)

for x in warehouse2:
    print(x)

gps2 = 0
for i in range(len(warehouse2)):
    for j in range(len(warehouse2[0]) - 1):
        if warehouse2[i][j:j+2] == "[]":
            gps2 += (100*(i+1) + (j+1))
print(gps2)
