from itertools import product

lines = open('input7.txt', 'r').read().split('\n')

def numbertime(line):
    target, nums = line.split(': ')
    target = int(target)
    nums = nums.split(' ')
    results = set()
    operators = ['+', '*', '||']
    combos = list(product(operators, repeat=len(nums) - 1))
    for op in combos:
        curr = int(nums[0])
        for i, o in enumerate(op):
            if o == '+':
                curr += int(nums[i + 1])
            elif o == '*':
                curr *= int(nums[i + 1])
            elif o == '||':
                curr = int(str(curr) + str(nums[i + 1]))
        results.add(curr)
    if target in results:
        return target
    else:
        return 0
sum = 0
for line in lines:
    sum += numbertime(line)
print(sum)