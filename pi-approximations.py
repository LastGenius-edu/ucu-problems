# Calculating three different Pi approximations using Leibniz, Archimedes and Chudnosky algorithms

import math
import decimal

def leibniz():
    n = pow(10, 8)
    sum = 0
    j = 0

    for i in range (1, n+1):
        power = (i + 1) % 2
        sum += (1 / (i + j)) * pow(-1, power)
        j += 1

    pi1 = sum * 4

    print("Number of elements in the series:", n)
    print(pi1)
    print("Difference between the approximation and math.pi is", pi1 - math.pi)


def archimedes():
    lengthsq = 2.0
    sides = 4

    for i in range(16):
        lengthsq = 2 - 2 * math.sqrt(1 - lengthsq / 4)
        sides = sides * 2
    
    pi2 = (sides / 2) * math.sqrt(lengthsq)

    print("We've approximated pi from", sides, "-gon", '\n', end = '')
    print(pi2)
    print("Difference between the approximation and math.pi is", pi2 - math.pi)

decimal.getcontext().prec = 36

def factorial(n):
    if n<1:
        return 1
    else:
        return n * factorial(n-1)
    
def chudnovsky(n):
    pi3 = decimal.Decimal(0)
    k = 0
    for k in range(0, n):
        pi3 += (decimal.Decimal(-1)**k) * (decimal.Decimal(factorial(6*k)) / ((factorial(k)**3)*(factorial(3*k))) * (13591409+545140134*k) / (640320**(3*k)))
        
    pi3 = pi3 * decimal.Decimal(10005).sqrt() / 4270934400
    pi3 = pi3 ** (-1)

    print("We've approximated pi from", n, "iterations")
    print(pi3)
    print("Difference between the approximation as a float and math.pi is", float(pi3) - math.pi)


leibniz()
print('\n', end='')
archimedes()
print('\n', end='')
chudnovsky(3)
print('\n', end='')

