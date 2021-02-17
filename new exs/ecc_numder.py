import numpy as np 

ecc = np.array([0.1,0.7,0.9], float)
F = np.array([np.pi/3.]*3, float)
h = 0.01 

def func(x):
    y = x - F - ecc*np.sin(x)
    return y 

def dfunc(E):
    y = (func(E+h/2.)-func(E-h/2.))/h 
    return y

norm = 1. 
E = np.array([10.]*3,float) 
Eold = np.array([10.]*3,float) 
th = 1e-3

while(norm>th):
    Eold = E 
    E = E - func(E)/dfunc(E)
    norm = np.linalg.norm(Eold-E)

print(E)