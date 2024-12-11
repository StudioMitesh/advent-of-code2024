from collections import defaultdict, deque

with open('input10.txt', 'r') as file:
    tmap = [list(line.strip()) for line in file.readlines()]
trailheads = [point for point in [(x,y) for x in range(len(tmap)) for y in range(len(tmap[0])) if tmap[x][y] == '0']]

def find_trail(tmap: list[list[str]], trailhead: tuple[int,int]) -> tuple[set, dict]:
    paths: deque[(int,int)] = deque()
    paths.append(trailhead)
    starts = {}
    starts[trailhead] = None
    trailends = set()
    neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while paths:
        curr = paths.popleft() # gotta love breadth first search
        x, y = curr
        val = int(tmap[x][y])
        if val == 9:
            trailends.add(curr)
        for nb in neighbours:
            nx, ny = x + nb[0], y + nb[1]
            if (nx, ny) not in starts and 0 <= nx < len(tmap) and 0 <= ny < len(tmap[0]) and int(tmap[nx][ny]) == val + 1:
                paths.append((nx,ny))
                starts[(nx,ny)] = (x,y)
    return starts, trailends

# PART 1
scores1 = 0
for trailhead in trailheads:
    starts, trailends = find_trail(tmap, trailhead)
    scores1 += len(trailends)
print(scores1)


# PART 2

def find_trail2(tmap: list[list[str]], trailhead: tuple[int,int]) -> tuple[set, dict]:
    paths: deque[(int,int)] = deque()
    paths.append(trailhead)
    starts = defaultdict(set)
    starts[trailhead] = set()
    trailends = set()
    neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while paths:
        curr = paths.popleft()
        x, y = curr
        val = int(tmap[x][y])
        if val == 9:
            trailends.add(curr)
        for nb in neighbours:
            nx, ny = x + nb[0], y + nb[1]
            if 0 <= nx < len(tmap) and 0 <= ny < len(tmap[0]) and int(tmap[nx][ny]) == val + 1:
                if (nx,ny) not in starts:
                    paths.append((nx,ny))
                starts[(nx,ny)].add(curr)
    return starts, trailends

def pathing(trailends: set[tuple[int,int]], starts: dict[tuple[int,int], set[tuple[int,int]]], trailhead: tuple[int,int]) -> list[list[tuple[int,int]]]:
    paths = []
    def path_helper(curr: tuple[int,int], path: list[tuple[int,int]]) -> None:
        if curr == trailhead:
            path.append(trailhead)
            paths.append(path[::-1])
            return
        for predec in starts.get(curr, set()):
            path_helper(predec, path + [curr])
    for trailend in trailends:
        path_helper(trailend, [])
    return paths

scores2 = 0
for trailhead in trailheads:
    starts, trailends = find_trail2(tmap, trailhead)
    paths = pathing(trailends, starts, trailhead)
    scores2 += len(paths)
print(scores2)