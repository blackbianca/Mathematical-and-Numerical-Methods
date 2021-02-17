import numpy as np
import matplotlib.pyplot as plt 

def func(x, t):
    y = np.exp(-x) + np.sin(t)
    return y

# main

t = 0.
t_end = 200. 
h = 0.01 
x = 0.
xvec = []
time = []

xvec.append(x)
time.append(t)

#-----first-step-----------#

y = x + h/2 *func(x, t)
x = x + h*func(y, t+h/2.)

xvec.append(x)
time.append(t)

t+=h

#-----main-cycle----------#

while(t<t_end):

    y = y + h*func(x, t+h)
    x = x + h*func(y, t+3*h/2.)

    xvec.append(x)
    time.append(t)

    t+=h

xend = 0.5 * (x + y + h/2.*func(x,t_end))
xvec.append(xend)
time.append(t_end)

plt.scatter(time, xvec, s=0.5, color="blue", )
plt.xlabel("time (s)")
plt.ylabel("x(t)")
plt.tight_layout()
plt.show()