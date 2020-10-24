import sys
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, exp, cos
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# Space for 2D plot
x = np.linspace(0,1,1000)

# Space for 3D plot
x2 = np.arange(0, 1, 0.001) #Define x as variable going from -1 to 1 with stepsize 0.001
t2 = np.arange(0, 0.07, 0.001)
x2, t2 = np.meshgrid(x2, t2)

#Commense the while loop!
def F(x,t):
    n = 1
    g = 0
    while n <= 100:
        g = g + 1/((n*pi)**2) * exp(-t*(2*n*pi)**2) * cos(2*n*pi*x)
        n += 1
    return(g)

def U(x,t):
    u = 1/6 - F(x,t)
    return(u)

def F2(x2,t2):
    n2 = 1
    g2 = 0
    while n2 <= 100:
        g2 = g2 + 1/((n2*pi)**2) * exp(-t2*(2*n2*pi)**2) * cos(2*n2*pi*x2)
        n2 += 1
    return(g2)

def U2(x,t):
    u2 = 1/6 - F2(x2,t2)
    return(u2)

#=================
# Plotting time!!!
#=================
# 2D plot
plt.figure(1)
plt.plot(x, U(x, 0), label='t=0')
plt.plot(x, U(x, 0.01), label='t=0.01')
plt.plot(x, U(x, 0.03), label='t=0.03')
plt.plot(x, U(x, 0.05), label='t=0.05')
plt.plot(x, U(x,1), label='t=1')
plt.legend('gab')
plt.title(r'Comparison between $u(x, t)$ and $x$ at various $t$', fontsize=16)
plt.xlabel(r' $x$ ', fontsize=14)
plt.ylabel(r' $u(x,t)$ ', fontsize=14)
plt.legend()


# 3D Plot
fig = plt.figure(2, dpi=100, figsize=(12, 9))
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x2, t2, U2(x2,t2), cmap=cm.coolwarm, linewidth=0, antialiased=True)
plt.title(r'Changes in $u(x, t)$ with respect to $t$ and $x$', fontsize=16)
plt.xlabel('x')
plt.ylabel('t')

plt.show()

sys.exit()
