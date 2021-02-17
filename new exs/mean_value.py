import numpy as np
import matplotlib.pyplot as plt
import random as rn

def func(x):
    y = np.sin(1./(x*(2.-x)))**2. 
    return y

Nvec = [int(1e3), int(5e3), int(1e4), int(5e4), int(1e5), int(5e5), int(1e6), int(5e6)]
Ivec = []

for k in range(len(Nvec)):
    N = Nvec[k]

    s = 0. 
    
    for i in range(N):
        x = rn.random()*2.
        s += func(x)

    I = 2./N*s 
    Ivec.append(I)

print(Ivec)

plt.scatter(Nvec, Ivec, s=50)
plt.plot(Nvec, Ivec, color="red")
plt.xscale("log")
plt.tight_layout()
plt.show()