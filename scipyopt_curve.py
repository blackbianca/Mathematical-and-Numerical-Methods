import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rnd
from scipy import optimize as opt

def data_set(a):
    x = np.linspace(-10.,10.,num=500)
    y = a[2]*np.exp(-(x-a[0])**2/(2.*a[1]**2))

    sigma = np.zeros(len(x), float)
    for i in range(len(y)):
        sigma[i] = 4.*rnd.random()
        y[i] = rnd.normal(y[i], sigma[i])

    return x,y

def func(x,m,s,h):
    gauss = h*np.exp(-(x-m)**2/(2.*s**2))
    return gauss


#---------main----------#

a = [0.,1.,10.]
a = np.array(a)
x,y = data_set(a)

popt, pcov = opt.curve_fit(func, x, y, p0=(a[0],a[1],a[2]))

gauss = lambda x:  popt[2]*np.exp(-(x-popt[0])**2/(2.*popt[1]**2))

#labels = []
#labels.append("mean = {0:.4g}".format(lsq.x[0]))
#labels.append("norm = {0:.4g}".format(lsq.x[2]))
#labels.append("$\sigma$ = {0:.4g}".format(lsq.x[1]))

plt.scatter(x,y,s=5,color="blue",label="Data")
plt.plot(x,gauss(x),color="red",label="scipy fit")

plt.legend()
#plt.legend(labels, loc='best', fontsize='small', 
#          fancybox=True)
plt.tight_layout()
plt.show()