# helpers

from .calculator import Calc

def say_hello():
    print("Hello from helpers")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)