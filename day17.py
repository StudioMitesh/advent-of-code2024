inp = open('input17.txt').read().strip().split('\n\n')
registers = inp[0].split('\n')
program = list(inp[1].split(' ')[1])
a = int(registers[0].split(' ')[2])
b = 0
c = 0
prog = [p for p in program if p != ',']

def combo(op):
    if op == 0 or op == 1 or op == 2 or op == 3:
        return op
    elif op == 4:
        return a
    elif op == 5:
        return b
    elif op == 6:
        return c
    else:
        return 0

point = 0
out = ""
while point < len(prog):
    p = int(prog[point])
    op = int(prog[point + 1])
    if p == 0 or p == 6 or p == 7:
        res = a // pow(2, combo(op))
        if p == 0: a = res
        elif p == 6: b = res
        else: c = res
    if p == 1:
        b = b ^ op
    elif p == 2:
        b = combo(op) % 8
    elif p == 3: 
        if a != 0:
            point = combo(op)
            continue
    elif p == 4:
        b = b ^ c
    elif p == 5:
        out += (str(combo(op) % 8) + ',')
    point += 2
    print("completed point: ", point, "a, b, c are ", a, b, c)

print(out)



