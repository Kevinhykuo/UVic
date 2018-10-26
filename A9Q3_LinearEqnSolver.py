import numpy as np

# ==========
# Part (a)
# ==========
# Solve for linear equations:
# ax + by + c = 0
# dx + ey + f = 0

# Enter the constants for equations
def sol(a, b, c, d, e, f):
    A = np.array([[a, b], [d, e]])
    B = np.array([-c, -f])
    x = np.linalg.solve(A, B)
    return(x)

# ==========
# Part (b.i)
# ==========
b1 = sol(2.63458, 9.23701, -7.29513, 7.43267, -2.94365, 5.15426)
print('Part 3(b.i):')
print('x = ', round(b1[0], 7))
print('y = ', round(b1[1], 7))
print(' ')

# ==========
# Part (b.ii)
# ==========
b2 = sol(3.41657, 4.72491, 1.53768, 4.44714, -6.92258, -3.68256)
print('Part 3(b.ii):')
print('x = ', round(b2[0], 7))
print('y = ', round(b2[1], 7))