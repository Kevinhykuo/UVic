import sys

import sympy as sym
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import seaborn as sbn
from sympy import Integral, Symbol

#Define the symbols
R = 1
u = Symbol('u') #The angle theta (with respect to x-axis)
z2 = Symbol('z2') #This is z'
r = Symbol('r')

#Define the intresting points
#Right now I've set these at the origin
#I could change them to whatever point I want by changing the values
x = 0
y = 0
z = 0

#Define the dx, dy, dz for finite difference approximation
dx = x + 0.0001
dy = y + 0.0001
dz = z + 0.0001

#Define the integrals for part (a)
ax1 = (-R*sym.sin(u)-y) / ((R*sym.cos(u)-x)**2 + (R*sym.sin(u)-y)**2 + (z2-z)**2)**1.5
ay1 = (R*sym.cos(u)-x) / ((R*sym.cos(u)-x)**2 + (R*sym.sin(u)-y)**2 + (z2-z)**2)**1.5

Ax1 = Integral(ax1*r, (r, 0, R), (u, 0, 2*sym.pi), (z2, -R, R)).doit()
Ay1 = Integral(ay1*r, (r, 0, R), (u, 0, 2*sym.pi), (z2, -R, R)).doit()

#Define functions for dx in part (a)
ax1dx = (-R*sym.sin(u)-y) / ((R*sym.cos(u)-dx)**2 + (R*sym.sin(u)-y)**2 + (z2-z)**2)**1.5
ay1dx = (R*sym.cos(u)-dx) / ((R*sym.cos(u)-dx)**2 + (R*sym.sin(u)-y)**2 + (z2-z)**2)**1.5

Ax1dx = Integral(ax1dx*r, (r, 0, R), (u, 0, 2*sym.pi), (z2, -R, R)).doit()
Ay1dx = Integral(ay1dx*r, (r, 0, R), (u, 0, 2*sym.pi), (z2, -R, R)).doit()

#Define functions for dy in part (a)
ax1dy = (-R*sym.sin(u)-dy) / ((R*sym.cos(u)-x)**2 + (R*sym.sin(u)-dy)**2 + (z2-z)**2)**1.5
ay1dy = (R*sym.cos(u)-x) / ((R*sym.cos(u)-x)**2 + (R*sym.sin(u)-dy)**2 + (z2-z)**2)**1.5

Ax1dy = Integral(ax1dy*r, (r, 0, R), (u, 0, 2*sym.pi), (z2, -R, R)).doit()
Ay1dy = Integral(ay1dy*r, (r, 0, R), (u, 0, 2*sym.pi), (z2, -R, R)).doit()

#Define functions for dz in part (a)
ax1dz = (-R*sym.sin(u)-y) / ((R*sym.cos(u)-x)**2 + (R*sym.sin(u)-y)**2 + (z2-dz)**2)**1.5
ay1dz = (R*sym.cos(u)-x) / ((R*sym.cos(u)-x)**2 + (R*sym.sin(u)-y)**2 + (z2-dz)**2)**1.5

Ax1dz = Integral(ax1dz*r, (r, 0, R), (u, 0, 2*sym.pi), (z2, -R, R)).doit()
Ay1dz = Integral(ay1dz*r, (r, 0, R), (u, 0, 2*sym.pi), (z2, -R, R)).doit()

#Defining the B-field for part (a)
Bx1 = (Ay1dz - Ay1)/dz
By1 = (Ax1dz - Ax1)/dz
Bz1 = (Ay1dx - Ay1)/dx - (Ax1dy - Ax1)/dy

print('For part (a):')
print("Bx1 = (uM / 4*.pi)*", Bx1)
print("By1 = (uM / 4*.pi)*", By1)
print("Bz1 = (uM / 4*.pi)*", Bz1)


#Define the integrals for part (b)
ax2 = (-R*sym.sin(u)) / ((R*sym.cos(u)-x)**2 + (R*sym.sin(u)-y)**2 + (z2-z)**2)**0.5
ay2 = (R*sym.cos(u)) / ((R*sym.cos(u)-x)**2 + (R*sym.sin(u)-y)**2 + (z2-z)**2)**0.5

Ax2 = Integral(ax2*r, (u, 0, 2*sym.pi), (z2, -R, R)).doit()
Ay2 = Integral(ay2*r, (u, 0, 2*sym.pi), (z2, -R, R)).doit()

#Define functions for dx in part (b)
ax2dx = (-R*sym.sin(u)) / ((R*sym.cos(u)-dx)**2 + (R*sym.sin(u)-y)**2 + (z2-z)**2)**0.5
ay2dx = (R*sym.cos(u)) / ((R*sym.cos(u)-dx)**2 + (R*sym.sin(u)-y)**2 + (z2-z)**2)**0.5

Ax2dx = Integral(ax2dx*r, (u, 0, 2*sym.pi), (z2, -R, R)).doit()
Ay2dx = Integral(ay2dx*r, (u, 0, 2*sym.pi), (z2, -R, R)).doit()

#Define functions for dy in part (b)
ax2dy = (-R*sym.sin(u)) / ((R*sym.cos(u)-x)**2 + (R*sym.sin(u)-dy)**2 + (z2-z)**2)**0.5
ay2dy = (R*sym.cos(u)) / ((R*sym.cos(u)-x)**2 + (R*sym.sin(u)-dy)**2 + (z2-z)**2)**0.5

Ax2dy = Integral(ax2dy*r, (u, 0, 2*sym.pi), (z2, -R, R)).doit()
Ay2dy = Integral(ay2dy*r, (u, 0, 2*sym.pi), (z2, -R, R)).doit()

#Define functions for dz in part (b)
ax2dz = (-R*sym.sin(u)) / ((R*sym.cos(u)-x)**2 + (R*sym.sin(u)-y)**2 + (z2-dz)**2)**0.5
ay2dz = (R*sym.cos(u)) / ((R*sym.cos(u)-x)**2 + (R*sym.sin(u)-y)**2 + (z2-dz)**2)**0.5

Ax2dz = Integral(ax2dz*r, (u, 0, 2*sym.pi), (z2, -R, R)).doit()
Ay2dz = Integral(ay2dz*r, (u, 0, 2*sym.pi), (z2, -R, R)).doit()

#Defining the B-field for part (b)
Bx2 = (Ay2dz - Ay2)/dz
By2 = (Ax2dz - Ax2)/dz
Bz2 = (Ay2dx - Ay2)/dx - (Ax2dy - Ax2)/dy

print('For part (b):')
print("Bx2 = (uM / 4*.pi)*", Bx2)
print("By2 = (uM / 4*.pi)*", By2)
print("Bz2 = (uM / 4*.pi)*", Bz2)
