from collections import deque, defaultdict

with open('input20.txt', 'r') as file:
    maze = [list(line.strip()) for line in file.readlines()]

startx, starty = 0, 0
endx, endy = 0, 0
for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x] == 'S':
            startx, starty = x, y
            break
        if maze[y][x] == 'E':
            endx, endy = x, y
            break


def find_path(maze, startx, starty, endx, endy):
    queue = deque([(startx, starty, 0, False, [])])
    visited = set()
    normal_steps = float('inf')
    cheats = []
    while queue:
        x, y, steps, cheat, path = queue.popleft()
        if (x, y, cheat) in visited:
            continue
        visited.add((x, y, cheat))
        if x == endx and y == endy:
            if not cheat:
                normal_steps = min(normal_steps, steps)
            else:
                cs, ce = path[0], (x,y)
                cheats.append((cs, ce, normal_steps - steps))
            continue
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze):
                if maze[ny][nx] != "#":
                    queue.append((nx, ny, steps + 1, cheat, path))
                elif not cheat:
                    for cdx, cdy in [(dx, dy), (dx*2, dy*2)]:
                        cx, cy = x + cdx, y + cdy
                        if (0 <= cx < len(maze[0]) and 0 <= cy < len(maze) and maze[cy][cx] != '#' and maze[y+dy][x+dx] == '#'):
                            queue.append((cx, cy, steps + 1, True, path + [(x, y)]))
    return cheats

cheats = find_path(maze, startx, starty, endx, endy)

savings = defaultdict(int)
for cs, ce, steps in cheats:
    savings[steps] += 1

hunnidplus = sum(count for save, count in savings.items() if save >= 100)
print(hunnidplus)
print(savings)