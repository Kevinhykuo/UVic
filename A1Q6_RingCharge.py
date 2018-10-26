'''
import sys

import sympy as sym
import numpy as np
import scipy as sci
from sympy import Symbol, Integral
from scipy.integrate import quad

#Define the constants
epsilon_0 = 8.854187817*10**(-12)

#Deine the variable
theta = Symbol('theta')

#Define the equation
f = (5/4 - sym.cos(theta))**(-0.5)

#Integrate the equation from 0 to pi
I = Integral(f, (theta, 0, sym.pi)).doit()

#def integrand(theta)
#   return (5/4 - sym.cos(theta))**(-0.5)

#I = quad(integrand, 0, sym.pi)

#Answer = 1/(4*sym.pi*epsilon_0)

#print('The potential at point A is Q/a^2')
#print(Answer)
print(I)
'''

import sympy as sym
import cmath as math
from scipy.integrate import quad

#Define the constants
a = 5/4
b = -0.5
epsilon_0 = 8.854187817*10**(-12) #Permeability of free space

#Define the integral to be evaluated
def integrand(theta, a, b): #Integrate with respect to theta (angle) from a to b
    return (a - sym.cos(theta))**(b)

#Evaluate the integral
I = quad(integrand, 0, math.pi, args=(a, b))

K = 4*(math.pi**2)*epsilon_0
I2 = I[0]/K  #Dividing the integral by 4*pi^2*epsilon_0

#Print the answer
print('Answer is Q/(4*pi^2*epsilon_0*a)',I)
print('This is also equal to', I2,'Q/a')

#print(sci.pi)
#print('Rounding to four significant digits:', round(I2, 3))