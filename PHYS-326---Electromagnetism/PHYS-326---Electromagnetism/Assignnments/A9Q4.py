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
z2 = Symbol('z2') #It's z'

#The coordinates of the origin for part (a)
xa = 0
ya = 0
za = 0

#The coordinates for part (b)
xb = 0
yb = 0
zb = 10*R

#The coordinates fo part (c)
xc = 6*R
yc = 0
zc = 0

#Coordinates for finite distance approximation for part (a)
dxa = xa + 0.0001
dya = ya + 0.0001
dza = za + 0.0001

#Coordinates for finite distance approximation for part (b)
dxb = xb + 0.0001
dyb = yb + 0.0001
dzb = zb + 0.0001

#Coordinates for finite distance approximation for part (c)
dxc = xc + 0.0001
dyc = yc + 0.0001
dzc = zc + 0.0001

#Defining the functions for the integrals for part (a)
axa = -sym.sin(u) / ( (R*sym.cos(u) - xa)**2 + (R*sym.sin(u) - ya)**2 - (z2-za)**2)**0.5
aya = sym.cos(u) / ( (R*sym.cos(u) - xa)**2 + (R*sym.sin(u) - ya)**2 - (z2-za)**2)**0.5

Axa = Integral(axa, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit() #Double integral of Ax with respect to z' and theta
Aya = Integral(aya, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit() #Double integral of Ay with respect to z' and theta

#Defining the functions for dx in part (a)
axadx = -sym.sin(u) / ( (R*sym.cos(u) - dxa)**2 + (R*sym.sin(u) - ya)**2 - (z2-za)**2)**0.5
ayadx = sym.cos(u) / ( (R*sym.cos(u) - dxa)**2 + (R*sym.sin(u) - ya)**2 - (z2-za)**2)**0.5

Axadx = Integral(axadx, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()
Ayadx = Integral(ayadx, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()

#Defining the functions for dy in part (a)
axady = -sym.sin(u) / ( (R*sym.cos(u) - xa)**2 + (R*sym.sin(u) - dya)**2 - (z2-za)**2)**0.5
ayady = sym.cos(u) / ( (R*sym.cos(u) - xa)**2 + (R*sym.sin(u) - dya)**2 - (z2-za)**2)**0.5

Axady = Integral(axady, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()
Ayady = Integral(ayady, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()

#Defining the functions for dz in part (a)
axadz = -sym.sin(u) / ( (R*sym.cos(u) - xa)**2 + (R*sym.sin(u) - ya)**2 - (z2-dza)**2)**0.5
ayadz = sym.cos(u) / ( (R*sym.cos(u) - xa)**2 + (R*sym.sin(u) - ya)**2 - (z2-dza)**2)**0.5

Axadz = Integral(axadz, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()
Ayadz = Integral(ayadz, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()

#Defining the B-field in part (a)
Bxa = (Ayadz - Aya)/dza
Bya = (Axadz - Axa)/dza
Bza = (Ayadx - Aya)/dxa - (Axady - Axa)/dya

print('Part (a):')
print("Bx = (uI / 4*.pi)*", Bxa)
print("By = (uI / 4*.pi)*", Bya)
print("Bz = (uI / 4*.pi)*", Bza)


#Defining the functions for the integrals for part (b)
axb = -sym.sin(u) / ( (R*sym.cos(u) - xb)**2 + (R*sym.sin(u) - yb)**2 - (z2-zb)**2)**0.5
ayb = sym.cos(u) / ( (R*sym.cos(u) - xb)**2 + (R*sym.sin(u) - yb)**2 - (z2-zb)**2)**0.5

Axb = Integral(axb, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()

Ayb = Integral(ayb, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()

#Defining the functions for dx in part (b)
axbdx = -sym.sin(u) / ( (R*sym.cos(u) - dxb)**2 + (R*sym.sin(u) - yb)**2 - (z2-zb)**2)**0.5
aybdx = sym.cos(u) / ( (R*sym.cos(u) - dxb)**2 + (R*sym.sin(u) - yb)**2 - (z2-zb)**2)**0.5

Axbdx = Integral(axbdx, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()
Aybdx = Integral(aybdx, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()

#Defining the functions for dy in part (b)
axbdy = -sym.sin(u) / ( (R*sym.cos(u) - xb)**2 + (R*sym.sin(u) - dyb)**2 - (z2-zb)**2)**0.5
aybdy = sym.cos(u) / ( (R*sym.cos(u) - xb)**2 + (R*sym.sin(u) - dyb)**2 - (z2-zb)**2)**0.5

Axbdy = Integral(axbdy, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()
Aybdy = Integral(aybdy, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()

#Defining the functions for dz in part (b)
axbdz = -sym.sin(u) / ( (R*sym.cos(u) - xb)**2 + (R*sym.sin(u) - yb)**2 - (z2-dzb)**2)**0.5
aybdz = sym.cos(u) / ( (R*sym.cos(u) - xb)**2 + (R*sym.sin(u) - yb)**2 - (z2-dzb)**2)**0.5

Axbdz = Integral(axbdz, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()
Aybdz = Integral(aybdz, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()

#Defining the B-field in part (b)
Bxb = (Aybdz - Ayb)/dzb
Byb = (Axbdz - Axb)/dzb
Bzb = (Aybdx - Ayb)/dxb - (Axbdy - Axb)/dyb

print('Part (b):')
print("Bx = (uI / 4*.pi)*", Bxb)
print("By = (uI / 4*.pi)*", Byb)
print("Bz = (uI / 4*.pi)*", Bzb)

#Defining the functions for the integrals for part (c)
axc = -sym.sin(u) / ( (R*sym.cos(u) - xc)**2 + (R*sym.sin(u) - yc)**2 - (z2-zc)**2)**0.5
ayc = sym.cos(u) / ( (R*sym.cos(u) - xc)**2 + (R*sym.sin(u) - yc)**2 - (z2-zc)**2)**0.5

Axc = Integral(axc, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()
Ayc = Integral(ayc, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()

#Defining the functions for dx in part (c)
axcdx = -sym.sin(u) / ( (R*sym.cos(u) - dxc)**2 + (R*sym.sin(u) - yc)**2 - (z2-zc)**2)**0.5
aycdx = sym.cos(u) / ( (R*sym.cos(u) - dxc)**2 + (R*sym.sin(u) - yc)**2 - (z2-zc)**2)**0.5

Axcdx = Integral(axcdx, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()
Aycdx = Integral(aycdx, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()

#Defining the functions for dy in part (c)
axcdy = -sym.sin(u) / ( (R*sym.cos(u) - xc)**2 + (R*sym.sin(u) - dyc)**2 - (z2-zc)**2)**0.5
aycdy = sym.cos(u) / ( (R*sym.cos(u) - xc)**2 + (R*sym.sin(u) - dyc)**2 - (z2-zc)**2)**0.5

Axcdy = Integral(axcdy, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()
Aycdy = Integral(aycdy, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()

#Defining the functions for dz in part (c)
axcdz = -sym.sin(u) / ( (R*sym.cos(u) - xc)**2 + (R*sym.sin(u) - yc)**2 - (z2-dzc)**2)**0.5
aycdz = sym.cos(u) / ( (R*sym.cos(u) - xc)**2 + (R*sym.sin(u) - yc)**2 - (z2-dzc)**2)**0.5

Axcdz = Integral(axcdz, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()
Aycdz = Integral(aycdz, (z2, -10*R, 10*R), (u, 0, sym.pi*2)).doit()

#Defining the B-field in part (b)
Bxc = (Aycdz - Ayc)/dzc
Byc = (Axcdz - Axc)/dzc
Bzc = (Aycdx - Ayc)/dxc - (Axcdy - Axc)/dyc

print('Part (c):')
print("Bx = (uI / 4*.pi)*", Bxc)
print("By = (uI / 4*.pi)*", Byc)
print("Bz = (uI / 4*.pi)*", Bzc)
