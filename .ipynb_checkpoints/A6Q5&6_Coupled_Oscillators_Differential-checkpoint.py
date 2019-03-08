import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Solve the coupled oscillators using differential Equations
# DOES NOT WORK

start = 0
end   = 10
step  = 100

t = np.linspace(start, end, step)
# t = np.arrange(start, end, step)

# Define the constants
# ====================
k = 1   # Spring constant
m = 1   # Mass
n = 10  # Number of masses

# Define the funcitons
# ====================
# def q_dot(ic, time): # ic are the initail conditions for pi and qi
#     p = p[0:n]
#     q_dot = [i/m for i in p] # Divide each term in p by m
#     return(q_dot)
#
# def p_dot(ic, time):
#     p_dot = -k * (2*q[2:n-1] - q[1:n-2] - q[3:n])
#     retun(p_dot)
#
# def p_dot1(ic, time):
#     p_dot1 = -k * (2*q[0] - q[1])
#     return(p_dot1)
#
# def p_dotn(ic, time):
#     p_dotn = -k * (2*q[n] - q[n-1])

# Equations of motion for momentas
def EoMp(ic, time):
    # The coordinats:
    q[0], q[1:n], p[:n] = ic
    # The momentas:
    p_dot = -k * (2*q[2:n-1] - q[1:n-2] - q[3:n])
    p_dot1 = -k * (2*q[0] - q[1])
    p_dotn = -k * (2*q[n] - q[n-1])
    # The differential equation:
    DE = [p[0] + p[1:n-1] + p[n] + p_dot1 + p_dot + p_dotn] # Combine the lists into a bigger list
    return(DE)

# Define the initial conditions
ic = np.zeros(n*2)
ic[0] = 1
# print(ic)

sol = odeint(EoMp, ic, t)

# Plot it out
plt.plot(t, sol[:, (n-1)+1], label='q1 (m1)')
plt.title(r'Changes in position of an oscillator in an coupled oscillator system', fontsize=16)
plt.xlabel(r' Time $(t)$ ', fontsize=14)
plt.ylabel(r' Positon $(q)$ ', fontsize=14)
plt.legend()
plt.show()

# =================
# Previous Attempts
# =================

# # Generate the names
# # ==================
# n = 10 # Number of terms
# P = [] # Array for momenta names
# Q = [] # Array for positon names
# for i in range (n): # Generate the names for
#     p = "p"+str(i)  # momentum
#     q = "q"+str(i)  # positon
#     # Convert the names into variales
#     exec("%s = %d" % p)
#     exec("%s = %d" % q)
#     # Put the names into the arrays
#     P.append(p)
#     Q.append(q)
# # Print the names out for error checking
# print(P)
# print(Q)
#
# # Generate the functions
# # ======================
# Q_dot = []
#
# for i in range(n):
#     def Q_dot(P[i]):
#         q_dot = P[i] / m
#         Q_dot.append(q_dot)
#     i += 1
#
# # Define the funciton
# # ===================
# # def H(t0, t):
#
#
# # Define the initial conditions
# # =============================
# # q1 = 0.1, p1 = 0
#
# # Solve the ode
# # sol = odeint(H, t0, t)
