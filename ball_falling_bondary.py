import numpy as np
import matplotlib.pyplot as plt

g = 9.81

x = 0.
v = 0.
t = 0.
x1 = 10. 
t1 = 3.

tol = 1e-3
N = 1e3

while(abs(x-x1)>tol):
    v += 1e-5
    x = v* t1 - 0.5 * g * t1**2

v0 = v

h = t1/N
xvec = []
vvec = []
time = []
count = 0.

while(x>=0):
    x = v0*t - 0.5*g*t**2
    v = v0 - g*t

    xvec.append(x)
    vvec.append(v)
    time.append(t)

    t += h
    count += 1

plt.scatter(time, xvec, s=0.5, color="blue", label="x(t)")
plt.scatter(time, vvec, s=0.5, color="red", label="v(t)")
plt.xlabel("time (s)")

plt.legend()
plt.tight_layout()
plt.show()

    
