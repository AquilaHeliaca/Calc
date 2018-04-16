import calculates as Calc

def parsePower(numbers, operators):
    while len(numbers) > 1 and "^" in operators:
        position = operators.index("^")
        result = pow(float(numbers[position]), float(numbers[position+1]))
        operators, numbers = changeListElements(operators, numbers, result, position)
    return operators, numbers

def parseSubstractAndSum(numbers, operators):
    while len(numbers) > 1:
        if operators[0] == "+": 
            result = Calc.Sum(numbers[0], numbers[1])
        elif operators[0] == "-":
            result = Calc.Substract(numbers[0], numbers[1])
        operators, numbers = changeListElements(operators, numbers, result, 0)
    return operators, numbers

def parseDivideAndMultiply(numbers, operators):
    while len(numbers) > 1 and ("*" in operators or "/" in operators):
            if "*" in operators: 
                position = operators.index("*")
                result = Calc.Multiply(numbers[position], numbers[position+1])
            elif "/" in operators:
                position = operators.index("/")
                result = Calc.Divide(numbers[position], numbers[position+1])
            operators, numbers = changeListElements(operators, numbers, result, position)
    return operators, numbers

def changeListElements(operatorsList, numbersList, result, pos):
    operatorsList.pop(pos)
    numbersList.pop(pos+1)
    numbersList[pos] = result
    return operatorsList, numbersList