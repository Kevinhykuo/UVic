import sys

import sympy as sym
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import seaborn as sbn
from sympy import Integral, Symbol
#from pylab import plot, show, title, xlabel, ylabel, legend

#Define the Ds'
D1 = 2
D2 = 10

# HERE COMES THE DIPOLES!!!


# For D=2R and D=10R
#Field = []
#Field2 = []

def generate_AxD1_p():
    p = range(0, sym.pi/2, 0.05*sym.py)
    F = []

for dist in p:
    AyD1 = R * R * sym.sin(p) / (R * D1)  # D=2R
    F.append(AyD1)

draw_graph(p,F)

'''
for p in (0, sym.pi/2, 0.1 * sym.pi):
    AyD1 = R*R*sym.sin(p) / (R*D1) #D=2R
    Field.append(AyD1)
    AyD2 = R*R*sym.sin(p) / (R*D2) #D=10R
    Field2.append(AyD2)
'''
plt.plot(p, Field, p, Field2)
plt.legend([Field, Field2])
plt.title('Vector potential of the dipole from z-axis to x-axis when D=2R and D=10R')
plt.xlabel('Angle "phi" (p)')
plt.ylabel('Magnitude of the vector potential of the dipole (uI*pi)')
plt.show()