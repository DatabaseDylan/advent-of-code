def calculate(numbers: list[int], operation_type: str) -> int:
    if operation_type == '+':
        total_num = 0
        for number in numbers:
            total_num += number
    elif operation_type == '*':
        total_num = 1
        for number in numbers:
            total_num *= number
    else:
        print("Uh oh.. something is not right!")

    return total_num

def main():
    with open('math_problems.txt', 'r') as file:
        math_problems = file.read().splitlines()

    grand_total = 0

    for line in enumerate(math_problems):
        current_line = line[1]
        math_problems[line[0]] = [current_line for current_line in current_line.split() if current_line != '']

    # loop over all 1000 columns (e.g. math problems)
    for column_index in range(len(math_problems[0])):
        numbers_to_calc = []
        
        # loop over each row in the column (e.g. our numbers and operation type)
        # skip last row because that is where operation type is stored
        for row_index in range(len(math_problems) - 1):
            numbers_to_calc.append(int(math_problems[row_index][column_index]))
        
        operation_type = math_problems[-1][column_index]
        total = calculate(numbers=numbers_to_calc, operation_type=operation_type)
        grand_total += total

    print(grand_total)

if __name__ == '__main__':
    main()