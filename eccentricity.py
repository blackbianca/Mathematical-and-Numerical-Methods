import numpy as np

def func(an, ecc, eccan):
    m = an - eccan + ecc*np.sin(eccan)
    return m

def funcder(ecc, eccan):
    b = ecc * np.cos(eccan) - 1.
    return b

Nmax = 1e4


#F = float(np.pi/3.)
F = np.pi
ecc = [0.1,0.7,0.9]
counter = int(0)
sol = []

th = 1e-6

for i in range(len(ecc)):
    e = ecc[i]
    x = 1.5
    p = 10.

    while((p > th) and (counter <= Nmax)):
        xp = x - func(F,e,x)/funcder(e, x)

        p = xp - x
        x = xp
        counter += 1

    sol.append(x)
    

print(sol)

