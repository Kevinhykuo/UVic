import sys
import math

'''
Approximate two-variable integral using Riemann sum.
Evaluate f(x,y)=sin(x+y)
Over region:
    x=0
    y=0
    y=1-z
Estimate using n=2000
'''

print("PHYS 326 - Assignment 1 - Q8")
print("Approximate two-variable integral using Riemann sum. " "\n"
      "Evaluate f(x,y)=sin(x+y)" "\n"
      "Over region:"    "\n"
            "x=0"       "\n"
            "y=0"       "\n"    
            "y=1-z"     "\n"
      "Estimate using n=5000")

def f(x,y):
    return math.asin(x+y)

x1 = 0
x2 = 1
y1 = 0
y2 = 1 - x2
n = 5000

Dx = (x2-x1)/n
Dy = (y2-y1)/n

i = 0
V = 0

while (i <= (n + 1)):
    V = f(x2,y2) * Dx*Dy + V
    i = i + 1

print("Volume apporximated using Riemann sum (n=5000) is", V)