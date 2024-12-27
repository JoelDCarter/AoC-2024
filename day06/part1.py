import re

moves = {
    '^': (0, -1, '>'),
    'v': (0, 1, '<'),
    '<': (-1, 0, '^'),
    '>': (1, 0, 'v')
}

with open('sample.txt', 'r', encoding='UTF-8') as file:
    rows = [line.rstrip() for line in file.readlines()]
    width = len(rows[0])
    height = len(rows)
    for j in range(height):
        guard = re.search('[\^v<>]', rows[j])
        if guard:
            row = j
            col = guard.start()
            direction = guard[0]
            break
    while True:
        rows[row] = rows[row][:col] + 'X' + rows[row][col + 1:]
        col_delta, row_delta, direction_if_blocked = moves[direction]
        row += row_delta
        col += col_delta
        if row < 0 or row >= height or col < 0 or col >= width:
            break
        if rows[row][col] == '#':
            row -= row_delta
            col -= col_delta
            direction = direction_if_blocked
    locations = sum([row.count('X') for row in rows])
    print(locations)
