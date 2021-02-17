import numpy as np 
import matplotlib.pyplot as plt 

G = 1. 
def accel(m, x):
    N = len(m)
    a = np.zeros([N,2], float) # N is the number of bodies, 2 is the the space dimension
    for i in range(N):
        for j in range(N):
            if (j!=i):
                rij = np.linalg.norm(x[i,:]-x[j,:])
                a[i,:] -= G*m[j]*(x[i,:]-x[j,:])/rij**3.

    return a 

def energy(m, x, v):
    Ek = 0. 
    N = int(len(m))
    for n in range(N):
        vn = np.linalg.norm(v[n,:])
        Ek += 0.5*m[n]*vn**2
    U = 0. 
    for i in range(N):
        for j in range(N):
            if (j>i):
                rij = np.linalg.norm(x[i,:]-x[j,:])
                U -= G*m[i]*m[j]/rij
    return Ek+U

mass = [3.,4.,5.]

# fixing the origin at body 2
xvec = [[3.,4.],[0.,0.],[3.,0.]]
xvec = np.array(xvec, float)
vvec = [[0.,0.],[0.,0.],[0.,0.]]
vvec = np.array(vvec, float)

t = 0. 
tf = 5. 
h = 1e-5 

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
ene = []

while(t<tf):

    x1.append(xvec[0,0])
    y1.append(xvec[0,1])
    x2.append(xvec[1,0])
    y2.append(xvec[1,1])
    x3.append(xvec[2,0])
    y3.append(xvec[2,1])

    E = energy(mass, xvec, vvec)
    ene.append(E)

    k1x = h/2. * vvec
    k1v = h/2. * accel(mass, xvec)

    k2x = h * (vvec + k1v)
    k2v = h * accel(mass, xvec+k1x)

    xvec = xvec + k2x 
    vvec = vvec + k2v 


    t += h

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.show()

ene = np.array(ene, float)
eene = np.zeros(len(ene)-1, float)
time = np.zeros(len(ene)-1, float)

for k in range(len(ene)-1):
    eene[k] = ene[k+1]/ene[k] - ene[k]/ene[k]
    time[k] = k*h

plt.plot(time, eene)
plt.show()