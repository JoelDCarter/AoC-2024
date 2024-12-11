def sign(x):
    return (x > 0) - (x < 0)

def analyze(levels):
    level_deltas = [levels[i] - levels[i - 1] for i in range(1, len(levels))]
    return 0 if level_deltas.count(0) > 0 or max([abs(delta) for delta in level_deltas]) > 3 or min([sign(delta) for delta in level_deltas]) != max([sign(delta) for delta in level_deltas]) else 1

def problem_dampener(levels):
    if analyze(levels) == 1:
        return 1
    else:
        for i in range(len(levels)):
            new_levels = levels.copy()
            del new_levels[i]
            if analyze(new_levels) == 1:
                return 1
    return 0
                   
with open('input.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
reports = [[int(level) for level in line.split()] for line in lines]
reports_analysis = [problem_dampener(levels) for levels in reports]
print(sum(reports_analysis))