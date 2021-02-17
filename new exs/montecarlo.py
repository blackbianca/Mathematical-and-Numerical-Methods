import numpy as np
import random as rn
import matplotlib.pyplot as plt 

Nvec = [int(1e3), int(5e3), int(1e4), int(5e4), int(1e5), int(5e5), int(1e6), int(5e6)]
Ivec = []

#rn.seed(190909)

def func(x):
    y = np.sin(1./(x*(2.-x)))**2. 
    return y

for k in range(len(Nvec)):
    N = Nvec[k]

    counter = int(0)

    for i in range(N):
        a = rn.random()*2. 
        b = rn.random()

        if (b<func(a)):
            counter += 1

    I = counter/N *2. 
    Ivec.append(I)

print(Ivec)

plt.scatter(Nvec, Ivec, s=50)
plt.plot(Nvec, Ivec, color="red")
plt.xscale("log")
plt.tight_layout()
plt.show()

Ivec = np.array(Ivec, float)
res = np.zeros(8, float)

for i in range(8):
    res[i] = Ivec[i] - 1.451904

xvec = np.linspace(1e3,5e6,1e4)
yvec = xvec**(-0.5)
plt.plot(xvec, yvec, color="orange")
plt.scatter(Nvec, res, s=50)
plt.plot(Nvec, res, color="red")
plt.tight_layout()
plt.show()