import numpy as np 
import matplotlib.pyplot as plt 

def poly_fit(x,y,Npar, xdom):
    x = np.array(x, float)
    y = np.array(y, float)

    A = np.zeros([Npar,Npar],float)
    b = np.zeros(Npar, float)

    for k in range(Npar):
        for j in range(Npar):
            A[j,k] = sum(x**(j+k))
            b[k] = sum(x**k * y)
    
    a = np.linalg.solve(A,b)
    print(len(a))
    print(a)

    yfit = np.zeros(len(xdom), float)
    for i in range(len(yfit)):
        for k in range(Npar):
            yfit[i] += a[k]*xdom[i]**k 

    return yfit


fname = "evol_120msun_scattered.dat"
time, m = np.genfromtxt(fname, dtype=float, comments="#", usecols=(0,1), unpack=True)

N1 = 3
N2 = 7
tdom = np.linspace(time[0], time[-1], int(1e4))
mfit1 = poly_fit(time,m,N1,tdom)
mfit2 = poly_fit(time,m,N2,tdom)

plt.scatter(time, m, label="dataset", color="red")
plt.plot(tdom, mfit1, label="poly fit 3", color="blue")
plt.plot(tdom, mfit2, label="poly fit 7", color="green")

plt.legend()
plt.tight_layout()
plt.show()
