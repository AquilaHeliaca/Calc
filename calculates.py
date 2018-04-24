def sum(a, b):
    """Return sum of numbers a and b"""
    return float(a)+float(b)
def substract(a, b):
    """Return substract of numbers a and b"""
    return float(a)-float(b)
def multiply(a, b):
    """Return multiply of numbers a and b"""
    return float(a)*float(b)
def divide(a, b):
    """Return divide of numbers a and b; return nothing and prints error if b = 0"""
    if float(b)!= 0.0: return float(a)/float(b)
    else: print("ERR!")