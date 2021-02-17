import numpy as np

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

I1 = float(0.)
I2 = float(0.)

x1 = np.linspace(0, r1_max, N)
h1 = float(x1[1]-x1[0])
x2 = np.linspace(1e-6, r2_max, N)
h2 = float(x2[1]-x2[0])

for i in range(1, N-1, 1):          # summing up from position 1 included to N-1 excluded
    I1 += isothermal(x1[i], sigma)

I1 += 0.5*(isothermal(x1[0], sigma) + isothermal(x1[-1], sigma))
I1 *= h1

for j in range(1, N-1, 1):
    I2 += NFW(x2[j], rho_0, r_s)

I2 += 0.5*( NFW(x2[0], rho_0, r_s) + NFW(x2[-1], rho_0, r_s) )
I2 *= h2

I1_true = 2*sigma**2/G * r1_max
I2_true = 4*np.pi*rho_0*r_s**3 * (np.log(101)+ 1./101 - 1)



print(float(I1/I1_true))
print(float(I2/I2_true))