import re

with open('input.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
sum = 0
for line in lines:
    for instruction in re.finditer(r'mul\((\d+),(\d+)\)', line):
        sum += int(instruction.group(1)) * int(instruction.group(2))
print(sum)