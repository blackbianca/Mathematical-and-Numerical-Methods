import numpy as np 
import matplotlib.pyplot as plt 

m1 = 1.
m2 = 1.
G = 1.

def acc(x, mass):
    
    Nm = int(len(mass))
    a = np.zeros([2,Nm], float)
    for i in range(Nm):
        for j in range(2):
            if (j!=i):
                norm = np.linalg.norm(x[:,i]-x[:,j])
                a[:,i] -= G*mass[j]*(x[:,i]-x[:,j])/norm**3

    return a
    


t_0 = 0 
t_fin = 300. 
h = 0.01
N = int((t_fin-t_0)/h)
masses = [m1, m2]

pos = np.array([[1.,-1.],[1.,-1.]], float)    # x1, x2 on the first row, y1 y2 on the second row
vel = np.array([[-0.5,0.5],[0.,.0]], float)

x1 = []
x2 = []
y1 = []
y2 = []

#euler method

for i in range(N):
    
    x1.append(pos[0,0])
    x2.append(pos[0,1])
    y1.append(pos[1,0])
    y2.append(pos[1,1])
    
    a = acc(pos, masses)
    pos = pos + vel*h 
    vel = vel + a*h

#midpoint method


posm = np.array([[1.,-1.],[1.,-1.]], float)    # x1, x2 on the first row, y1 y2 on the second row
velm = np.array([[-0.5,0.5],[0.,.0]], float)

x1m = []
x2m = []
y1m = []
y2m = []

Nm = int(len(masses))
k1x = np.zeros([2,Nm], float)
k1v = np.zeros([2,Nm], float)
k2x = np.zeros([2,Nm], float)
k2y = np.zeros([2,Nm], float)


for i in range(N):
    
    x1m.append(posm[0,0])
    x2m.append(posm[0,1])
    y1m.append(posm[1,0])
    y2m.append(posm[1,1])

    a = acc(posm, masses)
    
    k1x = 0.5*h*velm 
    k1v = 0.5*h*a

    a = acc(posm + k1x, masses)

    k2x = h*(velm + k1v)
    k2v = h*a
    
    posm = posm + k2x
    velm = velm + k2v
    
plt.plot(x1, y1, color="blue", label="Euler")
plt.plot(x2, y2, color="blue")
plt.plot(x1m, y1m, color="red", label="midpoint")
plt.plot(x2m, y2m, color="red")

plt.legend()
plt.tight_layout()
plt.show()