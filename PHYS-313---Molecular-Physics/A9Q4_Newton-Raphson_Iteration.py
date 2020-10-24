import sympy as sym
import scipy as sci
import math as m
from sympy import Symbol
from scipy.optimize import newton
from scipy.misc import derivative

# Newton-Raphson solver:
# sol = newton(F, x0)

x = Symbol('x')

# =======
# Part a:
# =======
# For quadratic equations of form:
# ax^2 + bx + c = 0
print('===Part (a)====')
a = 3.3
b = -7.9
c = 2.7

# Check answer using quadratic equation
y1 = (-b+(b**2 - 4*a*c)**0.5)/(2*a)
y2 = (-b-(b**2 - 4*a*c)**0.5)/(2*a)
print('Correct answer:', y1, y2)

# Using scipy.optimize.newton: Does not converge
# x1 = -b / (2 * a) + 0.00001 # Max/min of the quadratic equation + a bit to the right
# x2 = -b / (2 * a) - 0.00001 # Same as above but to left
# #
# def F1(x):
#     f1 = 3.3*x**2 - 4.9*x + 2.7
#     return(f1)
# #
# sol1 = newton(F1, x1, maxiter=50)
# sol2 = newton(F1, x2, maxiter=50)
# print(sol1, sol2)


# This way doesn't work either:
# x1 = -b / (2 * a) + 0.00001 # Max/min of the quadratic equation + a bit to the right
# x2 = -b / (2 * a) - 0.00001 # Same as above but to left
#
# def F1(x):
#     f1 = 3.3*x**2 - 4.9*x + 2.7
#     return(f1)
#
# def dF1(x):
#     df1 = 6.6*x - 4.9
#     return(df1)
#
# def NR(x):
#     x = x - F1(x)/dF1(x)
#     return(x)
#
# i=0
# while i<1000:
#     x1 = NR(x1)
#     x2 = NR(x2)
#     i+=1
#
# print(NR(x1), NR(x2))
#

# This works:
x1 = -b/(2*a) + 0.00001 # Max/min of the quadratic equation + a bit to the right
x2 = -b/(2*a) - 0.00001 # Same as above but to left

for i in range(100): # Execute Newton-Raphson
    f1 = a * x1 ** 2 + b * x1 + c
    f2 = a * x2 ** 2 + b * x2 + c
    df1 = 2*a*x1 + b
    df2 = 2*a*x2 + b
    x1 = x1 - f1/df1
    x2 = x2 - f2/df2
print('Part (a) solution:', x1, x2)


print(' ')

# =======
# Part b:
# =======
print('===Part (b)===')
def F2(x):
    f2 = m.log(x**2 + 3) - 11/x
    return(f2)

sol2 = newton(F2, 0.1, maxiter=50)

print('Part (b) solution:', sol2)