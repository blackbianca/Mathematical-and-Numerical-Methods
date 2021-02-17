import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rnd
from scipy import optimize as opt

def data_set(a):
    x = np.linspace(-5.,5.,num=500)
    y = a[2]*np.exp(-(x-a[0])**2/(2.*a[1]**2))

    sigma = np.zeros(len(x), float)
    for i in range(len(y)):
        sigma[i] = 0.1*rnd.random()
        y[i] = rnd.normal(y[i], sigma[i])

    return x,y

def fun_res(a,x,y):
    gauss_res = a[2]*np.exp(-(x-a[0])**2/(2.*a[1]**2)) - y
    return gauss_res


#---------main----------#

a = [0.,2.,1.]
a = np.array(a)
x,y = data_set(a)

lsq = opt.least_squares(fun_res, a, args = (x,y), xtol = 1e-7, loss="cauchy")

gauss = lambda x:  lsq.x[2]*np.exp(-(x-lsq.x[0])**2/(2.*lsq.x[1]**2))

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