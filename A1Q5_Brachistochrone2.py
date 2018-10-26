from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

X0 = -0.000000001 #Initial position of x
x = np.linspace(0, 1, 100) #Generate x values from 0 to 1 in steps or 100

def brach(X, x):
    def brach3(X, x):
        y2 = X
        dydx2 = y2
        return(dydx2)

    print('Brach3:',brach3)

    y2 = odeint(brach3, X0, x)

    print('y2:', y2**2)

    y = (1-y2**2) / (-2**dydx2)
    return(y)
z = odeint(brach, X0, x)

# u = (1-brach3^2)/y2
#
# print(u)
# sol = odeint(brach, X0, x)
#
#
# y = sol
# print(y)

plt.plot(x, z)
plt.ylabel('z')
plt.xlabel('x')
plt.show()