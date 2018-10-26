import numpy as np
import matplotlib.pyplot as plt

# Define the constants
# ====================
g = 1
l = 1

# ======
# Part a
# ======

m = np.linspace(0.0001, 10, 100)

def omega_a(m, pm):
    M = 1/m # M = m2/m1
    omega_a_SQ = g/l * ((1+M) + pm*(M+M**2)**0.5)
    omega_a = omega_a_SQ**0.5
    return(omega_a)

print(omega_a(0.00001, -1))

plt.figure(1)
plt.title('Part (a): Eigenfrequencies as a function of M for a double pendulum')
plt.plot(m, omega_a(m, 1), label=r'$\omega_+$')
plt.plot(m, omega_a(m, -1), label=r'$\omega_-$')
plt.xlabel(r' M = m1/m2 ', fontsize=14)
plt.ylabel(r' Eigenfrequency ($\omega$)', fontsize=14)
plt.legend()
plt.ylim(0.5, 3)
plt.xlim(0, 5)

# ======
# Part b
# ======
L = np.linspace(0.0001, 10, 100)
l2 = 1

def omega_b(L, pm):
    omega_b_SQ = g * (L + 1 + pm*(L**2 + 1)**0.5) / (l/l2)
    omega_b = omega_b_SQ**0.5
    return(omega_b)

plt.figure(2)
plt.title('Part (b): Eigenfrequencies as a function of L for a double pendulum')
plt.plot(L, omega_b(L, 1), label=r'$\omega_+$')
plt.plot(L, omega_b(L, -1), label=r'$\omega_-$')
plt.xlabel(r' L = l1/l2 ', fontsize=14)
plt.ylabel(r' Eigenfrequency ($\omega$)', fontsize=14)
plt.legend()

plt.show()
