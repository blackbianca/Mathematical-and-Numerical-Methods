import numpy as np 
import matplotlib.pyplot as plt 

ttrue = 3. 
xtrue = 10. 
tol = 1e-1 
v = 0.
x = 0. 
t = 0.
N = int(1e3)
h = ttrue/N
a = -9.81

def euler(x,v):
    x = x + v*h 
    v = v + a*h
    return x, v

xvec = np.zeros(N, float)
vvec = np.zeros(N, float)
time = np.zeros(N, float)

while(abs(xvec[-1]-xtrue)>tol):
    while(t < ttrue):
        num = int(t/h)
        xvec[num] = x 
        vvec[num] = v 
        time[num] = t 

        x, v = euler(x, v)
        t += h
        
    t = 0.
    v = vvec[0] + 1e-2
    x = xvec[0]



v = vvec[0]
x = 0. 
t = 0.

while(t < ttrue):
    num = int(t/h)
    xvec[num] = x 
    vvec[num] = v 
    time[num] = t 

    x, v = euler(x, v)
    t += h

plt.scatter(time, xvec)
plt.scatter(time, vvec) 

plt.show()


