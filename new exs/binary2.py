import numpy as np 
import matplotlib.pyplot as plt 

m1 = 1.
m2 = 1.
G = 1.
m = np.array([m1, m2], float)
Nm = int(len(m))

# midpoint method

def acc(x, mass):
    a = np.zeros([2, Nm], float)
    for i in range(Nm):
        for j in range(Nm):
            if (i!=j):
                rij = np.linalg.norm(x[:,i]-x[:,j])
                a[:,i] -= G*mass[j]*(x[:,i]-x[:,j])/rij**3.
    return a

x = np.array([[1.,-1.],[1.,-1.]], float)    # x1, x2 on the first row, y1 y2 on the second row
v = np.array([[-0.5,0.5],[0.,.0]], float)

t = 0. 
t_f = 300. 
h = 0.01

x1 = []
x2 = []
y1 = []
y2 = []

while(t<t_f):

    x1.append(x[0,0])
    x2.append(x[0,1])
    y1.append(x[1,0])
    y2.append(x[1,1])

    a = acc(x, m)
    k1x = 0.5*h*v 
    k1v = 0.5*h*a

    a = acc(x + k1x, m)
    k2x = h*(v + k1v)
    k2v = h*a 

    x = x + k2x 
    v = v + k2v 

    t += h 

plt.plot(x1, y1)
plt.plot(x2, y2)

plt.tight_layout()
plt.show()