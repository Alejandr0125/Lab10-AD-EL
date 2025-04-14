"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
#https://github.com/Alejandr0125/Lab10-AD-EL.git
#Partner 1: Alejandro Delatorre
#Partner 2: Ethan Laue
import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)# raise ValueError if a < 0

def hypotenuse(a, b):
    return math.hypot(a, b) # can have negative nums

def add(a, b):
    return a + b

def mul(a, b):
    return a * b
def div(a, b):
    if a==0:
        raise ZeroDivisionError
    return b / a

def exp(a, b):
    return a**b




def subtract(a, b):
    return a - b

def logarithm(a, b):
    if b <= 0 or a <= 1:
        raise ValueError
    return math.log(b,a)# use math library/raise ValueError



