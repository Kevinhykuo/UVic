import sys
import numpy as np
import math as m
import matplotlib.pyplot as plt
from numpy import sin, cos, pi, exp
from scipy.special import eval_laguerre
from scipy.misc import derivative
from scipy.integrate import quad
from scipy.optimize import fmin

#Constants
epsilon0 = 8.854187817*10**(-12)    #Permittivity of free space
hbar = 1.054571726*10**(-34)        #Plank's constant
e = 1.602176487*10**(-19)           #Electron charge
Mp = 1.672621637*10**(-27)          #Mass of proton
Me = 9.10938215*10**(-31)           #Mass of electron

#Quantum numbers
n = 2
l = 0 #For an s electron

z = 1 #For H atoms

#Functions
mu = (Mp*Me)/(Mp+Me)                        # Reduced mass
# a0 = 4*pi*epsilon0*(hbar**2)/(z*mu*(e**2))  #Bohr radius (In meters)
a0 = 1                                      #Bohr radius (In terms of Bohr radius)
print('Bohr radius:', a0)
print('Reduced mass:', mu)

r = np.linspace(0, 10*a0, 1000) # Generate values of r

# Components of the radial wave-function
def R1(r):
    return( ((2*z*r)/(n*a0))**l )

def R2(r):
    return( exp(-z*r/(n*a0)) )

def R3(r):
    #return( 0.5*((2*z*r/(n*a0))**2 - 4*(2*z*r/(n*a0)) + 2) )
    return( eval_laguerre(n+l, 2*z*r/(n*a0)) )

def R4(r):
    R4 = derivative(R3, 2*z*r/(n*a0), 2*l+1)
    return(R4)

# Radial component of Wave-function
def R(r):
    R = R1(r)*R2(r)*R4(r)
    return(R)

# Probability amplitude (Not normalized)
def Rpa(r):
    rpa = R(r)*R(r)
    return(rpa)

# Normalization constant
# (Can't use this because it only integrates form 0 to 10*a0)
# NC = quad(Rpa, 0, m.inf)
# print('NC:', NC[0])

# Derivative of R
def RX(r):
    RX = derivative(R, r, 1)
    return(RX)
# print('RX:', RX(r))

# Finding where the extermas of R
RXz = (np.where( abs(RX(r)) <= 2.5*10**(-3) )[0])
# print('RX values near zero:', RXz)

# A = []
# i = 0
# while i <= len(RXz)-1:
#     Rz = RX[RXz[i]]
#     A.append(Rz)
#     i += 1
#
# print(A)

# The x and y axis
def y(r):
    Y = (a0*(r*R(r)))**2
    return(Y)

# def x(r):
#     X = r/a0
#     return(X)
x =r/a0
# print(y)

y_ = (np.where(y(r) <= 10**(-5))[0]) #Find where y is near zero
# print('Values where y is near zero:', y_)

i = 0
A = []
print('x values where y is near zero:')
while i <= len(y_)-1:
    x2 = x[y_[i]]
    A.append(x2)
    i += 1
print(A)
#
# print( fmin(y(r), np.array([0,0,0])) )
# print( fmin(-y(r), 0))

# print(x)
# print(y)

#=================
# Plotting time!!!
#=================
plt.plot(x, y(r)/8)

plt.title(r'Radial probability amplitude of a 2s electorn in a hydrogen-like atom', fontsize=12)
plt.xlabel(r' $\frac{r}{a_0}$ ', fontsize=14)
plt.ylabel(r' $r^2 R^2 a_0$ ', fontsize=14)
plt.xlim(0,10)
plt.ylim(0,0.2)
plt.show()

sys.exit()