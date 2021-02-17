import numpy as np 
import matplotlib.pyplot as plt 

N = int(1e5) 
sigma = 265. 

xvec = []
yvec = []
zvec = []

def maxwell(x):
    x = np.sqrt(2./np.pi)* (x**2/sigma**3) * np.exp(-x**2/(2*sigma**2))
    return x

for i in range(N):
    z1 = np.random.rand()
    z2 = np.random.rand()

    r = np.sqrt(-2*sigma**2*np.log(1-z1))
    theta = np.pi * 2 * z2

    x = r*np.cos(theta)
    y = r*np.sin(theta)

    xvec.append(x)
    yvec.append(y)

for i in range(N):
    z1 = np.random.rand()
    z2 = np.random.rand()

    r = np.sqrt(-2*sigma**2*np.log(1-z1))
    theta = np.pi * 2 * z2

    x = r*np.cos(theta)

    zvec.append(x)

xvec = np.array(xvec, float)
yvec = np.array(yvec, float)
zvec = np.array(zvec, float)
vec = np.zeros(N, float)

for j in range(N):
    vec[j] = np.sqrt( xvec[j]**2 + yvec[j]**2 + zvec[j]**2 )


xtry = np.linspace(0,1000,1000)
ytry = maxwell(xtry)

logbins = np.logspace(0., 3., 25)
plt.hist(vec, bins=logbins, density=True)
# add log=True to get a log scale in the y axis


#plt.hist(vec, bins=25, density=True)
# I can also just use linear spacing, but in this case 
# the bins won't have the same wideness

plt.plot(xtry, ytry)
plt.xscale("log")


plt.tight_layout()
plt.show()