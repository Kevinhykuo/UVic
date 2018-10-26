import sys

import sympy as sym
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import seaborn as sbn
from sympy import Integral, Symbol


'''
The plan here is just the same as the previous plan: 
Get the integrals. 
Make the code do the integrals.
Make the code do the integrals again for different 'p's (angle: Phi's). 
d = 2R and 10R
'''


#Defining the 'd's.
#Here we let R=1 again, because we want a general graph of the magnetic field
#Same as last question
d1 = 2
d2 = 10

#Defining the Symbols and variables
I = Symbol('I') #The current through the wire
R = Symbol('R') #The radius of the coils
o = Symbol('o') #The angle with respect to the x-axis (Theta)
p = Symbol('p') #The angle with respect to the z-axis (Phi)


#Here are the general forms of the functions in the integral
#Bx = sym.cos(o)*sym.cos(p)/(R**2+d**2+2*R*d*sym.sin(p)Cos(o))**1.5
#By = sym.sin(o)*sym.cos(p)/(R**2+d**2+2*R*d*sym.sin(p)Cos(o))**1.5
#Bz = (R-d*sym.cos(o)*sym.sin(p))/(R**2+d**2+2*R*d*sym.sin(p)Cos(o))**1.5

#Do integrals for D=2R
for p in (0, sym.pi, 0.1*sym.pi):
    Bx2R = sym.cos(o)*sym.cos(p)/(1+d1**2+2*d1*sym.sin(p)*sym.cos(o))**1.5
    By2R = sym.sin(o)*sym.cos(p)/(1+d1**2+2*d1*sym.sin(p)*sym.cos(o))**1.5
    Bz2R = (1-d1*sym.cos(o)*sym.sin(p))/(1+d1**2+2*d1*sym.sin(p)*sym.cos(o))**1.5

    Integral(Bx2R, (o, 0, 2*sym.pi)).doit()
    Integral(By2R, (o, 0, 2*sym.pi)).doit()
    Integral(Bz2R, (o, 0, 2*sym.pi)).doit()

#Plot it out
plot(p, Bx2R, p, By2R, p, Bz2R)
legend([Bx2R, By2R, Bz2R])
title('Magnitude of magnetic field at points in the arc of radius = 2R')
xlabel('Points in the arc corresponding to angle "phi" (p)')
ylabel('Magnitude of each vectors of the magnetic field')

#Do the integrals for D=10R
for p in (0, sym.pi, 0.1*sym.pi):
    Bx10R = sym.cos(o)*sym.cos(p)/(1+d2**2+2*d2*sym.sin(p)*sym.cos(o))**1.5
    By10R = sym.sin(o)*sym.cos(p)/(1+d2**2+2*d2*sym.sin(p)*sym.cos(o))**1.5
    Bz10R = (1-d2*sym.cos(o)*sym.sin(p))/(1+d2**2+2*d2*sym.sin(p)*sym.cos(o))**1.5

    Integral(Bx10R, (o, 0, 2*sym.pi)).doit()
    Integral(By10R, (o, 0, 2*sym.pi)).doit()
    Integral(Bz10R, (o, 0, 2*sym.pi)).doit()

# Plot it out
plot(p, Bx10R, p, By10R, p, Bz10R)
legend([Bx10R, By10R, Bz10R])
title('Magnitude of magnetic field at points in the arc of radius = 2R')
xlabel('Points in the arc corresponding to angle "phi" (p)')
ylabel('Magnitude of each vectors of the magnetic field')


