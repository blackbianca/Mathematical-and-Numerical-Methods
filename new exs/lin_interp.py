import numpy as np 
import matplotlib.pyplot as plt  

fname = "evol_120msun_scattered.dat"
fname2 = "120a300.fis"

time,m = np.genfromtxt(fname,dtype="float", comments="#", usecols=(0,1), unpack=True)
time2,m2 = np.genfromtxt(fname2,dtype="float", comments="#", usecols=(0,7), unpack=True)

Nt1 = int(len(time))
Nm1 = int(len(m))
#Nt2 = int(len(time2))
#Nm2 = int(len(m2))

#print(Nt1, Nm1, Nt2, Nm2)
time2 /= 1e6

for i in range(Nt1-1):
    
    y = lambda t : ((time[i+1]-t)*m[i] + (t - time[i])*m[i+1])/(time[i+1]-time[i]) 
    
    temp = np.linspace(time[i], time[i+1], 100)
    masses = y(temp)
    plt.plot(temp, masses, color="red")

plt.scatter(time, m, s=50, label="data sample")
plt.scatter(time2, m2, s=5, label="total data")
plt.xlabel("time [Myr]")
plt.ylabel("mass [$M_{odot}$]")

plt.legend()
plt.tight_layout()
plt.show()