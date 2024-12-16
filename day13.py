import sympy as sp
import re

lines = open('input13.txt', 'r').read().strip()
pattern = r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)'
matches = re.findall(pattern, lines)
claws = []
claws2 = []
for match in matches:
    ax, ay, bx, by, px, py = map(int, match)
    claws.append(((ax, ay), (bx, by), (px, py)))
    claws2.append(((ax, ay), (bx, by), (px+10000000000000, py+10000000000000)))

ACOST = 3
BCOST = 1
def cost(claw):
    (ax, ay), (bx, by), (px, py) = claw
    a, b = sp.symbols("a b", integer=True)
    eq1 = a*ax + b*bx - px
    eq2 = a*ay + b*by - py
    try:
        listsols = []
        sol = sp.solve([eq1, eq2], (a, b))
        if sol:
            if isinstance(sol, dict):
                sol = [sol]
            for s in sol:
                listsols.append((s[a], s[b]))
    except:
        print('no solution')
    if listsols:
        cost = min(ACOST*a + BCOST*b for (a,b) in listsols)
    else:
        cost = 0
    return cost

cost1 = 0
for claw in claws:
    cost1 += cost(claw)

cost2 = 0
for claw in claws2:
    cost2 += cost(claw)

print(cost1)
print(cost2)