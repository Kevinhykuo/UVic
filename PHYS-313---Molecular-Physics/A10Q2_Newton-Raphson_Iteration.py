import sympy as sym
import scipy as sci
import math as m
from sympy import Symbol
from scipy.optimize import newton, fsolve, fmin, root
from scipy.misc import derivative

# x = Symbol('x')
# y = Symbol('y')

# Solving equations of the form:
# ax^2 + bxy + cy^2 - d = 0

# =============
# 1st function:
# =============
# print('===Part (a)===')
# Define the coefficients
Coeff1 = [12, 18, 15, -9]
a1 = Coeff1[0]
b1 = Coeff1[1]
c1 = Coeff1[2]
d1 = Coeff1[3]

# Define the main function
def F1(x, y):
    f1 = a1*x**2 + b1*x*y + c1*y**2 + d1
    return(f1)

print('Equations:')
print('F1 = ', a1,'x^2 + ', b1, 'xy + ', c1, 'y^2 + ', d1)

# Define the partial derivatives of the function
def dxF1(x, y):
    dxf1 = 2*a1*x + b1*y
    return(dxf1)

def dyF1(x, y):
    dyf1 = b1*y + 2*c1*y
    return(dyf1)


# sol1 = newton(F1, (0, 0), maxiter=50)
#
# print('Part (a) solution:', sol1)

# =============
# 2nd Equation:
# =============
# print('===Part (b)===')
# Define the coefficients
Coeff2 = [16, 23, 7, -6]

a2 = Coeff2[0]
b2 = Coeff2[1]
c2 = Coeff2[2]
d2 = Coeff2[3]

# Define the main function
def F2(x, y):
    f2 = a2*x**2 + b2*x*y + c2*y**2 + d2
    return(f2)

print('F2 = ', a2,'x^2 + ', b2, 'xy + ', c2, 'y^2 + ', d2)

# Define the partial derivatives of the function
def dxF2(x, y):
    dxf2 = 2*a2*x + b2*y
    return(dxf2)

def dyF2(x, y):
    dyf2 = b2*y + 2*c2*y
    return(dyf2)
#
# sol2 = newton(F2, (0, 0), maxiter=50)
#
# print('Part (b) solution:', sol2)

# =======================================
# Difference between 1st and 2nd Function
# =======================================
# Define the coefficients
Coeff3 = [Coeff1[0]-Coeff2[0], Coeff1[1]-Coeff2[1], Coeff1[2]-Coeff2[2], Coeff1[3]-Coeff2[3]]
a3 = Coeff3[0]
b3 = Coeff3[1]
c3 = Coeff3[2]
d3 = Coeff3[3]

# Define the function
def F3(x, y):
    f3 = a3*x**2 + b3*x*y + c3*y**2 + d3
    return(f3)

# =======================
# Commence Newton-Rahpson
# =======================
# k = -b/(2*a) + 0.00001 # Max/min of the quadratic equation + a bit to the right
# h = -b/(2*a) - 0.00001 # Same as above but to left

# def htop(x, y):
#     htop = dyF2(x, y)*F1(x, y) - dyF1(x, y)*F2(x, y)
#     return(htop)
#
# def ktop(x, y):
#     ktop = dxF1(x, y)*F2(x, y) - dxF2(x, y)*F1(x, y)
#     return(ktop)
#
# def bott(x, y):
#     bott = dxF1(x, y)*dyF2(x, y) - dyF1(x, y)*dxF2(x, y)
#     return(bott)
#
# def H(x, y):
#     H = htop(x, y)/bott(x, y)
#     return(H)
#
# def K(x, y):
#     K = ktop(x, y)/bott(x, y)
#     return(K)
#
# k = 1
# h = 1
#
#
# for i in range(10): # Execute Newton-Raphson
#     h = h - H(1, 1)
#     k = k - K(1, 1)
# print('Solution:', h, k)


# min = fmin(F3, x0=[0,0])
# print(min)

# =========================
# Commence "Newton-Rahpson"
# =========================

def eqn(p):
    x, y = p
    eq1 = F1(x,y)
    eq2 = F2(x,y)
    return (eq1, eq2)


x1, y1 = fsolve(eqn, (1, 1))
x2, y2 = fsolve(eqn, (-1, 1))
x3, y3 = fsolve(eqn, (-1, -1))
x4, y4 = fsolve(eqn, (1, -1))

print(' ')
print ("Solutions: \n", x1, y1, '\n', x2, y2, '\n', x3, y3, '\n', x4, y4, '\n',)