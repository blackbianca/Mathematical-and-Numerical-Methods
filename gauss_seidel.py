import numpy as np

a = [[4.,-1.,1.],[-1.,4.,-2.],[1.,-2.,4.]]
A = np.array(a, float)

b = np.array([12.,-1.,5.], float)
#x = np.array([1.,1.,1.], float)
x = np.zeros(3, float)
xold = np.zeros(3, float)

temp = 0.0
p = 1.0
counter = int(0)
Nmax = int(1e5)
th = 1e-80

while((p > th) and (counter <= Nmax)):
    xold = np.copy(x)

    for i in range(len(x)):
        temp = b[i]
        for j in range(len(x)):
            if(j==i):
                continue
            else:
                temp -= A[i][j]*x[j]
        x[i] = 1./A[i][i] * temp

    counter += 1
    p = np.dot(x-xold,x-xold)**2
    print(p)


if(counter < Nmax):
    print("x converged to", x,"after iterations", counter)
if(counter > Nmax):
    print("x did not converge after iterations", Nmax)


    

