import numpy as np 
import random as rn 
import matplotlib.pyplot as plt 
import scipy.integrate

rn.seed(190909)

def func(x):
    y = (np.exp(x)+1)**(-1.)
    return y 

# notice that func is already f(x)/w(x)
# in this case w(x) = x**-0.5 and its integral from 0 to 1 is =2

Iw = 2. 

Nvec = [int(1e3), int(5e3), int(1e4), int(5e4), int(1e5), int(5e5), int(1e6), int(5e6)]
Ivec = []

for k in range(len(Nvec)):
    N = Nvec[k]
    s = 0.
    for i in range(N):
        a = rn.random()**2
        s += func(a)

    I = s/N*Iw
    Ivec.append(I)

#print(Ivec)

realfunc = lambda x : (np.exp(x)+1)**(-1.) * x**-0.5
Itrue = scipy.integrate.quad(realfunc, 0, 1)
print(Itrue)

plt.scatter(Nvec, Ivec, s=50)
plt.plot(Nvec, Ivec, color="red")
plt.xscale("log")
plt.tight_layout()
plt.show()