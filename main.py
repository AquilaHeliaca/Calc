#Kalkulator ver 0.1.2
import parsers 
import calculates as Calc

def nawiaskiller(number):#mocno tymczasowa nazwa zmienić jak najszybciej
    #podzielić te gówno na mniejsze funkcje

    #funkcja 1. - znajduje nawias, wyodrębnia go z reszty wyrażenia
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
    print(startNumber , str(nawias), endNumber)
    #funkcja 2. - przekazuje zawartość nawiasu do splittera, wynik do obliczeń, umieszcza wynik z powrotem w całym wyrażeniu
    numbers, operators = Splitter(nawias)
    nawias = Calculate(numbers, operators)

    number = startNumber + str(nawias) + endNumber
    print(startNumber , str(nawias), endNumber)
    #********
    
    if "(" in number or ")" in number:#przerobić nawiaschecker zeby dało się go tu użyc a nie powtarzać kod
        nawiaskiller(number) 
    else:
        numbers, operators = Splitter(number)
        print(Calculate(numbers, operators))

def nawiaschecker(number): #narazie nie działa, kod jest umieszczony w głównym ciągu poleceń sprawdzić później o chuj tu wogóle
    if "(" in number or ")" in number:#i zrobić to działającym
        nawiaskiller(number)
    else:
        globalNumbers, globalOperators = Splitter(number)
    
def Splitter(inputNumber):
    """seperate numbers and operators"""
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
    """"doing math here
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
    print(numbers)#print tyylko do testowania, usunąć to potem
    return numbers[0]

globalNumbers = globalOperators = None
a = input("Wyrażenie do obliczenia: ")

if "(" in a or ")" in a:
    nawiaskiller(a)
else:
    globalNumbers, globalOperators = Splitter(a)
    #print(globalNumbers, globalOperators)
    print(Calculate(globalNumbers, globalOperators))
#globalNumbers, globalOperators = Splitter(a)
