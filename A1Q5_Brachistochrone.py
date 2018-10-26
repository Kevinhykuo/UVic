from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000) #Generate x values from 0 to 10 in steps or 100
X0 = -0.000000001 #Initial position of x

c = 1 #Just a constant

#Define the Brachistochrone function
def brach(X, t):
    y = X
    dydx = c/y - 1
    return(dydx)

#Solve the ODE
sol = odeint(brach, X0, x)

z = -(-sol)**0.5 #Doing this so Python won't freak out over square rooting a negative
print(z)

# ================
# Plotting time!!!
# ================
plt.plot(x, z)
plt.ylabel('$z$')
plt.xlabel('$x$')
plt.show()