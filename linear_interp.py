import numpy as np
import matplotlib.pyplot as plt

fname="evol_120msun_scattered.dat"
fname2="120a300.fis"

time,m = np.genfromtxt(fname,dtype="float", \
comments="#", usecols=(0,1), unpack=True)

time2,m2 = np.genfromtxt(fname2, dtype="float", comments="#", usecols=(0,7), unpack=True)
time2 = time2*1e-6

for i in range(len(time)-1):

    y = lambda x : ((time[i+1]-x)*m[i] + (x-time[i])*m[i+1])/(time[i+1]-time[i])

    x = np.linspace(time[i], time[i+1], 100)
    interp = y(x)
    plt.scatter(x, interp, s=0.5, color="red")


plt.scatter(time, m, label="Scattered points", s=15, color="blue")
plt.scatter(time2, m2, label="Original dataset", s=0.5, color="black")
plt.xlabel("Time [Myr]")
plt.ylabel("Mass [M$_\odot$]")
plt.legend()
plt.tight_layout()
plt.show()