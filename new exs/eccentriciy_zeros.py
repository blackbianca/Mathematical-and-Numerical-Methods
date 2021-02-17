import numpy as np

F = [np.pi/3]*3
ecc = [0.1, 0.7, 0.9]

#relaxation method

def func(x):
    y = F + ecc*np.sin(x)
    return y 


E = [10.]*3
Eold = [10.]*3
norm = 1.
th = 1e-5

while(norm>th):
    Eold = E
    E = func(E)
    norm = np.linalg.norm(E-Eold)

print(E)

#bisection method

F = np.pi/3
eccvalues = [0.1,0.7,0.9]
xmvec = []


for a in eccvalues:
    
    ecc = a

    x1 = 0.
    x2 = np.pi
    xm = 0.
    norm = 1.

    while(norm>th):
        xm = (x1+x2)/2.
        ym = xm - F - ecc*np.sin(xm)
        y1 = x1 - F - ecc*np.sin(x1)     


        if(ym*y1 > 0):
            x1 = xm
        else:
            x2 = xm 

        norm = np.linalg.norm(x1-x2) 

    xmvec.append(xm)

print(xmvec)

# newton-rhapsod method

F = [np.pi/3]*3
ecc = [0.1, 0.7, 0.9]

def ffunc(x):
    y = x - F  - ecc*np.sin(x)
    return y 

def dfunc(x):
    y = 1 - ecc*np.cos(x)
    return y


E = np.zeros(3, float)
Eold = np.copy(E)
norm = 1.
th = 1e-5

while(norm>th):
    Eold = E
    E = E - ffunc(E)/dfunc(E)
    norm = np.linalg.norm(E-Eold)

print(E)