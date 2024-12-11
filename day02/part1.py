def sign(x):
    return (x > 0) - (x < 0)

with open('input.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
reports = [[int(level) for level in line.split()] for line in lines]
reports_level_deltas = [[levels[i] - levels[i - 1] for i in range(1, len(levels))] for levels in reports]
reports_analysis = [(0 if max([abs(delta) for delta in level_deltas]) > 3 or min([sign(delta) for delta in level_deltas]) != max([sign(delta) for delta in level_deltas]) else 1) for level_deltas in reports_level_deltas]
print(sum(reports_analysis))