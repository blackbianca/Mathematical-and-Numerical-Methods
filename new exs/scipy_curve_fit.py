import numpy as np 
import scipy 
import matplotlib.pyplot as plt
from scipy import optimize as opt

def data_set(a):

    x = np.linspace(-5, 5, num=500)
    y = a[2]*np.exp(-(x-a[0])**2/(2.*a[1]**2))

    sigma = np.zeros(len(x), float)
    for i in range(len(y)):
        sigma[i] = 0.1*np.random.random()
        y[i] = np.random.normal(y[i],sigma[i])

    return x,y


def func(x,a,s,h):
    gauss=h*np.exp(-(x-a)**2/2./s**2)
    return gauss



#-----------main--------------#

a = [1.,1.,1.]
a = np.array(a)
xdata, ydata = data_set(a)

popt,pcov=opt.curve_fit(func, xdata ,ydata ,p0=a)

a = popt
funcfit = lambda x : a[2]*np.exp(-(x-a[0])**2/(2.*a[1]**2))
yfit = funcfit(xdata)

plt.scatter(xdata,ydata, label="dataset", s=1)
plt.plot(xdata, yfit, label="fit")

plt.legend()
plt.tight_layout()
plt.show()