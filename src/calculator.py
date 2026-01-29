 # calculator.py

def add(x, y):
    """Return the sum of x and y"""
    return x + y

def subtract(x, y):
    """Return x minus y"""
    return x - y

def multiply(x, y):
    """Return x multiplied by y"""
    return x * y

def combine(x, y):
    """Return the sum of add, multiply, subtract"""
    return add(x, y) + multiply(x, y) + subtract(x, y)

from calculator import add, subtract, multiply, combine

print(add(2,3))  
print(subtract(6,2))  
print(multiply(3,3))  
print(combine(2,3))  