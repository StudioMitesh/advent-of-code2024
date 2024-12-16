from collections import deque

with open('input12.txt', 'r') as file:
    garden = [list(line.strip()) for line in file.readlines()]
directions = [(0,1), (0,-1), (1,0), (-1,0)]

def regionbfs(garden: list[list[str]], x: int, y: int, visited: set) -> tuple[int,int,set,str]:
    plant = garden[x][y]
    queue = deque([(x,y)])
    visited.add((x,y))
    area = 0
    perimeter = 0 
    pers = {dir: set() for dir in directions}
    while queue:
        curr = queue.popleft()
        x, y = curr
        area += 1
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if 0 <= nx < len(garden) and 0 <= ny < len(garden[0]) and garden[nx][ny] == plant:
                if (nx,ny) not in visited:
                    queue.append((nx,ny))
                    visited.add((nx,ny))
            else:
                perimeter += 1
                pers[(dx,dy)].add((x,y))
    return area, perimeter, pers, plant


visited = set()
price = 0
for x in range(len(garden)):
    for y in range(len(garden[0])):
        if (x,y) not in visited:
            area, perimeter, pers, plant = regionbfs(garden, x, y, visited)
            print(area, perimeter, plant)
            price += area * perimeter
print(price)

print('Part 2 --------------------------------------------')
def dirbfs2(pers: set) -> int:
    fences = 0
    for fence in pers.values():
        visited = set()
        for p in fence:
            if p not in visited:
                fences += 1
                queue = deque([p])
                while queue:
                    curr = queue.popleft()
                    if curr in visited:
                        continue
                    visited.add(curr)
                    x, y = curr
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if (nx, ny) in fence:
                            queue.append((nx, ny))
    
    return fences



price2 = 0
visited2 = set()
for x in range(len(garden)):
    for y in range(len(garden[0])):
        if (x,y) not in visited2:
            area, perimeter, pers, plant = regionbfs(garden, x, y, visited2)
            fences = dirbfs2(pers)
            print(area, fences, plant)
            price2 += area * fences
print(price2)