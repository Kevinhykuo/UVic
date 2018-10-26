import sys
import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, arctan

#Define the constants and variables
#beta = Symbol('beta')
beta = np.linspace(0,1.5,100) #beta from 0 to 1.5 in steps of 100

#Define the function
a = arctan(2*beta)
top = 2*(beta**2)
#bottom = (cos(a) + 2*beta*sin(a) - 1) #Here for redundancy test.
bottom = (cos(a) * (1+4*(beta**2)) - 1)
r_min = top/bottom

#Plot
#x-axis: beta from 0 to 1.5
#y-axis: row_min from 1.00 to 1.25
plt.plot(beta, r_min)

#Label the axis and add title
plt.title(r'Question 2: Relationship between $\rho_{min}$ and $\beta$', fontsize=16)
plt.xlabel(r' $\beta$ ', fontsize=14)
plt.ylabel(r' $\rho_{min}$ ', fontsize=14)
plt.xlim(0, 1.50)
plt.ylim(1,1.25)

print(r_min) #Print out the values for r_min, for debugging

plt.show() #Show the graph

sys.exit()
