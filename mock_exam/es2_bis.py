import numpy as np 
import matplotlib.pyplot as plt 

c = 1./np.log(1e3)
s_min = 1. 
s_max = 1e3

svec = []
N = int(1e6)
for i in range(N):
    x = np.random.rand()
    s =  s_min*np.exp(x/c)
    svec.append(s)

y = lambda x : c/x

logbins = np.logspace(0.,3.,25)
plt.hist(svec, bins=logbins, density=True, log=True)
dom = np.linspace(s_min, s_max, int(1e4))
plt.plot(dom, y(dom))
plt.xscale("log")
plt.tight_layout()
plt.show()
