import calculates as calc

def parse_power(numbers, operators):
    """Prepare numbers for raising to power"""
    while len(numbers) > 1 and "^" in operators:
        position = operators.index("^")
        result = pow(float(numbers[position]), float(numbers[position+1]))
        operators, numbers = change_list_elements(operators, numbers, result, position)
    return operators, numbers

def parse_substract_and_sum(numbers, operators):
    """Prepare numbers for adding and substracting"""
    while len(numbers) > 1:
        if operators[0] == "+": 
            result = calc.sum(numbers[0], numbers[1])
        elif operators[0] == "-":
            result = calc.substract(numbers[0], numbers[1])
        operators, numbers = change_list_elements(operators, numbers, result, 0)
    return operators, numbers

def parse_divide_and_multiply(numbers, operators):
    """Prepare numbers for dividing and multiplying"""
    while len(numbers) > 1 and ("*" in operators or "/" in operators):
            if "*" in operators: 
                position = operators.index("*")
                result = calc.multiply(numbers[position], numbers[position+1])
            elif "/" in operators:
                position = operators.index("/")
                result = calc.divide(numbers[position], numbers[position+1])
            operators, numbers = change_list_elements(operators, numbers, result, position)
    return operators, numbers

def change_list_elements(operatorsList, numbersList, result, pos):
    """Updates list of operators and numbers"""
    operatorsList.pop(pos)
    numbersList.pop(pos+1)
    numbersList[pos] = result
    return operatorsList, numbersList