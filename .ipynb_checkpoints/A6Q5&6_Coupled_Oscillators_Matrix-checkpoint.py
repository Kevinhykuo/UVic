# In[0]
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.sparse import diags
from math import pi

# Define the constants
n = 10  # Number of oscillators
m = 1  # Mass of oscillators
k = 1  # Spring constant
Displacement = 1  # Amount of displacement
Displaced_Osc = 2  # Which oscillator to displace
L = Displacement * 10  # Total length of coupled oscillators
t = np.linspace(0, 100 * n, 1000 * n)

# Which oscillator we are intrested
OsNum = 1

# =============================
# Build the equations of motion
# =============================
# Build the matrix for the equations of motion
def matrix(n):
    diagonals = [(1 / m) * np.ones(n), -2 * k * np.ones(n), k *
                 np.array([0] + [1] * (n - 1) + [0]), k * np.ones(n - 1)]
    M = diags(diagonals,
              [n, -n, -n + 1, -n - 1])
    return(M)

M = matrix(n).toarray()
print(M)

# Define the equations of motion
def EoM(pq, t):
    return(M @ pq)

# Define the initial conditions
ic = np.zeros(2 * n)
ic[Displaced_Osc - 1] = Displacement  # Displacing a mass

# Slove the equations of motion
sol = odeint(lambda x, t: EoM(x, M), ic, t)
# print(sol)
# print(sol.shape)

# Plot it out
# ===========
# In[] Plot motion of all the oscillators
plt.figure(1)
for i in range(n):
    plt.plot(t, (sol[:, i] + (i + 1) * L / (n + 1)), label=i + 1)
plt.title(r'Motion of coupled oscillators')
plt.xlabel(r'Time ($t$)')
plt.ylabel(r'Position ($x$)')
plt.xlim(0, n * 10)
# plt.legend()

# In[] Plot motion of one oscillator
plt.figure(2)
plt.plot(t, sol[:, OsNum - 1], label=OsNum)
plt.title(r'Motion of oscillator')
plt.xlabel(r'Time ($t$)')
plt.ylabel(r'Position ($x$)')
plt.xlim(0, n * 10)
plt.legend()

# In[]
# ========================
# Do the Fourier transform
# ========================
Oscillator = sol[:, OsNum]

Fourier = np.fft.rfft(Oscillator)
freq = 2 * pi * np.fft.rfftfreq(t.shape[0], 0.1)

# Plot it out
# ===========
plt.figure(3)
plt.plot(freq, abs(Fourier), label=OsNum)
plt.title(r'Fourier transform of the motion of oscillator')
plt.xlabel(r'Frequency ($f$)')
# plt.ylabel(r'Position ($x$)')
plt.xlim(0, 0.22 * n)
plt.legend()

plt.show()
