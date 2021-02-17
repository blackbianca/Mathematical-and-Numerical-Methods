import numpy as np
import matplotlib.pyplot as plt
import cmath
from numpy.fft import rfft,irfft

fname="sunspots.txt"

mon,spots = np.genfromtxt(fname,dtype="float", \
comments="#", usecols=(0,1), unpack=True)

# data plotting
plt.plot(mon,spots)
plt.xlabel("Time $t$",fontsize=20)
plt.ylabel("$f(t)$",fontsize=20)
#plt.xlim(0,1024)
plt.tight_layout()
plt.show()


# calculates Fourier transform with DFT
N=len(spots)
c=np.zeros(N//2+1, complex)
for k in range(N//2+1):
    for n in range(N//+1):
        c[k] += spots[n]*cmath.exp(-1j*2*cmath.pi*k*n/N)


cabs=(abs(c))
kk=[]
maxc=0.0
maxk=0

# calculated frequency k/N corresponding to the max c_k
kk = range(N//2+1)

    
#plots |ck| versus k (Figure 74)
plt.plot(kk,cabs)
plt.xlabel("$k$",fontsize=20)
plt.ylabel("$|c_k|$",fontsize=20)
#plt.ylim(0,600)
#plt.xlim(0,513)
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


#prints frequency corresponding to the max c_k
#print(maxk*float(N),maxk,maxc)

#DENOISE DATA BY REMOVING THE SMALLEST |c_k| (possibly white noise)
threshold=1e4 #maximum value of |c_k| that I consider associated with noise
for k in range(N//2+1):
    if(cabs[k]<threshold):
        c[k]=0.0

#spots2=irfft(c)
# rebuild original function
spots2 = np.zeros(N, complex)
for n in range(N):
    for k in range(N//2+1):
        spots2[n] += c[k] * cmath.exp(2j*cmath.pi*k*n/N)
    for k in range(N//2+1,N,1):
        spots2[n] += c[N-k] * cmath.exp(2j*cmath.pi*k*n/N)

spots2 = spots2*1./N

#plots the reconstructed function "without noise" 
a,=plt.plot(mon,spots)
b,=plt.plot(mon,spots2,color="red",linewidth=1)
plt.xlabel("Time $t$",fontsize=20)
plt.ylabel("$f(t)$",fontsize=20)
#plt.xlim(0,1024)
plt.legend([a,b],["Signal","De-noised signal"],loc="lower left", fontsize=15)
plt.tight_layout()
plt.show()