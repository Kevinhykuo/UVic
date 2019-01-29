import sys

import sympy as sym
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import seaborn as sbn
from sympy import Integral, Symbol


'''
So, here's the plan. 
Get the code to do the integrals obtained in the calculations for various values of d.
(aka. The different radius of rings where we want to calculate the magnetic fields)
d=0, 0.1R, 0.2R 0.3R, 0.4R, 1.5R, 2.0R, 3.0R, 5.0R

Get the program to plot it out. 
Hope that it works.
Hope really hard that it works.
If it doesn't work, and another 'really' and repeat.
'''
#Defining the d's for inside the solenoid
d1 = 0.1
d2 = 0.2
d3 = 0.3
d4 = 0.4

#Defining the d's outside the solenoid
d5 = 1.5
d6 = 2.0
d7 = 3.0
d6 = 5.0
#Here we just let R=1, as we want a general graph of the magnetic field.

#Defining the Symbols and variables
I = Symbol('I') #The current through the wire
R = Symbol('R') #The radius of the coils
#o = Symbol('o') #The angle with respect to the x-axis (Theta)
t = Symbol('t') #Arbiruary 'time' to map the turn of the coils
w = 2*sym.pi*200 #The 'rate' the the coils turn
print('w=', w)


#Here are the different functions for the integrals in their general form
#Bx = -(R*sym.cos(10-20*t)+0.1*(R*sym.sin(w*t)-d*sym.sin(o)))/(R**2 + d**2 - 2*R*d*sym.cos(w*t-o))**1.5
#By = -(R*sym.sin(w*t)*(10-20*t)-0.1*(R*sym.sin(w*t)-d*sym.sin(o)))/(R**2 + d**2 -2*R*d*sym.cos(w*t-o))**1.5
#Bz = (R-d*sym.cos(w*t-o))/(R**2 + d**2 -2*R*d*sym.cos(w*t-o))**1.5

#Do the integrals for d=0

for o in (0, 2*sym.pi, 0.1*sym.pi): #Find field at angles of the ring from 0 to 2*pi
    Bx0R = -(sym.cos(10-20*t)+0.1*(sym.sin(w*t)-d1*sym.sin(o)))/(1 + d1**2 - 2*d1*sym.cos(w*t-o))**1.5
    By0R = -(sym.sin(w*t)*(10-20*t)-0.1*(sym.sin(w*t)-d1*sym.sin(o)))/(1 + d1**2 -2*d1*sym.cos(w*t-o))**1.5
    Bz0R = (1-d1*sym.cos(w*t-o))/(1 + d1**2 -2*d1*sym.cos(w*t-o))**1.5

    Integral(Bx0R, (t, 0, 1)).doit()
    Integral(By0R, (t, 0, 1)).doit()
    Integral(Bz0R, (t, 0, 1)).doit()

'''
#Print some values to make sure the code works. For testing.
#Spoilers: It works, the code is good, but my computer can't handle it.
print("Bx0R = u*I/(4*pi) 401^(1/2) R", )
print("By0R = u*I/(4*pi) 401^(1/2) R", )
print("Bz0R = u*I/(4*pi) 401^(1/2) R", )
'''

#Plot it out
plot(o, Bx0R, o, By0R, o, Bz0R)
legend([Bx0R, By0R, Bz0R])
title('Magnitude of magnetic field at points in the ring of radius = 0 in xy-plane')
xlabel('Points in the ring corresponding to angle "theta" (o)')
ylabel('Magnitude of each vectors of the magnetic field')

'''
Now I would repeat the above process for the different values of 'd'.
All I need to do is swap out d1 with the differnt 'd's, then change the names a bit and plot everything out. 
Rinse and repeat for all values of 'd'. 
'''
