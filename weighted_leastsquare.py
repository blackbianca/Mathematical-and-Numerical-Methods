import numpy as np
import matplotlib.pyplot as plt

def data_set():
    x = np.logspace(0,4,num=10000)
    b = -2.0
    a = 3.0
    y=10.**a * x**b

    x = np.log10(x)
    y = np.log10(y)

    sigma = np.zeros(len(x), float)
    for i in range(len(y)):
        sigma[i] = 10.*np.random.random()
        y[i] = np.random.normal(y[i], sigma[i])

    w = 1./sigma**2

    return x,y,w

def least_square(x,y,w):
    N = int(len(x))
    num = 0.
    den = 0.
    xm = 0.
    ym = 0.
    wm = sum(w)
    for i in range(N):
        xm += w[i]*x[i]/wm
        ym += y[i]*w[i]/wm
    
    for i in range(N):
        num += w[i]*y[i]*(x[i]-xm)
        den += w[i]*x[i]*(x[i]-xm)
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

x,y,w = data_set()
A,B,sA,sB,sy = least_square(x,y,w)
print(sy)
func = lambda z : A + B*z

plt.scatter(x,y, color="blue", label="data")
plt.plot(x, func(x), color="red", label="fit")

labels = []
labels.append("A = {0:.4g}".format(A)+"$\pm${0:.4g}".format(sA))
labels.append("B = {0:.4g}".format(B)+"$\pm${0:.4g}".format(sB))
labels.append("$\sigma_y$ = {0:.4g}".format(sy))

plt.legend(labels, loc='best', fontsize='small', 
          fancybox=True, framealpha=0.7, 
          handlelength=0, handletextpad=0)
plt.tight_layout()
plt.show()