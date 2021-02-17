import random as rn
import numpy as np
import matplotlib.pyplot as plt

xvec=[]

rn.seed(190909)
for i in range(int(1e3)):
    x = rn.random()
    xvec.append(x)


hist, bins = np.histogram(xvec, bins = 20)
logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
plt.hist(xvec, bins=logbins )
plt.xscale("log")

plt.show()
