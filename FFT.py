import numpy as np
import matplotlib.pyplot as plt
from cmath import exp,pi
from numpy.fft import rfft,irfft

fname="sunspots.txt"

mon,spots = np.genfromtxt(fname,dtype="float", \
comments="#", usecols=(0,1), unpack=True)

#plt.plot(mon, spots, color="blue")
#plt.tight_layout()
#plt.show()

# calculates Fourier transform with FFT
N=len(spots)
c=rfft(spots)
cabs=(abs(c))
kk=[]
maxc=0.0
maxk=0

m = range(N)

# data plotting
plt.plot(m,spots)
plt.xlabel("Time $t$",fontsize=20)
plt.ylabel("$f(t)$",fontsize=20)
plt.xlim(0,1024)
plt.tight_layout()
plt.show()

# calculated frequency k/N corresponding to the max c_k
for k in range(N//2+1):
    if((cabs[k]>maxc) and (k>0)):
        maxc=cabs[k]
        maxk=k/float(N)
    kk.append(k)

    
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

#print(len(c))
spots2=irfft(c)
# notice that irfft takes a vector of lenght 2//N+1 but gives an
# output of dimensions N
#print(len(spots2))
#plots the reconstructed function "without noise" 
a,=plt.plot(m,spots)
m = range(N-1)
b,=plt.plot(m,spots2,color="red",linewidth=1)
plt.xlabel("Time $t$",fontsize=20)
plt.ylabel("$f(t)$",fontsize=20)
#plt.xlim(0,1024)
plt.legend([a,b],["Signal","De-noised signal"],loc="lower left", fontsize=15)
plt.tight_layout()
plt.show()

#kvec = []

#ck = np.zeros(N//2+1,complex)

#for m in range(N//2+1):
#    sum = 0.
#    for l in range(N):
#        sum += mon[l]*exp(-2j*pi*m*l/N)
#    ck[m] = sum
#    kvec.append(m)


#plt.plot(kvec, abs(ck), color="red")
#plt.tight_layout()
#plt.show()