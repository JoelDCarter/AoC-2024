import itertools
import re

nodes = {}
antinodes = {}

def add_antinode(x, y):
    within_map_area = 0 if x < 0 or x >= width or y < 0 or y >= height else 1
    antinodes[(x, y)] = within_map_area
    return bool(within_map_area)

with open('sample.txt', 'r', encoding='UTF-8') as file:
    rows = [line.rstrip() for line in file.readlines()]
    width = len(rows[0])
    height = len(rows)
    for j in range(height):
        for node in re.finditer('[\dA-Za-z]', rows[j]):
            f = node[0]
            if nodes.get(f) is None:
                nodes[f] = []
            nodes[f].append((node.start(), j))
    for f in nodes.keys():
        antenna_pairs = list(itertools.combinations(nodes[f], 2))
        for pair in antenna_pairs:
            x1, y1 = pair[0]
            x2, y2 = pair[1]
            x_delta = x2 - x1
            y_delta = y2 - y1
            distance = abs(x_delta) + abs(y_delta)
            if distance > 1:
                add_antinode(x1, y1)
                add_antinode(x2, y2)
                i = 1
                while add_antinode(x1 - x_delta * i, y1 - y_delta * i):
                    i += 1
                i = 1
                while add_antinode(x2 + x_delta * i, y2 + y_delta * i):
                    i += 1
    print(sum(antinodes.values()))
