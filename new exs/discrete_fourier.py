import cmath as cm  
import matplotlib.pyplot as plt 
import numpy as np
from numpy.fft import rfft,irfft

fname = "sunspots.txt"
mon, sunspots = np.genfromtxt(fname, dtype="float", comments="#", usecols=(0,1), unpack=True)

# plot data
plt.plot(mon, sunspots)
plt.xlabel("Months")
plt.ylabel("Sunspots")
plt.tight_layout()
plt.show()

# apply DFT
N = len(sunspots)
c = np.zeros(N//2+1, complex)

for k in range(N//2+1):
    for n in range(N):
        c[k] += sunspots[n] * cm.exp(-2j*cm.pi*k*n/N)

# we can take the absolute value just to plot the coefficients
# but in order to rebuild the original function we're going to need the complex values
cabs = abs(c)

# plot fourier coefficients 
kk = range(N//2+1)
plt.plot(kk, cabs)
plt.xlabel("k")
plt.ylabel("|$c_k$|")
plt.tight_layout()
plt.show()

maxck = max(cabs)
kmax = 0.
for i in range(len(cabs)):
    if (cabs[i] == maxck):
        kmax = k

nu = kmax/N
T = N/kmax 

print(nu, T)

threshold = 1e4

for k in range(N//2+1):
    if (cabs[k]<threshold):
        c[k] = 0.0

#cN = np.zeros(N, complex)
#for k in range(N//2+1):
#    cN[k] = c[k]
#for k in range(N//2+1,N,1):
#    cN[k] = c[N-k]

#sunspots2=irfft(c)
# rebuild original function
sunspots2 = np.zeros(N, complex)
for n in range(N):
    for k in range(N//2+1):
        sunspots2[n] += c[k] * cm.exp(2j*cm.pi*k*n/N)

sunspots2 /= N
plt.plot(mon, sunspots)
plt.plot(mon, sunspots2)
plt.xlabel("Months")
plt.ylabel("Sunspots")
plt.tight_layout()
plt.show()