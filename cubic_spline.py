import numpy as np
import matplotlib.pyplot as plt 

N = 18

def kappa(x,y):
    A = np.zeros([N-2,N-2], float)
    b = np.zeros(N-2, float)
    for i in range(N-2):
        j = i+1
        if(i==0):
            A[i,i] = 2.*(x[j-1]-x[j+1])
            A[i,i+1] = x[j]-x[j+1]
        elif(i==N-3):
            A[i,i] = 2.*(x[j-1]-x[j+1])
            A[i,i-1] = x[j-1]-x[j]
        else:
            A[i,i] = 2.*(x[j-1]-x[j+1])
            A[i,i-1] = x[j-1]-x[j]
            A[i,i+1] = x[j]-x[j+1]

        b[i] = 6.*(y[j-1]-y[j])/(x[j-1]-x[j]) - 6.*(y[j]-y[j+1])/(x[j]-x[j+1])

    k = np.linalg.solve(A, b)

    kk = np.zeros(N, float)
    kk[0] = 0.
    for i in range(N-3):
        kk[i+1] = k[i]
    kk[N-1] = 0.

    return kk

def spline(xinterp,k,x,y):

    # here we need to understand between which point xinterp belongs!
    # if xinterp is between i and i+1, then to compute yinterp we need to use f(i,i+1)
    for n in range(len(x)-1):
        if(xinterp>=x[n]) and (xinterp<x[n+1]):
            i=n

    yinterp = k[i]/6.*((xinterp-x[i+1])**3/(x[i]-x[i+1])-(x[i]-x[i+1])*(xinterp-x[i+1])) - k[i+1]/6.*((xinterp-x[i])**3/(x[i]-x[i+1])-(x[i]-x[i+1])*(xinterp-x[i])) + (y[i]*(xinterp-x[i+1])-y[i+1]*(xinterp-x[i]))/(x[i]-x[i+1])
    return yinterp



#----------main-------------#

#creating fake data
x = np.arange(0,18,1.)
y = np.sin(x)

xinterp = np.linspace(x[0], x[-1], 100)
k = kappa(x, y)

print(len(k))
print(len(x))
print(len(xinterp))

yinterp = np.zeros(len(xinterp), float)
for i in range(len(xinterp)-1):
    yinterp[i] = spline(xinterp[i],k,x,y)


#---------plot-------------#


a=plt.scatter(xinterp,yinterp,color="red",marker='.',s=10)
b=plt.scatter(x,y,marker='o',s=30)

plt.legend([b,a],["Data","Interpolation"],loc="lower left",fontsize="14")
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.tight_layout()
plt.show()

