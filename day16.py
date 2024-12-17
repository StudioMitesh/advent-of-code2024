import heapq

with open('test.txt', 'r') as file:
    maze = [list(line.strip()) for line in file.readlines()]

startx, starty = None, None
endx, endy = None, None
for x in range(len(maze)):
    for y in range(len(maze[0])):
        if maze[x][y] == 'S':
            startx, starty = x, y
        elif maze[x][y] == 'E':
            endx, endy = x, y

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

pq = []
heapq.heappush(pq, (0, startx, starty, 0)) # cost, x, y, direction
visited = set()
came_from = {}

# dijkstra
while pq:
    cost, x, y, dir = heapq.heappop(pq)
    if (x,y) == (endx, endy):
        print(cost) # PART 1
        break
    if (x,y,dir) in visited:
        continue
    visited.add((x,y,dir))
    dx, dy = directions[dir]
    nx, ny = x + dx, y + dy
    if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != '#':
        if (nx, ny) not in came_from:
            came_from[(nx, ny)] = (x, y)
        heapq.heappush(pq, (cost + 1, nx, ny, dir))
    if (x, y, (dir + 1) % 4) not in visited:
        if (x, y) not in came_from:
            came_from[(x, y)] = (x, y)
        heapq.heappush(pq, (cost + 1000, x, y, (dir + 1) % 4))
    if (x, y, (dir - 1) % 4) not in visited:
        if (x, y) not in came_from:
            came_from[(x, y)] = (x, y)   
        heapq.heappush(pq, (cost + 1000, x, y, (dir - 1) % 4))

# PART 2
tiles = set()
curr = (endx, endy)
while curr != (startx, starty):
    tiles.add(curr)
    curr = came_from.get(curr, None)
    if curr is None:
        break
tiles.add((startx, starty))

for x in range(len(maze)):
    for y in range(len(maze[0])):
        if (x, y) in tiles and maze[x][y] != '#':
            maze[x][y] = 'O'
for x in maze:
    print(''.join(x))

print(len(tiles))