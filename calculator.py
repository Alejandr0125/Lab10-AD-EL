"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
<<<<<<< HEAD

=======
>>>>>>> 724bdeb2c578d08f57a6210a799177a88ca56dbd
def square_root(a): # raise ValueError if a < 0
    if a < 0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a, b):  # can have negative nums
    return math.hypot(a,b)

def add(a, b):
    return a + b

def subtract(a, b): a - b

def multiply(a, b): a * b
<<<<<<< HEAD

import math
def add(a, b):
    return a + b
=======
>>>>>>> 724bdeb2c578d08f57a6210a799177a88ca56dbd

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError
<<<<<<< HEAD

    return a/b



def logarithm(a, b):
=======
    return a/b

def logarithm(a, b): math.log(a,b)

def exponent(a, b): a**b




def log(a, b):
>>>>>>> 724bdeb2c578d08f57a6210a799177a88ca56dbd
    return math.log(a,b)

def exp(a, b):
    return a**b

<<<<<<< HEAD
def square_root(a,b=.5):
    return a ** b

def hypotanuse


=======
>>>>>>> 724bdeb2c578d08f57a6210a799177a88ca56dbd


