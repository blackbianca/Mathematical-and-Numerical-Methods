import numpy as np 

def myfunc(x):
    x = np.exp(1-x*x)
    return x

# the main

x = 0.1     # Ansatz
xold = 10.0 # variable in which I'm gonna store the old values of x
th = 1e-5   # threshold

counter = int(0)

Nmax = 1e4

while( (abs(xold-x)>th) and (counter <= Nmax)):  # here we ensure we exit the while loop in case of divergences
    xold = x        # assigning old value
    x = myfunc(x)   # computing new value

    counter+=1

if(counter < Nmax):
    print("x converged to", x,"after iterations", counter)
if(counter > Nmax):
    print("x did not converge after iterations", Nmax)


# HERE WE DO NOT REACH CONVERGENCE
# it will work if i use myfunc = sqrt(1-logx)