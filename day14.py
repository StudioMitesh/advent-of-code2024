import re
from collections import defaultdict

lines = open('input14.txt', 'r').read().strip()
pattern = r'p=([+-]?\d+),([+-]?\d+) v=([+-]?\d+),([+-]?\d+)'
robots = []
robots2 = []
matches = re.findall(pattern, lines)
for match in matches:
    px, py, vx, vy = map(int, match)
    robots.append({'p': (px, py), 'v': (vx, vy)})

robots2 = robots.copy()
def simulate(robots, seconds=100, width=101, height=103):
    for robot in robots:
        px, py = robot['p']
        vx, vy = robot['v']
        robot['p'] = ((px + seconds*vx) % width, (py + seconds*vy) % height)

simulate(robots)

positions = defaultdict(int)
for robot in robots:
    positions[robot['p']] += 1

def quadrants(positions, width=101, height=103):
    midx = width // 2
    midy = height // 2
    quadrants = [0,0,0,0]
    for (x,y), count in positions.items():
        if x == midx or y == midy:
            continue
        if x < midx and y < midy:
            quadrants[0] += count
        elif x >= midx and y < midy:
            quadrants[1] += count
        elif x < midx and y >= midy:
            quadrants[2] += count
        else:
            quadrants[3] += count
    sf = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
    return sf

safetyfactor = quadrants(positions)
print(safetyfactor)

# PART 2
def contiguity(cols, min_robs=10):
    cols.sort()
    count = 1
    for i in range(1, len(cols)):
        if cols[i] == cols[i - 1] + 1:
            count += 1
            if count >= min_robs:
                return True
        else:
            count = 1
    return False


def christmas(robots2, width=101, height=103):
    MIN_ROBS = 10
    MAX_ITER = 100000
    for i in range(MAX_ITER):
        simulate(robots2, seconds=1, width=width, height=height)
        psns = defaultdict(list)
        for robot in robots2:
            x, y = robot['p']
            psns[y].append(x)
        for y, cols in psns.items():
            if contiguity(cols, min_robs=MIN_ROBS):
                return i
            
def draw(robots2, width=101, height=103):
    grid = [['.' for _ in range(width)] for _ in range(height)]
    for robot in robots2:
        x, y = robot['p']
        grid[y][x] = '#'
    for row in grid:
        print(''.join(row))

christmas_time = christmas(robots2)
draw(robots2)
print(christmas_time)
        