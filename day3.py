inp = open('input3.txt', 'r').read()

# PART 1
sum = 0
digits = '0123456789'
i = 0
while i < len(inp):
    if inp[i:i+4] == 'mul(':
        i += 4
        x = 0
        y = 0
        while i < len(inp) and inp[i] in digits:
            x = x * 10 + int(inp[i])
            i += 1
        if i < len(inp) and inp[i] == ',':
            i += 1
        while i < len(inp) and inp[i] in digits:
            y = y * 10 + int(inp[i])
            i += 1
        if i < len(inp) and inp[i] == ')':
            i += 1
            sum += x * y
    else:
        i += 1
print(sum)

# PART 2
sum2 = 0
j = 0
do = True
while j < len(inp):
    if inp[j:j+7] == "don't()":
        do = False
        j += 7
    elif inp[j:j+4] == 'do()':
        do = True
        j += 4
    elif inp[j:j+4] == 'mul(':
        if do:
            j += 4
            x = 0
            y = 0
            while j < len(inp) and inp[j] in digits:
                x = x * 10 + int(inp[j])
                j += 1
            if j < len(inp) and inp[j] == ',':
                j+= 1
            while j < len(inp) and inp[j] in digits:
                y = y * 10 + int(inp[j])
                j += 1
            if j < len(inp) and inp[j] == ')':
                j += 1
                sum2 += x * y
        else:
            j += 4
    else:
        j += 1
print(sum2)