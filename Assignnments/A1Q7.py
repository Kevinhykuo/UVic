import sys
import math

'''
Approximate single variable integral using Riemann sum.
Integral of f(x) = x^2 - Cos(x) from x=0 to 2
Intervals of 10, 100, 1000
f = x**2 - math.acos(x)
'''

print("PHYS 326 - Assignment 1 - Q7")
print("Approximate single variable integral using Riemann sum." "\n"
        "Evaluate f(x) = x^2 - Cos(x) from x=0 to 2" "\n"
        "Intervals of 10, 100, 1000")

def f(x):
    return x**2-math.acos(x)

x1 = 0
x2 = 2
n1 = 10
n2 = 100
n3 = 1000

Dx1 = (x2-x1)/n1
Dx2 = (x2-x1)/n2
Dx3 = (x2-x1)/n3

i = 0
j = 0
k = 0
A1 = 0
A2 = 0
A3 = 0

while (i <= (n1 + 1)):
    A1 = f(x2) * Dx1 + A1
    i = i + 1

while (j <= (n2 + 1)):
    A2 = f(x2) * Dx2 + A2
    j = j + 1

while (k <= (n3 + 1)):
    A3 = f(x2) * Dx3 + A3
    k = k + 1

print("Area approximated using Riemann sum (n=10) is", A1)
print("Area approximated using Riemann sum (n=100) is", A2)
print("Area approximated using Riemann sum (n=1000) is", A3)
