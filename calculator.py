"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example

def square_root(a): # raise ValueError if a < 0
    if a < 0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a, b):  # can have negative nums
    return math.hypot(a,b)


def add(a, b): a+b

def subtract(a, b): a - b

def multiply(a, b): a * b

import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError

    return a/b



def logarithm(a, b):
    return math.log(a,b)

def exp(a, b):
    return a**b

def square_root(a,b=.5):
    return a ** b

def hypotanuse




