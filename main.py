#Kalkulator ver 0.1.2

def Splitter(inputNumber):
    numbers = []
    operators = []
    number = ""
    for x in range(len(inputNumber)):
        if inputNumber[x] in "1234567890.":
            number += inputNumber[x]
        elif inputNumber[x] in "+-*/^":
            numbers.append(number)
            number = ""
            operators.append(inputNumber[x])
        else:
            print("Err")
    if number != "": numbers.append(number)
    return numbers, operators

def Calculate(numbers, operators):
    #potęgowanie
    if "^" in operators:
        while len(numbers) > 1 and "^" in operators:
            position = operators.index("^")
            result = pow(int(numbers[position]), int(numbers[position+1]))
            operators, numbers = changeListElements(operators, numbers, result, position)

    #mnożenie i dzielenie
    if "*" in operators or "/" in operators:
        while len(numbers) > 1 and ("*" in operators or "/" in operators):
            if "*" in operators and "/" in operators:
                if operators.index("*")<operators.index("/"): position = operators.index("*")
                else: position = operators.index("/")
            elif "/" in operators: 
                position = operators.index("/")
                result = Divide(numbers[position], numbers[position+1])
                operators, numbers = changeListElements(operators, numbers, result, position)
            else:
                position = operators.index("*")
                result = Multiply(numbers[position], numbers[position+1])
                operators, numbers = changeListElements(operators, numbers, result, position)

    #dodawanie i odejmowanie
    while len(numbers) > 1:
        if operators[0] == "+": 
            result = Sum(numbers[0], numbers[1])
            operators, numbers = changeListElements(operators, numbers, result, 0)
        elif operators[0] == "-":
            result = Substract(numbers[0], numbers[1])
            operators, numbers = changeListElements(operators, numbers, result, 0)
    print(numbers)
    return numbers[0]  
        
def changeListElements(operatorsList, numbersList, result, pos):
    operatorsList.pop(pos)
    numbersList.pop(pos+1)
    numbersList[pos] = result
    return operatorsList, numbersList

def Sum(a, b):
    return int(a)+int(b)
def Substract(a, b):
    return int(a)-int(b)
def Multiply(a, b):
    return int(a)*int(b)
def Divide(a, b):
    if int(b)!= 0: return int(a)/int(b)
    else: print("ERR!")


a = input("Wyrażenie do obliczenia: ")
globalNumbers, globalOperators = Splitter(a)
print(globalNumbers, globalOperators)
print(Calculate(globalNumbers, globalOperators))