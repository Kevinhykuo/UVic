import sys

import sympy as sym
import numpy as np
import scipy as sci
from sympy import Symbol

#Define constants and variables
a = 834.213
b = 240603.0
c = 1599.7
d = 130
e = 38.9

n_SA = Symbol('n_SA') #Index of refraction of standard air
sigma_0 = Symbol('sigma_0') #Wavenumber in vacuum

#Defining the equation for refractive index of standard air
n = (a + b/(d-sigma_0**2) + c/(e-sigma_0**2))*10**(-7) + 1

# #========
# #Part (a)
# #========
# #Defining the constants and variables
# sigma_0a = 22000 / (10**4) #Vacuum wavenumber. Converted from cm^(-1) to micrometer^(-1)
# n_a = (a + b/(d-sigma_0a**2) + c/(e-sigma_0a**2))*10**(-7) + 1
#
# #Finding wavelengith in vacuum
# #Wavelength is just inverse wavenumber
# lambda_0a = sigma_0a**(-1) * 10**3 #Convert from wavenumber to wavelength while also converting from micrometer to nanometer.
#
# #Finding wavelength in air
# lambda_SAa = lambda_0a/n_a
#
# #Print the answer
# print('Part (a):')
# print("Index of refraction of standard air: n_SA = ", n_a)
# print("Wavenumber in vacuum: sigma_0 = ", sigma_0a, "per micrometer")
# print("Wavelength in standard air: lambda_SA = ", round(lambda_SAa, 3), "nm")
# print("Wavelength in vacuum: lambda_0 = ", round(lambda_0a, 3), "nm")
# print( )

#========
#Part (b)
#========
#Defining the constants and variables
lambda_SAb = 380*10**(-3) #Wavelength in standard air. In micrometer
x = Symbol('x')  #x is the vacuum wavenumber (sigma_0) in per micrometer
n_b = (x*lambda_SAb)**(-1) #Index of refraction of standard air

#Define the equation
expr = (a + b/(d-x**2) + c/(e-x**2))*10**(-7) + 1 - n_b

#Solve the equation for x
sigma_0b = sym.solve(expr, x)

#Print the answer
print("Part (b):")
print("Standard air wavelength: lambda_SA =", lambda_SAb, "micrometer")
print("Standard air wavenumber: sigma_SA =", round(lambda_SAb**(-1), 5), "per micrometer = ", round(lambda_SAb**(-1), 5)*10**4, "per cm")
print("Vacuum wavenumber: sigma_0 = ", sigma_0b, "per micrometer")