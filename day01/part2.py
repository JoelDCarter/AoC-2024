with open('input.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
left = [int(line.split()[0]) for line in lines]
right = [int(line.split()[1]) for line in lines]
similarity = [left_value * right.count(left_value) for left_value in left]
similarity_score = sum(similarity)
print(similarity_score)
