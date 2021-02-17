import numpy as np 
import matplotlib.pyplot as plt 

G = 1. 
m1 = 1. 
m2 = 1.
m = np.array([m1,m2], float)



def acc(x, mass):
    Nm = int(len(mass))
    a = np.zeros([2,Nm], float)
    for i in range(Nm):
        for j in range(Nm):
            if(i!=j):
                rij = np.linalg.norm(x[:,i]-x[:,j]) 
                a[:,i] -= G*mass[j]*(x[:,i]-x[:,j])/rij**3. 
    return a

def energy(x,v,mass):
    Nm = int(len(mass))
    Ek = 0. 
    U = 0. 
    for i in range(Nm):
        Ek += 0.5*mass[i]*np.linalg.norm(v[:,i])**2
        for j in range(Nm):
            if (j>i):
                rij = np.linalg.norm(x[:,i]-x[:,j])
                U -= G*mass[i]*mass[j]/rij
    return Ek+U

#leapfrog method

x = np.array([[1.,-1.],[1.,-1.]], float)    # x1, x2 on the first row, y1 y2 on the second row
v = np.array([[-0.5,0.5],[0.,.0]], float)

t = 0. 
t_f = 300. 
h = 0.01

x1 = []
x2 = []
y1 = []
y2 = []
ene = []

while(t<t_f):

    x1.append(x[0,0])
    x2.append(x[0,1])
    y1.append(x[1,0])
    y2.append(x[1,1])
    ene.append(energy(x,v,m))

    a1 = acc(x,m) 
    x = x + h*v + h*h*0.5*a1 

    a2 = acc(x, m)
    v = v + h*0.5*(a1 + a2)

    t+=h

plt.plot(x1,y1, color="red", label="leapfrog")
plt.plot(x2,y2, color="red")

#euler method

x = np.array([[1.,-1.],[1.,-1.]], float)    # x1, x2 on the first row, y1 y2 on the second row
v = np.array([[-0.5,0.5],[0.,.0]], float)

t = 0.

x1e = []
x2e = []
y1e = []
y2e = []
enee = []

while(t<t_f):

    x1e.append(x[0,0])
    x2e.append(x[0,1])
    y1e.append(x[1,0])
    y2e.append(x[1,1])
    enee.append(energy(x,v,m))

    a = acc(x,m)
    x = x + h*v
    v = v + h*a

    t+=h

plt.plot(x1e,y1e, color="blue", label="Euler")
plt.plot(x2e,y2e, color="blue")

plt.legend()
plt.tight_layout()
plt.show()

num = int(t_f/h)+1
time = np.linspace(0, t_f+h, num)

for i in range(len(ene)-1):
    ene[i] = abs((ene[i+1]-ene[i])/ene[i])
    enee[i] = abs((enee[i+1]-enee[i])/enee[i])

ene[-1]=0. 
enee[-1]=0.

plt.scatter(time, ene, s=0.5, color="red", label="leapfrog")
plt.scatter(time, enee, s=0.5, color="blue", label="Euler")

plt.legend()
plt.tight_layout()
plt.show()