import re

with open('input.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
sum = 0
enabled = True
for line in lines:
    for instruction in re.finditer(r'mul\((\d+),(\d+)\)|(do|don\'t)\(\)', line):
        if instruction.group(3) == 'do':
            enabled = True
        elif instruction.group(3) == 'don\'t':
            enabled = False
        elif enabled:
            sum += int(instruction.group(1)) * int(instruction.group(2))
print(sum)