import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, pi
from scipy.special import eval_legendre

# =====================================
# WARNING!!!
# =====================================
# DOES NOT CONTAIN GENERAL WAVEFUNCTION
# ONLY PART OF WAVEFUNCTION
# ONLY POLAR COMPONTENT
# =====================================

# Define the quantum numbers
l = 2 #For d electron
m = 0
z = 1 #For hydrogen

# Define parameters to be evaluated
i = 0               #Starting point
f = 2*pi            #End point (in radians)
f2 = f * 180/pi     #Converts radians to degrees
am = f2*3600        #Converts degrees to arcminute
ss = 10             #Steps to take per arcminute
s = am*10           #How many total steps to take

theta = np.linspace(i, f, s) #Generate values of theta

# Define the meridional part of the wavefunction
# def THETA(theta):
#     return( (sin(theta))**abs(m) * (eval_legendre(l, cos(theta)) )

# Define a function for the probability amplitude
def WF_THETA(theta):
    return(( (sin(theta))**abs(m) * (eval_legendre(l, cos(theta)) )**2)

# Define a function for the probability amplitude
def WF_THETA(theta):
    return( ((sin(theta))**abs(m) * (eval_legendre(l, cos(theta)))**2) )

# def WF_THETA(theta): Hard code version
#     return( (1/2 * (3*cos(theta)**2 -1) )**2 )

# Calculate probability at an angle
theta90 = WF_THETA(90) #Calculate the probability at 90 degrees
theta00 = WF_THETA(0)  #Calculate the probability at 0 degrees

# Print it out
print('Probability at 90 degrees:', theta90)
print('Probability at 0 degrees:', theta00)
print('Ratio of probablility at 90 degrees and 0 degrees:',theta90/theta00)

# Plot it out
ax = plt.subplot(projection='polar') #Use polar coordinates
ax.plot(theta, WF_THETA(theta))

#Find values where theta is very small (almost = 0)
#d = (np.where(WF_THETA(theta) <= 10**(-13))[0]) * f2/s

# print('Angles where possibility is near zero:')
d = (np.where(WF_THETA(theta) <= 10**(-13))[0])
# while i <= len(d)-1:
#     y2 = WF_THETA(theta)[d[i]]
#     print(y2)
#     i += 1
# print(d)

print(' ')
print('Angles where possibility is near 0 (arcminute):')
print(d/ss)
print(' ')
print('Angles where possibility is near 0 (degrees):')
print((d/ss)/3600) #Convert to arcminuite (1 degree = 3600 arcminuite)
print(' ')
print('Angles where possibility is near 0 (radians):')
print( ((d/ss)/3600)/180, 'pi' )


plt.show()
