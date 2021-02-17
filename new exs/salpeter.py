import numpy as np
import random as rn
import matplotlib.pyplot as plt

mmin = 0.1 
mmax = 150
alpha = 2.3
beta = 1. - alpha
N = int(1e6)
rn.seed(190909)

def salp(x):
    y = (mmax**beta + mmin**beta*(1.-x))**(1./beta)
    return y

def func(x):
    y = x**(-alpha)
    return y

mass = np.zeros(N, float)

for i in range(N):
    a = rn.random()
    a = salp(a)
    mass[i] = a

logbins = np.logspace(np.log10(mmin), np.log10(mmax), 20)
plt.hist(mass, bins=logbins, density=True, log=True)
plt.plot(mass, func(mass), label="Salpeter")
plt.xscale('log')
plt.xlabel('Stellar Mass M$_\odot$')
plt.ylabel("Population")

plt.legend()
plt.tight_layout()
plt.show()