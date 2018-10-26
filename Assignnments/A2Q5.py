import sys
import math
import numpy as np
import scipy as sp

from scipy.integrate import quad

def vx(u):
    return a - a*math.asin(u)

def vy(u):
    return a + math.acos(u)

def vz(u):
    return a*u

def r(u):
    return sqrt(vx**2 + vy**2 + vz**2)

def fx(u):
    return (1/k)*(1/r**2)*vx/(r)

def fy(u):
    return (1/k)*(1/r**2)*vy/(r)

def fz(u):
    return (1/k)*(1/r**2)*vz/(r)

def Ix(u, a, k):
    return quad(fx, -4*math.pi, 0, args=(a, k)

def Iy(u, a, k):
    return quad(fy, -4*math.pi, 0, args=(a, k))

def Iz(u, a, k):
    return quad(fz, -4*math.pi, 0, args=(a, k)

print("Electric field is", Ix, Iy, Iz)