with open('input.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
left = [int(line.split()[0]) for line in lines]
right = [int(line.split()[1]) for line in lines]
left.sort()
right.sort()
distance = [max(left[i], right[i]) - min(left[i], right[i]) for i in range(0, len(lines))]
total_distance = sum(distance)
print(total_distance)
