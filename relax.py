import numpy as np

def myfunc(x):
    x = 2.0 -np.exp(-x)
    return x

# the main

x = 0.0     # Ansatz
xold = 10.0 # variable in which I'm gonna store the old values of x
th = 1e-5   # threshold
w = 0.2     # trying overrelaxing

counter = int(0)

while(abs(xold-x)>th):
    xold = x        # assigning old value
    x = (1. + w )*myfunc(x) - w*x   # computing new value

    counter+=1
    print(x, counter)