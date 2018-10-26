import sys
import math as m
from sympy import Symbol
from sympy.physics.mechanics import Lagrangian, LagrangesMethod, dynamicsymbols
from math import sin, cos

# Define the constants
m = Symbol('m')
g = Symbol('g')
l = Symbol('l')

# Define the symbols
t = Symbol('t')
the1, the2, phi1, phi2 = dynamicsymbols('the1 the2 ph1, ph2')
the1d, the2d, phi1d, phi2d = dynamicsymbols('the1d the2d phi1d phi2d', 1)

# Define the kinetic energies (T) and the potential (V)
T1 = 2*the1d**2 + the2d**2 + 2*(phi1d*sin(the1))**2 + (phi2d*sin(the2))**2 + 2*the1d*the2d*sin(the1-the2)
T2 = 2*the1d*the2d*cos(the1)*cos(the2)*cos(phi1-phi2)
T3 = 2*the1d*phi2d*cos(the1)*sin(the2)*sin(phi1+phi2)
T4 = -2*phi1d*the2d*sin(the1)*cos(the2)*sin(phi1+phi2)
T5 = 2*phi1d*phi2d*sin(the1)*sin(the2)*cos(phi1-phi2)
V1 = m*g*l*(2*cos(the1) + cos(the2))

# Define the Lagrangian
L = 0.5*m*l*( T1+T2+T3+T4+T5 ) + V1
LM = LagrangesMethod(L, [the1, phi1, the2, phi2])

# The equations of motions
mechanics_printing(pretty_print = False)
LM.form_lagranges_equations()
