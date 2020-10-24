# from scipy.constants import *
# print ("The Planck constant h:", c)
# print ("The Avogadro constant N_A:", N_A)
# print ("The muon mass in u:", physical_constants['muon mass in u'])

# In[]
from plotly import offline
offline.init_notebook_mode()
offline.iplot([{"y": [1, 2, 1]}])

# In[]
import matplotlib
matplotlib.use('Qt5Agg')
# This should be done before `import matplotlib.pyplot`
# 'Qt4Agg' for PyQt4 or PySide, 'Qt5Agg' for PyQt5
import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(0, 20, 500)
plt.plot(t, np.sin(t))
plt.show()

# In[]
from IPython.display import Latex
Latex('''The mass-energy equivalence is described by the famous equation

$$E=mc^2$$

discovered in 1905 by Albert Einstein.
In natural units ($c$ = 1), the formula expresses the identity

\\begin{equation}
E=m
\\end{equation}''')

# In[]
import sympy as sp
sp.init_printing(use_latex='mathjax')
x, y, z = sp.symbols('x y z')
f = sp.sin(x * y) + sp.cos(y * z)
sp.integrate(f, x)

# In[]
from IPython.display import Math
Math(r'i\hbar \frac{dA}{dt}~=~[A(t),H(t)]+i\hbar \frac{\partial A}{\partial t}.')

# In[]
from IPython.display import Image
Image('http://jakevdp.github.com/figures/xkcd_version.png')

# In[]
## Heading test
%timeit 3+1

# In[]
from sympy import Symbol, Matrix
x = Symbol('x')
y = Symbol('y')
A = Matrix([[1,x], [y,1]])
print(A)
