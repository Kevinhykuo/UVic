import sys

import sympy as sym
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import seaborn as sbn
from sympy import Integral, Symbol
from pylab import plot, show, title, xlabel, ylabel, legend

#Define the symbols
R = 1 #Set R = 1, so the problem essentially becomes a unit
u = Symbol('u') #This is the angle theta (with respect to x-axis)
p = Symbol('p') #This is the angle phi (with respect to z-axis)

#Define the Ds'
D1 = 2
D2 = 10

#For D = 2R
#A for loop for phi in range of 0 to pi/2 in steps of 0.05pi
for p in (0, sym.pi/2, 0.05*sym.pi):
    Ax1 = -sym.sin(u) / (D1**2 + 1 - 2*D1*sym.sin(p)*sym.cos(u))**0.5
    Ay1 = sym.cos(u) / (D1 ** 2 + 1 - 2 * D1 * sym.sin(p) * sym.cos(u))** 0.5

    Integral(Ax1, (u, 0, 0.5*sym.pi)).doit()
    Integral(Ay1, (u, 0, 0.5*sym.pi)).doit()

#Plot it all out
plot(p, Ax1, p, Ay1)
legend([Ax1, Ay1])
title('Vector potential from z-axis to x-axis when D = 2R')
xlabel('Angle "phi" (p)')
ylabel('Magnitude of the vector potential for Ax and Ay')

# For D = 10R
# A for loop for phi in range of 0 to pi/2 in steps of 0.05pi
for p in (0, sym.pi/2, 0.05 * sym.pi):
    Ax2 = -sym.sin(u) / (D2 ** 2 + 1 - 2 * D2 * sym.sin(p) * sym.cos(u)) ** 0.5
    Ay2 = sym.cos(u) / (D2 ** 2 + 1 - 2 * D2 * sym.sin(p) * sym.cos(u)) ** 0.5

    Integral(Ax2, (u, 0, 0.5*sym.pi)).doit()
    Integral(Ay2, (u, 0, 0.5*sym.pi)).doit()

#Plot it all out
plot(p, Ax2, p, Ay2)
legend([Ax2, Ay2])
title('Vector potential from z-axis to x-axis when D = 2R')
xlabel('Angle "phi" (p)')
ylabel('Magnitude of the vector potential for Ax and Ay, (uIR^2)/(4pi)')

# HERE COMES THE DIPOLES!!!
# For D=2R and D=10R
Vector = []
Vector2 = []

for p in (0, sym.pi/2, 0.1 * sym.pi):
    AyD1 = R*R*sym.sin(p) / (R*D1) #D=2R
    Vector.append(AyD1)
    AyD2 = R*R*sym.sin(p) / (R*D2) #D=10R
    Vector2.append(AyD2)

plot(p, AyD1, p, AyD2)
legend([AyD2, AyD2])
title('Vector potential of the dipole from z-axis to x-axis when D=2R and D=10R')
xlabel('Angle "phi" (p)')
ylabel('Magnitude of the vector potential of the dipole (uI*pi)')