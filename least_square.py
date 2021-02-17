import numpy as np
import matplotlib.pyplot as plt

def data_set():
    x = np.logspace(0,4,num=10000)
    b = -2.0
    a = 3.0
    y=10.**a * x**b

    x = np.log10(x)
    y = np.log10(y)

    sigma = 1.
    y = np.random.normal(y,sigma)

    return x,y

def least_square(x,y):
    N = int(len(x))
    num = 0.
    den = 0.
    xm = 0.
    ym = 0.
    for i in range(N):
        xm += x[i]/N
        ym += y[i]/N
    for i in range(N):
        num += y[i]*(x[i]-xm)
        den += x[i]*(x[i]-xm)
    B = num/den
    A = ym - xm*B

    sy = 0.
    for i in range(N):
        sy += (y[i]-A-B*x[i])**2/(N-1)
    sy = sy**0.5

    sum2 = 0.
    for i in range(N):
        sum2 += x[i]**2
    sum1 = sum(x)

    D = N*sum2 - sum1**2

    sA = sy*np.sqrt(sum2/D)
    sB = sy*np.sqrt(N/D)

    return A,B,sA,sB,sy


#--------main-----------#

x,y = data_set()
A,B,sA,sB,sy = least_square(x,y)

func = lambda z : A + B*z

plt.scatter(x,y, color="blue", label="data")
plt.plot(x, func(x), color="red", label="fit")

labels = []
labels.append("A = {0:.4g}".format(A)+"$\pm${0:.4g}".format(sA))
labels.append("B = {0:.4g}".format(B)+"$\pm${0:.4g}".format(sB))
labels.append("$sigma$_y = {0:.4g}".format(sy))

plt.legend(labels, loc='best', fontsize='small', 
          fancybox=True, framealpha=0.7, 
          handlelength=0, handletextpad=0)
plt.tight_layout()
plt.show()