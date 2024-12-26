import functools

rulesBefore = {}
sum_middle_page_numbers = 0

def cmp_pages(page1, page2):
    if page1 == page2 or rulesBefore.get(page2) is None:
        return 0
    if page1 in rulesBefore[page2]:
        return -1
    return 1

def intersects(arr1, arr2):
    return len(set(arr1) & set(arr2)) > 0

with open('sample.txt') as file:
    for line in file:
        line = line.rstrip()
        if line.find('|') > -1:
            before, after = line.split('|')
            before, after = int(before), int(after)
            if rulesBefore.get(after) is None:
                rulesBefore[after] = []
            if not before in rulesBefore[after]:
                rulesBefore[after].append(before)
        elif line.find(',') > -1:
            update = [int(page) for page in line.split(',')]
            size = len(update)
            correctlyOrdered = True
            for i in range(size):
                page = update[i]
                if not rulesBefore.get(page) is None and intersects(rulesBefore[page], update[i + 1:]):
                    correctlyOrdered = False
                    break
            if not correctlyOrdered:
                update.sort(key=functools.cmp_to_key(cmp_pages))
                sum_middle_page_numbers += update[int(size / 2)]
print(sum_middle_page_numbers)
