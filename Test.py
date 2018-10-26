import scipy.integrate as integrate
import scipy.special as special
import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt, sin, cos, pi
from scipy.integrate import quad

'''
#Single Integral
print('Single Integral:')

#Bessel function
result = integrate.quad(lambda x: special.jv(2.5,x), 0, 4.5)
    #special.jv(2.5,x) calls the Bessel function J_2.5(x) as function of x
print(' Bessel function:', result)

#Defining a function (I)
I = sqrt(2/pi)*(18.0/27*sqrt(2)*cos(4.5) - 4.0/27*sqrt(2)*sin(4.5) + sqrt(2*pi) * special.fresnel(3/sqrt(pi))[0])
print(' ', I)
print(' ', abs(result[0]-I)) #Probably evaluating the Bessel function from 0 to I?

#Now defining an integral
def integrand(x, a, b):
    return a*x**2 + b #Function to be evaluated

a = 2
b = 1
I2 = quad(integrand, 0, 1, args=(a,b))
print(' Integral of 2x^2+1 frorm 0 to 1:', I2)


#Integral to infinity
from scipy.integrate import quad
def integrand(t, n, x):
    return np.exp(-x*t) / t**n #Note this function also depends on variable n

def expint(n, x):
    return quad(integrand, 1, np.inf, args=(n, x))[0]

vec_expint = np.vectorize(expint)

vec_expint(3, np.arange(1.0, 4.0, 0.5))

import scipy.special as special
special.expn(3, np.arange(1.0,4.0,0.5))

result = quad(lambda x: expint(3, x), 0, np.inf) #Do integral again with t from 0 to infinity
print(result)

I3 = 1.0/3.0 #Set n=3
print(I3)

print(' Integral of 1/3 - e^(-xt)t^(-n), where t=1, n=4, x=0.5:', I3 - result[0]) #The number in [] specifies the cell in the array
'''

# x = [i for i in range(10)]
# y = [i**2 for i in x]
#
# plt.figure(figsize=(1,2))
# plt.plot(x,y)
# plt.show()

from math import exp
from scipy.optimize import fsolve

x_guess = 1
y_guess = 2


def equations(p):
    x, y = p
    eq1 = x + y ** 2 - 4
    eq2 = exp(x) + x * y - 3
    return (eq1, eq2)


x, y = fsolve(equations, (x_guess, y_guess))

print ("x= ", x, "y = ", y)