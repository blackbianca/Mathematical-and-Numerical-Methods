import random as rn
import numpy as np
import matplotlib.pyplot as plt

avec = []
bvec = []

rn.seed()
for i in range(int(1e4)):
    a = rn.random()
    avec.append(a)
    bvec.append(a**0.5)

n_bins = int(50)

fig, axs = plt.subplots(1, 2, tight_layout=True)  # number of rows and columns, tight_layout improves the images displaying

axs[0].hist(avec, bins=n_bins)
axs[1].hist(bvec, bins=n_bins)

plt.show()