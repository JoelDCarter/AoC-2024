import re

def count_occurrences(list, pattern):
    count = 0
    for text in list:
        count += len(re.findall(f"(?=({pattern}))", text))
    return count

def build_diagonals(i, j, diagonalLtoR, diagonalRtoL):
    for k in range(size):
        line = ''.join([rows[j + k][i + k] for k in range(size - max(i, j))])
        if len(line) > 3: diagonalLtoR[f"{i},{j}"] = line
        line = ''.join([rows[j + k][width - i - 1 - k] for k in range(size - max(i, j))])
        if len(line) > 3: diagonalRtoL[f"{i},{j}"] = line

with open('input.txt', 'r', encoding='UTF-8') as file:
    rows = [line.rstrip() for line in file.readlines()]
    width = len(rows[0])
    height = len(rows)
    size = min(width, height)
    cols = [''.join([rows[j][i] for j in range(height)]) for i in range(width)]
    diagonalLtoR = {}
    diagonalRtoL = {}
    for i in range(width):
        build_diagonals(i, 0, diagonalLtoR, diagonalRtoL)
    for j in range(1, height):
        build_diagonals(0, j, diagonalLtoR, diagonalRtoL)
    pattern = 'XMAS|SAMX'
    total_count = count_occurrences(rows, pattern) + count_occurrences(cols, pattern) + count_occurrences(diagonalLtoR.values(), pattern) + count_occurrences(diagonalRtoL.values(), pattern)
    print(total_count)