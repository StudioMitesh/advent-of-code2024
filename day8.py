with open('input8.txt', 'r') as file:
    mappy = [list(line.strip()) for line in file.readlines()]
antennas = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
antennalocs = {}
for i in range(len(mappy)):
    for j in range(len(mappy[0])):
        if mappy[i][j] in antennas:
            if mappy[i][j] not in antennalocs:
                antennalocs[mappy[i][j]] = []
            antennalocs[mappy[i][j]].append((i, j))
antinodes = set()
antinodes2 = set()
def anti2(ant1, ant2):
    x1, y1 = ant1
    x2, y2 = ant2
    dx = x2 - x1
    dy = y2 - y1
    x, y = x1, y1
    while 0 <= x < len(mappy) and 0 <= y < len(mappy[0]):
        x += dx
        y += dy
        if 0 <= x < len(mappy) and 0 <= y < len(mappy[0]):
            antinodes2.add((x, y))
    x, y = x2, y2
    while 0 <= x < len(mappy) and 0 <= y < len(mappy[0]):
        x -= dx
        y -= dy
        if 0 <= x < len(mappy) and 0 <= y < len(mappy[0]):
            antinodes2.add((x, y))

def anti1(ant1, ant2):
    x1, y1 = ant1
    x2, y2 = ant2
    dx = x2 - x1
    dy = y2 - y1
    anti1 = (x1 + 2 * dx, y1 + 2 * dy)
    anti2 = (x2 - 2 * dx, y2 - 2 * dy)
    if 0 <= anti1[0] < len(mappy) and 0 <= anti1[1] < len(mappy[0]):
        antinodes.add(anti1)
    if 0 <= anti2[0] < len(mappy) and 0 <= anti2[1] < len(mappy[0]):
        antinodes.add(anti2)

for ant, pos in antennalocs.items():
    for i in range(len(pos)):
        for j in range(i+1, len(pos)):
            anti1(pos[i], pos[j])
            anti2(pos[i], pos[j])
print(len(antinodes))
print(len(antinodes2))