import sys
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, exp, sin, arccos, cos
from scipy.special import eval_legendre
from scipy.integrate import quad

A1 = []  # Create the A1 array for error checking
A2 = []  # Create the A2 array for error checking
Ab = []  # Create the Ab array for error checking
F1 = 0  # Define a F1 as zero, so it can be looped
F2 = 0  # Define a F2 as zero, so it can be looped

# Define x as variable going from -1 to 1 in steps of 1000
x = np.linspace(-1, 1, 1000)
g = x * exp(x) - arccos(x)  # Define g for comparison

i = 0

# Commense the while loop!
while i <= 10:  # To get a0 to a10. Upper limit 126
    #===========
    # Part (a)
    #===========
    # Define the funcitons
    def Ia1(x):
        return((x * exp(x) - arccos(x)) * sin(i * pi * x))

    def Ia3(x):
        return((x * exp(x) - arccos(x)) * cos((i + 0.5) * pi * x))

    # Integrate the funcitons
    ta1 = quad(Ia1, -1, 1)
    ta2 = quad(Ia3, -1, 1)

    #===========
    # Part (b)
    #===========
    # Define the functions
    def Ib1(x):
        return((x * exp(x) - arccos(x)) * eval_legendre(i, x))

    # Intergrate the functions
    tb1 = quad(Ib1, -1, 1)

    #=====================
    # Finding Coefficients
    #=====================
    # Calculate the coefficients
    aa1 = ta1[0]
    aa2 = ta2[0]
    ab1 = ((2 * i + 1) / 2) * tb1[0]

    A1.append(aa1)  # Record the values of aa1 into the array A1
    A2.append(aa2)  # Record the values of aa2 into the array A2
    Ab.append(ab1)  # Record the values of ab1 into the array Ab

    # Sum up the functions to find the solutions
    F1 = F1 + aa1 * sin(i * pi * x) + aa2 * cos((i + 0.5) * pi * x)
    F2 = F2 + ab1 * eval_legendre(i, x)

    i += 1

# Printing values for debugging
print('Coefficients for Part (a):')
print('ai:', A1)  # For debugging
print('bi:', A2)  # For debugging
print('')
print('Coefficients for Part (b)')
print('ai:', Ab)
print('')
print('g(x) values:')
print(g)
print('')
print('Part (a) series values:')
print(F1)
print('')
print('Part (b) series values:')
print(F2)

#=================
# Plotting time!!!
#=================
# Plot it all out
plt.plot(x, g, 'g')
plt.plot(x, F1)
# plt.plot(x, F2, '--')

# Label the axis and add title
plt.legend('gab')
plt.title(r'Comparison between g(x) and approximations of g(x)', fontsize=16)
plt.xlabel(r' $x$ ', fontsize=14)
plt.ylabel(r' $g(x)$ ', fontsize=14)
plt.xlim(-1, 1)
plt.ylim(-4, 4)
plt.show()
