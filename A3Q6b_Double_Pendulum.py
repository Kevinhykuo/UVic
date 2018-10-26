import sys
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, sin, cos
from scipy.integrate import odeint
from matplotlib import animation

start = 0
end = 15
step = 1000

t = np.linspace(start, end, step)

# Define constants
m = 1
l = 1
g = 9.81

# Define the functions
a = m*l**2

def H(t0, t):
    theta1, theta2, p1, p2 = t0
    c = cos(theta1 - theta2)
    s = sin(theta1 - theta2)
    t1 = p1**2 + 2*p2**2 - 2*p1*p2*c
    t3 = c*s
    b1 = (1+s**2)
    t2 = p1*p2*s
    f1 = t1*t3/(a*b1**2) - t2/(a*b1) - 2*m*g*l*sin(theta1)
    f2 = -t1*t3/(a*b1**2) + t2/(a*b1) - m*g*l*sin(theta2)
    dd = [p1, p2, f1, f2]
    return(dd)

# !!!This one may be inaccurate!!!
# def H(t0, t):
#     theta1, theta2, p1, p2 = t0
#     c = cos(theta1 - theta2)
#     s = sin(theta1 - theta2)
#     t1 = s*(c**2 - 2) - 2*s*c**2
#     t2 = p1*p2/a
#     b1 = (c**2 - 2)**2
#     f1 = t1*t2/b1 -  2*m*g*l*sin(theta1)
#     f2 = -t1*t2/b1 - m*g*l*sin(theta2)
#     dd = [p1, p2, f1, f2]
#     return(dd)


# Define the initial conditions
# t0 = [theta1, theta2, p1, p2]
t0 = [pi/2, 0, 0, 0]


# Solve the ODE
sol = odeint(H, t0, t)

# Plot it out
plt.figure(1)
plt.plot(t, sol[:, 2], label='$\\theta_1$')
plt.plot(t, sol[:, 3], label='$\\theta_2$')
plt.plot(t, sol[:, 0], label='$p_1$')
plt.plot(t, sol[:, 1], label='$p_2$')
plt.title(r'Changes in angles of a double pedulum', fontsize=16)
plt.xlabel(r' Time $(t)$ ', fontsize=14)
plt.ylabel(r' Angle $(rad)$ ', fontsize=14)
plt.legend()

plt.figure(2)
plt.plot(sol[:, 0], sol[:, 2])
plt.title('Phase diagram of $p_1$ and $\\theta_1$', fontsize=16)
plt.xlabel('$\\theta_1$', fontsize=14)
plt.ylabel('$p_1$', fontsize=14)

plt.figure(3)
plt.plot(sol[:,1 ], sol[:, 3])
plt.title('Phase diagram of $p_2$ and $\\theta_2$', fontsize=16)
plt.xlabel('$\\theta_2$', fontsize=14)
plt.ylabel('$p_2$', fontsize=14)

# Define another set of initial conditions
t0 = [pi/2, 0.05, 0, 0]

# Solve the new ode
sol = odeint(H, t0, t)

# Plot it out again
plt.figure(4)
plt.plot(t, sol[:, 2], label='$\\theta_1$')
plt.plot(t, sol[:, 3], label='$\\theta_2$')
plt.plot(t, sol[:, 0], label='$p_1$')
plt.plot(t, sol[:, 1], label='$p_2$')
plt.title(r'Changes in angles of a double pedulum', fontsize=16)
plt.xlabel(r' Time $(t)$ ', fontsize=14)
plt.ylabel(r' Angle $(rad)$ ', fontsize=14)
plt.legend()

plt.figure(5)
plt.plot(sol[:, 0], sol[:, 2])
plt.title('Phase diagram of $p_1$ and $\\theta_1$', fontsize=16)
plt.xlabel('$\\theta_1$', fontsize=14)
plt.ylabel('$p_1$', fontsize=14)

plt.figure(6)
plt.plot(sol[:,1 ], sol[:, 3])
plt.title('Phase diagram of $p_2$ and $\\theta_2$', fontsize=16)
plt.xlabel('$\\theta_2$', fontsize=14)
plt.ylabel('$p_2$', fontsize=14)


plt.show()
