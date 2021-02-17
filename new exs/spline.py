import numpy as np 
import matplotlib.pyplot as plt 


def kappa(x,y): #calculates the k coefficients of the spline, see eq. 267 of lecture notes
    N=len(x)-2
    A=np.zeros([N,N],float)
    b=np.zeros([N],float)
    for m in range(N):
        i=m+1
        A[m,m]=2.*(x[i-1]-x[i+1])   #this is just the matrix of the final equation Ak = b
        b[m]=6.*((y[i-1]-y[i])/(x[i-1]-x[i])-(y[i]-y[i+1])/(x[i]-x[i+1]))   #known vector in the RHS
        if((m+1)<N):
            A[(m+1),m]=(x[i]-x[i+1])
            A[m,(m+1)]=(x[i]-x[i+1])
            
#notice that the matrix is symmetric!

    #print(A)
    #print(b)
    k=np.linalg.solve(A,b) #call LU decomposition
    kk=[0.]
    for i in range(len(k)):
        kk.append(k[i])
    kk.append(0)
    kk=np.array(kk)
    #print(kk[-2],kk[-1])
    return kk   #returns the k coefficients of the spline


#x are the real data
#xinterp is a support sample to plot the interpolation

def spline(key,xdata,ydata,xinterp):
    N = int(len(xdata))
    for n in range(N):
        if((xdata[n] <= xinterp) and (xinterp <= xdata[n+1])):
            i = n
            #print(i)
        else:
            continue 

    yinterp = key[i]/6.*((xinterp-xdata[i+1])**3/(xdata[i]-xdata[i+1])-(xdata[i]-xdata[i+1])*(xinterp-xdata[i+1])) - key[i+1]/6.*((xinterp-xdata[i])**3/(xdata[i]-xdata[i+1])-(xdata[i]-xdata[i+1])*(xinterp-xdata[i])) + (ydata[i]*(xinterp-xdata[i+1])-ydata[i+1]*(xinterp-xdata[i]))/(xdata[i]-xdata[i+1])

    return yinterp

#----------fake-data---------#

N = int(18)
xdata = np.arange(0,N,1.)
ydata = np.sin(xdata)

kk = kappa(xdata,ydata)

xinterp = np.linspace(xdata[0], xdata[-1], 500)
Nx = int(len(xinterp))
yinterp = np.zeros(Nx, float)

for j in range(Nx-1):
    yinterp[j] = spline(kk,xdata,ydata,xinterp[j])

plt.scatter(xdata,ydata,s=10.)
plt.scatter(xinterp, yinterp, s=2.)
plt.show()

#---------true-dataset------------#


fname = "evol_120msun_scattered.dat"
time,m = np.genfromtxt(fname,dtype="float", comments="#", usecols=(0,1), unpack=True)

NN = int(len(time))
#print(NN)

kk = kappa(time,m) 

tinterp = np.linspace(time[0], time[-1], 100)
Nt = int(len(tinterp))
minterp = np.zeros(Nt, float)

for j in range(Nt-1):
    minterp[j] = spline(kk,time,m,tinterp[j])

plt.scatter(time,m,s=10.)
plt.scatter(tinterp, minterp, color="orange")
plt.show()

