with open('input.txt', 'r', encoding='UTF-8') as file:
    rows = [line.rstrip() for line in file.readlines()]
    width = len(rows[0])
    height = len(rows)
    count = 0
    for i in range(1, width - 1):
        for j in range(1, height - 1):
            if rows[j][i] == 'A':
                tl = rows[j - 1][i - 1]
                tr = rows[j - 1][i + 1]
                bl = rows[j + 1][i - 1]
                br = rows[j + 1][i + 1]
                if ((tl == 'M' and br == 'S') or (tl == 'S' and br == 'M')) and \
                   ((tr == 'M' and bl == 'S') or (tr == 'S' and bl == 'M')):
                    count += 1
    print(count)