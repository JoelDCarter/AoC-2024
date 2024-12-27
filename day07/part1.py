import itertools

total_calibration_result = 0
with open('sample.txt') as file:
    operators = '+', '*'
    for line in file:
        line = line.rstrip()
        result, operands = line.split(': ')
        result = int(result)
        operands = [int(operand) for operand in operands.split(' ')]
        operation_combos = list(itertools.product(operators, repeat = len(operands) - 1))
        for i in range(len(operation_combos)):
            operations = operation_combos[i]
            test = operands[0]
            for j in range(len(operands) - 1):
                if operations[j] == '+':
                    test += operands[j + 1]
                else:
                    test *= operands[j + 1]
            if test == result:
                total_calibration_result += result
                break
    print(total_calibration_result)