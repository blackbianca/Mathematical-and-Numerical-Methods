import numpy as np
import random as rn

Msun = float(1.989e30)
pc = float(3.086e16) 
G = float(6.67e-11) * pc**(-3) * Msun  #grav constant in Msun^-1 pc^3 s^-1
#print(G)

def isothermal(x, sigma):
    sigma = float(sigma)
    f = 2.*sigma**2/G
    return f

def NFW(x, rho_0, r_s):
    rho_0 = float(rho_0)
    r_s = float(r_s)
    f = 4.*np.pi*x**2 * rho_0/(x/r_s * (1+x/r_s)**2)
    return f


sigma = float(1e4) * 1./pc
#print(sigma)
rho_0 = float(10**8) * 1e-9
r_s = float(1e4)
r1_max = 10.
r2_max = 100. * r_s
N = int(input("Enter number of steps:   "))
N_count1 = int(0)
N_count2 = int(0)

I1 = float(0.)
I2 = float(0.)

h1 = 3*sigma**2/G

for i in range(int(N)):
    a = rn.random()
    y = a*h1
    b = rn.random()
    x = b * r1_max
    if(y < isothermal(x, sigma)):
        N_count1 += 1

A1 = h1 *r1_max

I1 = N_count1/N * A1

h2 = NFW(r_s, rho_0, r_s) 

for i in range(int(N)):
    a = rn.random()
    y = a*h2
    b = rn.random()
    x = b * r2_max
    if(y < NFW(x, rho_0, r_s)):
        N_count2 += 1

A2 = h2 * r2_max

I1 = N_count1/N * A1
I2 = N_count2/N * A2


print(I1, I2)