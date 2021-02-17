import random as rn
import numpy as np
import matplotlib.pyplot as plt

def gauss(x):
    x = 1./(np.sqrt(8*np.pi))*np.exp(-x**2/8.)
    return x

L = 1.
y = []

rn.seed(190909)
while(L < int(1e4)):
    a = rn.random()
    yt = a*100. - 50.
    b = rn.random()
    if (b < gauss(yt)):
        y.append(yt)
    L = len(y)

print(len(y))

fig, bins = np.histogram(y, bins=50)
plt.hist(y, bins=bins, density=True)

x = np.linspace(-8, 8, 100)
plt.plot(x, gauss(x), "r")

plt.show()

