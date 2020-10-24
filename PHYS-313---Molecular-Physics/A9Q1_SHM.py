import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, sin, cos
from scipy.integrate import odeint
from sympy.plotting import plot

start = -pi
end = pi
t = np.linspace(start, end, 1000)

# Define Constants
k = 1
m = 1
b = 0
A = 1 # Amplitude

# Define Functions
omega = (k/m)**0.5
print(' omega = ',omega)

# =================
# Solve using Sympy
# =================
# sym.init_printing()
#
# x_0, v_0, t = sym.symbols('x_0, v_0, t')
# x = sym.Function('x')
#
# # Define the ODE to be solved
# solsym = sym.dsolve(sym.Derivative(x(t),t, 2) + omega*x(t))
#
# # Define the Initial Conditions
# ics = [sym.Eq(solsym.args[1].subs(t, 0), x_0), sym.Eq(solsym.args[1].diff(t).subs(t, 0), v_0)]
#
# # Solve
# solved_ics = sym.solve(ics) # Solve ODE without IC
# full_sol = solsym.subs(solved_ics) #Factor in IC
#
# # Solved ODE
# F = sym.simplify(full_sol.subs({x_0:0, v_0:1}))
#
# print(F.rhs)
# # # Plot it out
# # sym.figure(1)
# plot(F.rhs, sym.diff(F.rhs, t)

# =================
# Solve using Scipy
# =================


def f(u, t):
    v, x = u
    a = -(omega**2)*x - (b/m)*v
    dd = [a, v]
    return(dd)

# ts = np.arange(0, 12, snapshot_dt)

t0 = [0, 1]

solsci = odeint(f, t0, t)

# Plot it out
plt.figure(1)
plt.plot(t, solsci[:, 0], label='$x$')
plt.plot(t, solsci[:, 1], label='$a$')

fig1 = plt.figure(2)
ax1 = fig1.add_subplot(111)
ax1.axis('equal')
ax1.plot(solsci[:, 0], abs(solsci[:, 1]/(omega)) )
plt.title(r'', fontsize=16)
plt.xlabel(r'$\frac{x}{a}$ ', fontsize=14)
plt.ylabel(r' $v/(a \omega)$ ', fontsize=14)
plt.xlim((-1, 1))
plt.ylim((0, 1))
# plt.legend()

fig2 = plt.figure(3)
ax = fig2.add_subplot(111)
ax.set_aspect('auto')
plt.axis('equal')
plt.plot(solsci[:, 0], 1/abs(solsci[:, 1]/(omega)) )
plt.title(r'', fontsize=16)
plt.xlabel(r'$\frac{x}{a}$ ', fontsize=14)
plt.ylabel(r' $a \omega s$ ', fontsize=14)
plt.xlim((-1, 1))
plt.ylim((0, 2))
# plt.legend()

# For debugging
# print(solsci[:, 0]*2/pi)
# print(solsci[:, 1]*2/pi)

plt.show()
