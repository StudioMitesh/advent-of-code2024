inp = open('input4.txt', 'r').read()


# PART 1
rows = inp.split('\n')
sum = 0
grid = []
for row in rows:
    grid.append(list(row))
# horizontal checks
for i in range(len(grid)):
    for j in range(len(grid[i])-3):
        if ''.join(grid[i][j:j+4]) == 'XMAS' or ''.join(grid[i][j:j+4]) == 'SAMX':
            sum += 1
# vertical checks
for i in range(len(grid)-3):
    for j in range(len(grid[i])):
        if ''.join([grid[i][j], grid[i+1][j], grid[i+2][j], grid[i+3][j]]) == 'XMAS' or ''.join([grid[i][j], grid[i+1][j], grid[i+2][j], grid[i+3][j]]) == 'SAMX':
            sum += 1
# diagonal checks top left to bottom right
for i in range(len(grid)-3):
    for j in range(len(grid[i])-3):
        if (grid[i][j] == 'X' and grid[i+1][j+1] == 'M' and grid[i+2][j+2] == 'A' and grid[i+3][j+3] == 'S') or (grid[i][j] == 'S' and grid[i+1][j+1] == 'A' and grid[i+2][j+2] == 'M' and grid[i+3][j+3] == 'X'):
            sum += 1
# diagonal checks bottom left to top right
for i in range(3, len(grid)):
    for j in range(len(grid[i])-3):
        if (grid[i][j] == 'X' and grid[i-1][j+1] == 'M' and grid[i-2][j+2] == 'A' and grid[i-3][j+3] == 'S') or (grid[i][j] == 'S' and grid[i-1][j+1] == 'A' and grid[i-2][j+2] == 'M' and grid[i-3][j+3] == 'X'):
            sum += 1
print(sum)

# PART 2
sum2 = 0
for i in range(len(grid)-2):
    for j in range(len(grid[i])-2):
        if grid[i][j] == 'M' and grid[i+1][j+1] == 'A' and grid[i+2][j+2] == 'S':
            if grid[i+2][j] == 'S' and grid[i+1][j+1] == 'A' and grid[i][j+2] == 'M' or grid[i+2][j] == 'M' and grid[i+1][j+1] == 'A' and grid[i][j+2] == 'S':
                sum2 += 1
        elif grid[i][j] == 'S' and grid[i+1][j+1] == 'A' and grid[i+2][j+2] == 'M':
            if grid[i+2][j] == 'S' and grid[i+1][j+1] == 'A' and grid[i][j+2] == 'M' or grid[i+2][j] == 'M' and grid[i+1][j+1] == 'A' and grid[i][j+2] == 'S':
                sum2 += 1
print(sum2)
