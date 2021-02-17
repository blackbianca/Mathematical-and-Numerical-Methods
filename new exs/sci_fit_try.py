import numpy as np 
from scipy import optimize
import matplotlib.pyplot as plt

def pol(x,a0,a1,a2,a3,a4):
    y = a0 + a1*x + a2*x**2. + a3*x**3. + a4*x**4. 
    return y 

fname = "evol_120msun_scattered.dat"
time,mass = np.genfromtxt(fname,dtype="float", comments="#", usecols=(0,1), unpack=True)

par = [1.,1.,1.,1.,1.]
popt, pcov = optimize.curve_fit(pol, time,mass,p0=(par[0], par[1], par[2], par[3], par[4]))

t = np.linspace(time[0], time[-1], int(1e4))
m = pol(t, popt[0], popt[1], popt[2], popt[3], popt[4])

plt.scatter(time, mass, s=5)
plt.plot(t, m, color="red")
plt.tight_layout()
plt.show()