import sys
import math

import sympy as sympy
import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sbn
from sympy import symbols
from sympy import Symbol


N=200
R=1
L=20*R
n=N/L

u= 1.25663706 * 10**(-6)
print("u=", u)

k= -u/(4*math.pi)
print("k=", k)

##DEFINING THE POSITION OF A POINT ON THE WIRE
#This is in cylindrical coordinates
# o is theta angle between the x-axis
# t is the time, ranging from t=0 to t=1
o,t = symbols('o,t')

r_Pos = np.array([R,400*math.pi*t,-20*R*t+10*R])
print(r_Pos)

##DEFINING THE PLACE WHERE WE WANT TO KNOW THE MAGNETIC FIELD
#This is in cylindrical coordinates
p_Pos = np.array([0,I,-1/10])