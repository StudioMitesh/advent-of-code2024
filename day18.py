data = open('input18.txt').read().strip().split('\n')
space = [['.' for _ in range(71)] for _ in range(71)]
for i in range(1024):
    line = data[i]
    x, y = line.split(',')
    print(x, y)
    space[int(y)][int(x)] = '#'



# bfs flood fill
from collections import deque
def bfspath(space, start, end):
    queue = deque([start])
    visited = set()
    visited.add(start)
    came_from = {}
    while queue:
        curr = queue.popleft()
        y, x = curr
        print(curr)
        if curr == end:
            print("found path")
            path = []
            while curr != start:
                path.append(curr)
                curr = came_from[curr]
            return path[::-1]
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= ny < len(space) and 0 <= nx < len(space[0]) and (ny,nx) not in visited and space[ny][nx] == '.':
                queue.append((ny,nx))
                visited.add((ny,nx))
                came_from[(ny,nx)] = curr
                print("added to queue", (ny,nx))
    return None

path = bfspath(space, (0,0), (70,70))
print(path)
if path:
    for y, x in path:
        space[y][x] = 'O'

for row in space:
    print(''.join(row))
print(len(path) if path else "No path")