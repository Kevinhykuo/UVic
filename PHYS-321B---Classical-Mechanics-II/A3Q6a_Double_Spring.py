import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

start = 0
end = 50
step = 1000

t = np.linspace(start, end, step)

# Define constants
m = 1
k = 1

# Define the function
def H(t0, t):
    q1, q2, p1, p2 = t0
    dd = [p1, p2, (k/m) * (q2 - 2*q1), (k/m) * (q1 - 2*q2)]
    return(dd)

# Define the initial conditions
t0 = [0.1, 0, 1, 0]

# Solve the ode
sol = odeint(H, t0, t)

# Plot it out
plt.plot(t, sol[:, 2], label='q1 (m1)')
plt.plot(t, sol[:, 3], label='q2 (m2)')
plt.title(r'Changes in position of a triple spring system', fontsize=16)
plt.xlabel(r' Time $(t)$ ', fontsize=14)
plt.ylabel(r' Positon $(q)$ ', fontsize=14)
plt.legend()
plt.show()
