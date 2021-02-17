import numpy as np 
import matplotlib.pyplot as plt 

sigma = 2.
def gauss(x):
    y = 1/np.sqrt(2*np.pi*sigma**2) * np.exp(-x**2/(2.*sigma**2))
    return y

N=int(1e5)
data = []

for i in range(N):
    a = np.random.rand()*100. - 50. # number a distributed according to f(x) which in this case is just uniform
    m = np.random.rand()            # number m distributed always according to uniform

    if (m>gauss(a)):                # comparison between m and p(a)
        continue
    else:
        data.append(a)


plt.hist(data, bins = 50, density=True)
x = np.linspace(-8, 8, 100)
plt.plot(x, gauss(x), "r")
plt.tight_layout
plt.show()