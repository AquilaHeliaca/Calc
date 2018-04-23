#Kalkulator ver 0.2
import parsers 
import calculates as Calc
import sys

def bracketFinder(number):
    """Isolate the bracket and pass entire divided input to nawiaskurwer
    When expression is returned by nawiaskurwer, it's pass to nawiaschecker """
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
    nawias = number[startIndex+1:endIndex]
    print(startNumber , str(nawias), endNumber) #tymczasowe do logowania
    number =  nawiaskurwer(nawias, startNumber, endNumber)
    nawiaschecker(number)

def nawiaskurwer(nawias, startNumber, endNumber):#NNAZWA BARDZO BARDZO TYMCZASOWA
    """Calculate value in bracket, then join entire math expression and return it to bracket finder"""
    numbers, operators = Splitter(nawias)
    nawias = Calculate(numbers, operators)

    number = startNumber + str(nawias) + endNumber
    print(startNumber , str(nawias), endNumber)
    return number

def nawiaschecker(number): 
    """checks if bracket still present in fucking number
        when yes function nawiaskiller start again"""
    if "(" in number or ")" in number:
        bracketFinder(number)
    else:
        numbers, operators = Splitter(number)
        print(Calculate(numbers, operators)) 
    
def Splitter(inputNumber):
    """seperate numbers and operators"""
    inputNumber = inputNumber.replace(" ", "")
    numbers = []
    operators = []
    number = ""
    for x in range(len(inputNumber)):
        if inputNumber[x] in "1234567890.":
            number += inputNumber[x]
        elif inputNumber[x] in ",":
            number += "."
        elif inputNumber[x] in "+-*/^":
            numbers.append(number)
            number = ""
            operators.append(inputNumber[x])
        else:
            print("Err")
    if number != "": numbers.append(number)
    return numbers, operators

def Calculate(numbers, operators):
    """doing math here
    input: numbers and operators from splitter
    output: one number - result """
    #potęgowanie
    if "^" in operators:
        operators, numbers = parsers.parsePower(numbers, operators)

    #mnożenie i dzielenie
    if "*" in operators or "/" in operators:
        operators, numbers = parsers.parseDivideAndMultiply(numbers, operators)

    #dodawanie i odejmowanie
    operators, numbers = parsers.parseSubstractAndSum(numbers, operators)
    return numbers[0]

#usage of sys.argv
a = ""
if len(sys.argv) > 1:
    for x in range (1, len(sys.argv)):
        a += sys.argv[x]
else:
    a = input("Wyrażenie do obliczenia: ")
globalNumbers = globalOperators = None
if a.lower() == "help":
    print("""
    Calc ver 0.2
    Let user do basic math: + - * /
    You can also add to power and use brackets   
    """)
elif "(" in a or ")" in a:
    bracketFinder(a)
else:
    globalNumbers, globalOperators = Splitter(a)
    print(Calculate(globalNumbers, globalOperators))
