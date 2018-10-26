import numpy as np
import scipy as sci
import sympy as sym
import matplotlib.pyplot as plt
from math import pi
from scipy.constants import *
from scipy.optimize import fsolve

sym.init_printing(use_latex='mathjax')

# Conversions
AMUtoKg = 1 / (Avogadro * 1000)
h_ev = physical_constants['Planck constant in eV s'][0]

# In[]
# Constants
print('Speed of light         :    c = ', c, 's')
print('Boltzmann`s constant   :    k = ', k, 'J/K')
print('Plank`s constant       :    h = ', h, 'Js')
print('                         hbar = ', hbar, 'Js')
print('Planck constant in eV  :    h = ', h_ev, 'eV')
print('Avogadro`s number      :   NA = ', Avogadro, 'mole^-1')
print('Amu to kg              :  amu = ', u, 'kg')
print(' ')

# In[]
# ==========
# Question 1
# ==========
print('Question 1: \n===========')
TermVal = [655686, 659883, 666100, 674279, 684300]

i = 0
Jdiff = []
while i <= len(TermVal) - 2:
    TermDiff = abs(TermVal[i + 1] - TermVal[i]) / (i + 2)
    Jdiff.append(TermDiff)
    i += 1

print('Lande Interval =', Jdiff)


def E(T1=0, T2=4):
    diff = TermVal[T2] - TermVal[T1]
    a = 2 * diff / ((T2 + 1) * (T2 + 2) - (T1 + 1) * (T1 + 2))
    return(a)


print('a =', E(0, 4), 'or', E(0, 4) * h_ev * c, 'eV')

print(' ')

# In[]
# ==========
# Question 2
# ==========
print('Question 2: \n===========')


def RM(m1, m2):  # Reduced mass
    rm = (m1 * m2) / (m2 + m2)
    return(rm)


def r2(J_max=11, m1=12, m2=16, T=740):
    r2 = (hbar / 4) * (((4 * J_max + 1)**2 - 1) /
                       (RM(m1 * u, m2 * u) * k * T))**0.5
    return(r2)


print('r = ', r2())
print(' ')

# In[]
# ==========
# Question 5
# ==========
print('Question 5: \n===========')
# The masses in atomic mass units
m15 = 14
m25 = 14

# Define the functions for the periods


def P(m1=14, m2=14, r=1.09e-10, K=2.3e3, T=300):
    I = RM(m1 * u, m2 * u) * r**2
    p_rot = 2 * pi * (I / (2 * k * T))**0.5
    p_vib = 2 * pi * (RM(m1 * u, m2 * u) / K)**0.5
    return(p_rot, p_vib)


# Part(a):
print('P_rot:', P(m15, m25)[0])

# Part (b):
print('P_vib:', P(m15, m25)[1])

# Part(c):
print('Ratios:', P(m15, m25)[0] / P(m15, m25)[1])

print(' ')

# In[]
# ==========
# Question 6
# ==========
print('Question 6: \n===========')
# Define the masses in AMU
M1 = [16, 12, 32, 9.56]
M2 = [18, 12, 32, 10.16]

# Define Function


def I(m1, m2, m3, Inertia, x, y):
    mT = m1 + m2 + m3
    a = m1 * (m2 + m3) / mT
    b = m3 * (m1 + m2) / mT
    h = m1 * m3 / mT
    f = a * x**2 + 2 * h * x * y + b * y**2 - Inertia
    return(f, a, 2 * h, b, Inertia)

# def coeff(m1, m2, m3):
#     mT = m1 + m2 + m3
#     a = m1*(m2+m3)/mT
#     b = m3*(m1+m2)/mT
#     h = m1*m3/mT
#     return(a, 2*h, b)

# Compare the coefficients for debugging
# print(I(M1[0], M1[1], M1[2], M1[3], 1, 1)[1:])
# print(coeff(M1[0], M1[1], M1[2]))
# print(I(M2[0], M2[1], M2[2], M2[3], 1, 1)[1:])
# print(coeff(M2[0], M2[1], M2[2]))


C1 = I(M1[0], M1[1], M1[2], M1[3], 1, 1)[1:]
C2 = I(M2[0], M2[1], M2[2], M2[3], 1, 1)[1:]
print('Functions: ')
print(C1[3], ' = ', C1[0], 'x^2 + ', C1[1], 'xy + ', C1[2], 'y^2')
print(C2[3], ' = ', C2[0], 'x^2 + ', C2[1], 'xy + ', C2[2], 'y^2')
print(' ')

# Solve the functions


def Eqn(p):
    x, y = p
    eq1 = I(M1[0], M1[1], M1[2], M1[3], x, y)[0]
    eq2 = I(M2[0], M2[1], M2[2], M2[3], x, y)[0]
    return (eq1, eq2)


x1, y1 = fsolve(Eqn, (1, 1))
x2, y2 = fsolve(Eqn, (-1, 1))
x3, y3 = fsolve(Eqn, (-1, -1))
x4, y4 = fsolve(Eqn, (1, -1))

print("Solutions: \n ", x1, y1, '\n', x2, y2, '\n', x3, y3, '\n ', x4, y4)

# x = np.linspace(-1.5, 1.5, 100)
# plt.plot(x, Eqn[0], label=Eq1)
# plt.plot(x, Eqn[1], label=Eq2)
# plt.legend()
# plt.show()
