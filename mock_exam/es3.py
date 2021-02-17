import numpy as np 
import matplotlib.pyplot as plt

def func(x):
    y = np.sin(x)*(1-x)**2
    return y 

dom = np.arange(0., np.pi, 0.01)
plt.plot(dom, func(dom))
plt.show()

Nvec = [int(1e3), int(1e4), int(1e5), int(1e6)]
Ivec = []
for j in range(len(Nvec)):
    N = Nvec[j]
    values = np.zeros(N, float)
    for k in range(N):
        a = np.random.rand()*np.pi
        b = func(a)
        values[k] = b 

    I = np.pi/N * sum(values)
    Ivec.append(I)

plt.plot(Nvec,Ivec)
plt.scatter(Nvec,Ivec, color="red")
plt.xscale("log")
plt.show()


