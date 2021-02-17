import numpy as np 
import matplotlib.pyplot as plt 

def spline(xdata, ydata):
    N = len(xdata)-2 
    A = np.zeros([N,N], float)
    b = np.zeros(N, float)

    for i in range(N):
        n = i+1
        A[i,i] = 2.*(xdata[n-1]-xdata[n+1])
        b[i] = 6.*(ydata[n-1]-ydata[n])/(xdata[n-1]-xdata[n]) - 6.*(ydata[n]-ydata[n+1])/(xdata[n]-xdata[n+1])
        if(n<N):
            A[i,i+1] = xdata[n] - xdata[n+1]
            A[i+1,i] = xdata[n] - xdata[n+1]

    k = np.linalg.solve(A,b)
    kk = [0.]
    for i in range(len(k)):
        kk.append(k[i])
    kk.append(0.)

    return kk 

def func(k, x, y):
    xdom = np.linspace(x[0], x[-2], int(1e4))
    ydom = np.zeros(len(xdom), float)
    for i in range(len(xdom)):
        for j in range(len(x)):
            if((xdom[i] >= x[j]) and (xdom[i] <= x[j+1])):
                ydom[i] = k[j]/6. * ((xdom[i]-x[j+1])**3./(x[j]-x[j+1]) - (x[j]-x[j+1])*(xdom[i]-x[j+1])) - k[j+1]/6.*((xdom[i]-x[j])**3./(x[j]-x[j+1]) - (x[j]-x[j+1])*(xdom[i]-x[j])) + (y[j]*(xdom[i]-x[j+1]) - y[j+1]*(xdom[i]-x[j]))/(x[j]-x[j+1])

    return xdom, ydom

#----------main-----------#

N = int(18)

x = np.arange(0,18,1.)
y = np.sin(x)

fname = "evol_120msun_scattered.dat"
time,mass = np.genfromtxt(fname,dtype="float", comments="#", usecols=(0,1), unpack=True)


kappa = spline(time, mass)
t, m = func(kappa, time, mass)

plt.scatter(time, mass, s=10)
plt.plot(t, m, color="red")
plt.tight_layout()
plt.show()