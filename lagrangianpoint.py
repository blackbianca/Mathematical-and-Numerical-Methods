import numpy as np

G = 6.674e-8
M = 5.974e27
m = 7.348e25
R = 3.844e10
w = 2.662e-6

def func(r):
    a = G*M/r**2 - G*m/(R-r)**2 - w**2 * r 
    return a

def funcder(r):
    b = - 2*G*M/r**3 - 2*G*m/(R-r)**3 - w**2
    return b

Nmax = 1e4


r = 1.
p = 10.
counter = int(0)

th = 1e-6


while((p > th) and (counter <= Nmax)):
    rp = r - func(r)/funcder(r)

    p = rp - r
    r = rp
    counter += 1
    

print(r*1e-5) # from cm to km