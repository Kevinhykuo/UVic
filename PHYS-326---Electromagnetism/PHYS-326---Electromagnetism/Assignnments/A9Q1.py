import sys

import sympy as sym
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import seaborn as sbn
from sympy import Integral, Symbol

#Defining constants and variables
R = 1 #Let R = 1, so this essentially becomes a unit.
u = Symbol('u') #Angle theta

#The position of the line
x2 = Symbol('x2')
y2 = 0
z2 = 0

#The coordinates of the origin
x = 0
y = 0
z = 0

#Coordinates for finite distance approximation
dx = x + 0.0001
dy = y + 0.0001
dz = z + 0.0001

#Defining the functions for the integrals
ax1 = -sym.sin(u) / ( (2*R*sym.cos(u)-x)**2 + (2*R*sym.sin(u)-y)**2 +(z2-z)**2 )**(0.5) #For the curved part
ax2 = ( (x2-x)**2 + (y2-y)*2 + (z2-z)**2 )**(-1) #For the linear part

Ax1 = Integral(ax1, (u, sym.pi/6, 5*sym.pi/6)).doit()
Ax2 = Integral(ax2, (x2, -(3**0.5)*R, (3**0.5)*R)).doit()
Ax = Ax1 + Ax2

ay1 = sym.cos(u) / ( (2*R*sym.cos(u)-x)**2 + (2*R*sym.sin(u)-y)**2 +(z2-z)**2 )**(0.5) #For the curved part

Ay = Integral(ay1, (u, sym.pi/6, 5*sym.pi/6)).doit()

#Defining the functions for the integrals for dx
ax1dx = -sym.sin(u) / ( (2*R*sym.cos(u)-dx)**2 + (2*R*sym.sin(u)-y)**2 +(z2-z)**2 )**(0.5) #For the curved part
ax2dx = ( (x2-dx)**2 + (y2-y)*2 + (z2-z)**2 )**(-1) #For the linear part

Ax1dx = Integral(ax1dx, (u, sym.pi/6, 5*sym.pi/6)).doit()
Ax2dx = Integral(ax2dx, (x2, -(3**0.5)*R, (3**0.5)*R)).doit()
Axdx = Ax1dx + Ax2dx

ay1dx = sym.cos(u) / ( (2*R*sym.cos(u)-dx)**2 + (2*R*sym.sin(u)-y)**2 +(z2-z)**2 )**(0.5) #For the curved part

Aydx = Integral(ay1dx, (u, sym.pi/6, 5*sym.pi/6)).doit()

#Defining functions for dy
ax1dy = -sym.sin(u) / ( (2*R*sym.cos(u)-x)**2 + (2*R*sym.sin(u)-dy)**2 +(z2-z)**2 )**(0.5) #For the curved part
ax2dy = ( (x2-x)**2 + (y2-dy)*2 + (z2-z)**2 )**(-1) #For the linear part

Ax1dy = Integral(ax1dy, (u, sym.pi/6, 5*sym.pi/6)).doit()
Ax2dy = Integral(ax2dy, (x2, -(3**0.5)*R, (3**0.5)*R)).doit()
Axdy = Ax1dy + Ax2dy

ay1dy = sym.cos(u) / ( (2*R*sym.cos(u)-x)**2 + (2*R*sym.sin(u)-dy)**2 +(z2-z)**2 )**(0.5) #For the curved part

Aydy = Integral(ay1dy, (u, sym.pi/6, 5*sym.pi/6)).doit()

#Defining functions for dz
ax1dz = -sym.sin(u) / ( (2*R*sym.cos(u)-x)**2 + (2*R*sym.sin(u)-y)**2 +(z2-dz)**2 )**(0.5) #For the curved part
ax2dz = ( (x2-x)**2 + (y2-y)*2 + (z2-dz)**2 )**(-1) #For the linear part

Ax1dz = Integral(ax1dz, (u, sym.pi/6, 5*sym.pi/6)).doit()
Ax2dz = Integral(ax2dz, (x2, -(3**0.5)*R, (3**0.5)*R)).doit()
Axdz = Ax1dz + Ax2dz

ay1dz = sym.cos(u) / ( (2*R*sym.cos(u)-x)**2 + (2*R*sym.sin(u)-y)**2 +(z2-dz)**2 )**(0.5) #For the curved part

Aydz = Integral(ay1dz, (u, sym.pi/6, 5*sym.pi/6)).doit()


#Defining the B-field
Bx = (Aydz - Ay)/dz
By = (Axdz - Ax)/dz
Bz = (Aydx - Ay)/dx - (Axdy - Ax)/dy

print("Bx = (uI / 4*.pi)*", Bx)
print("By = (uI / 4*.pi)*", By)
print("Bz = (uI / 4*.pi)*", Bz)


