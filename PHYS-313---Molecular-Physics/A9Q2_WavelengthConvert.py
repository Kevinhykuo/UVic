import sympy as sym
from sympy import Symbol
from math import isclose

# Define constants and variables
a = 834.213
b = 240603.0
c = 1599.7
d = 130
e = 38.9

# Wavelengths in standard air to convert to vacuum wavenumber
nm_um = (10**(-9)) / (10**(-6)) # Convert from nm to micrometer
lambda_1 = 1138.121*nm_um
lambda_2 = 1140.355*nm_um
lambda_3 = 615.4225*nm_um
lambda_4 = 616.0747*nm_um
lambda_5 = 514.8838*nm_um
lambda_6 = 515.3402*nm_um

def F(lambda_SA):
    wn = Symbol('wn')
    n_b = (wn * lambda_SA) ** (-1)  # Index of refraction of standard air
    # Define the equation
    # NOTE: This equation only applies if wn is in per micrometer
    expr = (a + b / (d - wn ** 2) + c / (e - wn ** 2)) * 10 ** (-7) + 1 - n_b
    # Solve the equation for wavenumber
    WN = sym.solve(expr, wn)
    return(WN)

# Debug
print('===DEBUG===')
lambda_SA = (380*10**(-9)) # Standard air wavelength in m
wn_SA = (1/lambda_SA) # Standard air wavenumber in /m
print("Standard air wavelength: lambda_SA =", lambda_SA*100, "cm")
print("Standard air wavenumber: sigma_SA =", wn_SA*0.01, "per cm")
print("Vacuum wavenumber: lambda_0 = ", [i*10**4 for i in F(lambda_SA*10**6)], "per cm")
print("Vacuum wavenumber: lambda_0 = ", F(lambda_SA*10**6), "per micrometer")

# Above numbers should match these numbers
print('Correct vacuum wavenumber:     [-11.4026114293297, -6.23699546853199, 2.63083202582880, 6.23700862311110, 11.4031256848653] per micrometer')
# ....and it DOES NOT
print('===DEBUG END===')
print(' ')

print("Standard air wavenumber: k_1 =", 1/lambda_1, "per micrometer")
print("Standard air wavenumber: k_2 =", 1/lambda_2, "per micrometer")
print("Standard air wavenumber: k_3 =", 1/lambda_3, "per micrometer")
print("Standard air wavenumber: k_4 =", 1/lambda_4, "per micrometer")
print("Standard air wavenumber: k_5 =", 1/lambda_5, "per micrometer")
print("Standard air wavenumber: k_6 =", 1/lambda_6, "per micrometer")

print(' ')

wn1 = F(lambda_1)
wn2 = F(lambda_2)
wn3 = F(lambda_3)
wn4 = F(lambda_4)
wn5 = F(lambda_5)
wn6 = F(lambda_6)


print("Vacuum wavenumber: k_01 = ", wn1, "per micrometer")
print("Vacuum wavenumber: k_02 = ", wn2, "per micrometer")
print("Vacuum wavenumber: k_03 = ", wn3, "per micrometer")
print("Vacuum wavenumber: k_04 = ", wn4, "per micrometer")
print("Vacuum wavenumber: k_05 = ", wn5, "per micrometer")
print("Vacuum wavenumber: k_06 = ", wn6, "per micrometer")

print(' ')

print("Vacuum wavenumber: k_01 = ", [i*10**-(-6+2) for i in wn1], "per centimeter")
print("Vacuum wavenumber: k_02 = ", [i*10**-(-6+2) for i in wn2], "per centimeter")
print("Vacuum wavenumber: k_03 = ", [i*10**-(-6+2) for i in wn3], "per centimeter")
print("Vacuum wavenumber: k_04 = ", [i*10**-(-6+2) for i in wn4], "per centimeter")
print("Vacuum wavenumber: k_05 = ", [i*10**-(-6+2) for i in wn5], "per centimeter")
print("Vacuum wavenumber: k_06 = ", [i*10**-(-6+2) for i in wn6], "per centimeter")


print(' ')

print('Term value seperation (k_01 - k_02):', [i*10**-(-6+2) for i in wn1][2] - [i*10**-(-6+2) for i in wn2][2])
print('Term value seperation (k_03 - k_04):', [i*10**-(-6+2) for i in wn3][2] - [i*10**-(-6+2) for i in wn4][2])
print('Term value seperation (k_05 - k_06):', [i*10**-(-6+2) for i in wn5][2] - [i*10**-(-6+2) for i in wn6][2])

