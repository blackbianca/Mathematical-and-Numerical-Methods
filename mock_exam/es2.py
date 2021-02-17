import numpy as np 
import matplotlib.pyplot as plt 

c = 1./np.log(1e3)
y = lambda x : c/x

N = int(1e6)
smin = 1. 
smax = 1e3
values = []

for i in range(N):
    a = np.random.rand()
    s = smin * np.exp(a/c)
    values.append(s)

logbins = np.logspace(0.,3., num=20)
plt.hist(values, bins=logbins, density=True, log=True )

stest = np.arange(1.,1e3, 1.)
plt.plot(stest, y(stest))
plt.xscale("log")
plt.show()