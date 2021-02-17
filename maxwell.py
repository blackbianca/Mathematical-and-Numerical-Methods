import random as rn
import numpy as np
import matplotlib.pyplot as plt

def maxwell(x, sigma):
    x = np.sqrt(2./np.pi)* (x**2/sigma**3) * np.exp(-x**2/(2*sigma**2))
    return x

x,y,z = [],[],[]

for i in range(int(1e5)):
    a = np.random.normal(loc=0.0, scale=265.0)
    b = np.random.normal(loc=0.0, scale=265.0)
    c = np.random.normal(loc=0.0, scale=265.0)
    x.append(a)
    y.append(b)
    z.append(c)

v = [0] * len(x)

for j in range(len(x)):
    v[j] = np.sqrt( x[j]**2 + y[j]**2 + z[j]**2 )


fig, bins = np.histogram(y, bins=50)
logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
plt.hist(v, bins=50, density=True)

x = np.logspace(0, 3, int(100))
#x = np.linspace(0, 1000., int(1e5))
plt.plot(x, maxwell(x,265.0), "r")
#plt.xlim(0, 1e3)
#plt.xscale('log')

plt.show()