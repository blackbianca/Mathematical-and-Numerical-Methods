import numpy as np
import matplotlib.pyplot as plt


def poly(x, y, m):
    A = np.zeros([m,m], float)
    b = np.zeros(m, float)
    a = np.zeros(m, float)

    for i in range(m):
        for j in range(m):
            A[i][j] = sum(x**(i+j))

    for i in range(m):
        b[i] = sum(x**i*y)

    a = np.linalg.solve(A, b)

    N = int(len(x))
    y = np.zeros(N, float)
    for i in range(N):
        for j in range(m):
            y[i] += a[j]*x[i]**j

    return y

#-------main----------#

fname="evol_120msun_scattered.dat"

time,m = np.genfromtxt(fname,dtype="float", \
comments="#", usecols=(0,1), unpack=True)

m3 = poly(time,m,3)
m7 = poly(time,m,7)

plt.scatter(time,m,s=5,color="blue",label="Data")
plt.plot(time,m3,color="red",label="poly fit 3")
plt.plot(time,m7,color="green",label="poly fit 7")
plt.legend()
plt.tight_layout()
plt.show()