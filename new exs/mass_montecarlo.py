import numpy as np
import random as rn

pc = 3.086e16 #pc to m
G = 6.67e-11 *pc**-3
sigma = 1e4 *pc**-1
r_max = 10
Msun = 1.989e30
N = int(1e4)

#isothermal profile 

def isothermal(x):
    y = 2*sigma**2/G
    return y

s = 0. 
for i in range(N):
    a = rn.random()*r_max
    s += isothermal(a)

M = r_max/N*s 
print(M/Msun)

#NFW

rho_0 = 1e8
r_s = 10
r_max = 100*r_s
tol = 1e-6

def NFW(x):
    if (x<tol):
        x = 1e-6
    y = rho_0/(x/r_s * (1+x/r_s)**2) *4*np.pi*x**2
    return y

s = 0. 
for i in range(N):
    a = rn.random()*r_max
    s += NFW(a)

M = r_max/N*s 
print(M)
