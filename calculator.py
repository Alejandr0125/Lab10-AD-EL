"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
<<<<<<< HEAD
def square_root(a): # raise ValueError if a < 0
    if a < 0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a, b):  # can have negative nums
    return math.hypot(a,b)


def add(a, b): a+b

def subtract(a, b): a - b

def multiply(a, b): a * b
=======
import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
>>>>>>> c96d3b11f949fef0f15c3023879faa2d6735ef87

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
<<<<<<< HEAD
    return a/b

def logarithm(a, b): math.log(a,b)#use math library + raise ValueError

def exponent(a, b): a**b


=======
    return b/a

def log(a, b):
    return math.log(a,b)

def power(a, b):
    return a**b
>>>>>>> c96d3b11f949fef0f15c3023879faa2d6735ef87


