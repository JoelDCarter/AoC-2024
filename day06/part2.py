import re

moves = {
    '^': (0, -1, '>'),
    'v': (0, 1, '<'),
    '<': (-1, 0, '^'),
    '>': (1, 0, 'v')
}
obstacles = []

with open('sample.txt', 'r', encoding='UTF-8') as file:
    rows = [line.rstrip() for line in file.readlines()]
    width = len(rows[0])
    height = len(rows)
    for j in range(height):
        guard = re.search('[\^v<>]', rows[j])
        if guard:
            obstacles.append((j, guard.start()))
            break
    for j in range(height):
        for i in range(width):
            if (j, i) in obstacles or rows[j][i] == '#':
                continue
            row, col = obstacles[0]
            direction = guard[0]
            visits = {}
            while True:
                col_delta, row_delta, direction_if_blocked = moves[direction]
                row += row_delta
                col += col_delta
                if row < 0 or row == height or col < 0 or col == width:
                    break
                if rows[row][col] == '#' or (row == j and col == i):
                    if visits.get((row, col)) is None:
                        visits[(row, col)] = 0
                    visits[(row, col)] += 1
                    if visits[(row, col)] == 4:
                        obstacles.append((j, i))
                        break
                    row -= row_delta
                    col -= col_delta
                    direction = direction_if_blocked
    print(len(obstacles) - 1)
