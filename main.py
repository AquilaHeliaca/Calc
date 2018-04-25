#Kalkulator ver 0.2
import parsers 
import sys

def bracket_finder(number):
    """Isolate the bracket and pass it to bracket_calculate()
    When expression is returned by bracket_calculate(), the entire expression is passed to are_brackets_there() function """
    startIndex = 0
    for x in range(len(number)-1, 0, -1):
        if number[x] == "(": 
            startIndex = x
            break
    for x in range(startIndex, len(number)):
        if number[x] == ")": 
            endIndex = x
            break
    startNumber = number[:startIndex]
    endNumber = number[endIndex+1:]
    bracket = number[startIndex+1:endIndex]
    number =  bracket_calculate(bracket, startNumber, endNumber)
    are_brackets_there(number)

def bracket_calculate(bracket, startNumber, endNumber):
    """Calculate value of expression in bracket, then return entire expression to bracket_finder"""
    numbers, operators = splitter(bracket)
    bracket = calculate(numbers, operators)

    number = startNumber + str(bracket) + endNumber
    return number

def are_brackets_there(number): 
    """Checks is bracket in expression
        If yes, bracket_finder function starts again
        If not expression is calculated and value is printed"""
    if "(" in number or ")" in number:
        bracket_finder(number)
    else:
        numbers, operators = splitter(number)
        print("{0:.12f}".format(calculate(numbers, operators))) 
    
def splitter(inputNumber):
    """seperate numbers and operators"""
    inputNumber = inputNumber.replace(" ", "")
    numbers = []
    operators = []
    number = ""
    for x in range(len(inputNumber)):
        if inputNumber[x] in "1234567890.":
            number += inputNumber[x]
        elif inputNumber[x] == ",":
            number += "."
        elif inputNumber[x] == "-":
            if x!=0:
                if inputNumber[x-1] not in "+-*/^":
                    operators.append("+")
            if number != "": 
                numbers.append(number)
            number = "-"
        elif inputNumber[x] in "+*/^":
            numbers.append(number)
            number = ""
            operators.append(inputNumber[x])
        else:
            print("Err")
    if number != "": numbers.append(number)
    return numbers, operators

def calculate(numbers, operators):
    """doing math here
    input: numbers and operators from splitter
    output: one number - result """
    
    if "^" in operators:
        operators, numbers = parsers.parse_power(numbers, operators)

    if "*" in operators or "/" in operators:
        operators, numbers = parsers.parse_divide_and_multiply(numbers, operators)

    operators, numbers = parsers.parse_substract_and_sum(numbers, operators)
    return numbers[0]

a = ""
if len(sys.argv) > 1:
    for x in range (1, len(sys.argv)):
        a += sys.argv[x]
else:
    a = input("Expression to calculate: ")
globalNumbers = globalOperators = None
if a.lower() == "help":
    print("""
    Calc ver 0.2
    Let user do basic math: + - * /
    You can also raise to power and use brackets   
    """)
elif "(" in a or ")" in a:
    bracket_finder(a)
else:
    globalNumbers, globalOperators = splitter(a)
    print(globalNumbers, globalOperators)
    print("{0:.12f}".format(calculate(globalNumbers, globalOperators)))