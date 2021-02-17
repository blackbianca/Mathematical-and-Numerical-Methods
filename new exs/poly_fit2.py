import numpy as np 
import matplotlib.pyplot as plt 

def poly(xdata, ydata, x, Npar):
    N = int(len(xdata))
    A = np.zeros([Npar,Npar], float)
    b = np.zeros(Npar, float)
    for k in range(Npar):
        for j in range(Npar):    
            A[k,j] = sum(xdata**(k+j))
    for k in range(Npar):
            b[k] = sum(xdata**k * ydata)

    a = np.linalg.solve(A,b)

    func = np.zeros(len(x), float)
    for i in range(len(x)):
        for j in range(Npar):
            func[i] += a[j]*x[i]**j

    return func


#-----------main-----------#

fname = "evol_120msun_scattered.dat"
time, mass = np.genfromtxt(fname, dtype=float, comments="#", usecols=(0,1), unpack=True)

t = np.linspace(time[0], time[-1], int(1e4))

N1 = 3
m1 = poly(time, mass, t, N1)

N2 = 7
m2 = poly(time, mass, t, N2)

#----------plot-------------#

plt.scatter(time, mass, s=10)
plt.plot(t, m1, color="red")
plt.plot(t, m2, color="green")
plt.tight_layout()
plt.show()