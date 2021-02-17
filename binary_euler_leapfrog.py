import numpy as np
import matplotlib.pyplot as plt

def accel(N, x):
    a = np.zeros([N,2], float)
    for i in range(N):
        for j in range(N):
            if(i!=j):
                rij = np.linalg.norm((x[i,:]-x[j,:]))
                a[i,:] += -(x[i,:] - x[j,:])/rij**3.
    return a


def eul_steppos(N, x, v, h):
    for i in range(N):
        x[i,:] = x[i,:] + v[i,:]*h
    return x

def leap_steppos(N,v,x,h):
    a = accel(N, x)
    for i in range(N):
        x[i,:] = x[i,:] + h*v[i,:] + h**2/2. * a[i,:]
    return x

def eul_stepvel(N,a,v,h):
    for i in range(N):
        v[i,:] = v[i,:] + a[i,:]*h
    return v

def leap_stepvel(N,a1,a2,v,h):
    for i in range(N):
        v[i,:] = v[i,:] + h/2.*(a1[i,:] + a2[i,:])
    return v

def energy(x, v):
    e = 1./4.*np.linalg.norm(v[0,:]-v[1,:])**2 - 1./abs(np.linalg.norm(x[0,:]-x[1,:]))
    return e

def momentum(x, v):
    L = v[0,0]*x[0,0] + v[0,1]*x[0,1] + v[1,0]*x[1,0] + v[1,1]*x[1,1]
    return L


# main
N = int(2)
eul_x = np.array([[1.0,1.0], [-1.0,-1.0]], float)   # (x,y)_1 and (x,y)_2
eul_v = np.array([[-0.5,0.], [0.5,0.0]], float)     # initial velocities

leap_x = np.copy(eul_x)
leap_v = np.copy(eul_v)

# we assume m1 = m2 = 1, G = 1

t = 0.
t_f = 300.
h = 0.01

#fname="binarystar.txt"
#f=open(fname,"w")
#f.write("#Time X1 Y1 Vx1 Vy1 X2 Y2 Z2 Vx2 Vy2\n")

eul_x1=[]
eul_x2=[]
eul_y1=[]
eul_y2=[]

leap_x1=[]
leap_x2=[]
leap_y1=[]
leap_y2=[]

eul_E = []
leap_E = []
eul_L = []
leap_L = []

while(t<t_f):

    #f.write(str(t+h)+" ")
    #for i in range(len(x)):
    #    f.write(str(x[0,0])+" "+str(x[0,1])+" "+str(v[0,0])+" "+str(v[0,1])+str(x[1,0])+" "+str(x[1,1])+" "+str(v[1,0])+" "+str(v[1,1]))
    #f.write("\n")

    a = accel(N, eul_x)
    eul_x = eul_steppos(N, eul_x, eul_v, h)
    eul_v = eul_stepvel(N, a, eul_v, h)

    leap_a1 = accel(N, leap_x)
    leap_x = leap_steppos(N, leap_v, leap_x, h)

    leap_a2 = accel(N, leap_x)
    leap_v = leap_stepvel(N, leap_a1, leap_a2, leap_v, h)

    eul_E.append(energy(eul_x, eul_v))
    eul_L.append(momentum(eul_x, eul_v))

    leap_E.append(energy(leap_x, leap_v))
    leap_L.append(momentum(leap_x, leap_v))

    t+=h
    
    eul_x1.append(eul_x[0,0])
    eul_y1.append(eul_x[0,1])
    eul_x2.append(eul_x[1,0])
    eul_y2.append(eul_x[1,1])

    leap_x1.append(leap_x[0,0])
    leap_y1.append(leap_x[0,1])
    leap_x2.append(leap_x[1,0])
    leap_y2.append(leap_x[1,1])

    
#f.close()

plt.scatter(eul_x1,eul_y1, color="blue", s=1, label="Euler")
plt.scatter(eul_x2,eul_y2, color="blue", s=1)
plt.xlabel("$\mathrm{x}$")
plt.ylabel("$\mathrm{y}$")

plt.scatter(leap_x1,leap_y1, color="red", s=1, label="leapfrog")
plt.scatter(leap_x2,leap_y2, color="red", s=1)
plt.xlabel("$\mathrm{x}$")
plt.ylabel("$\mathrm{y}$")

plt.legend()
plt.tight_layout()
plt.show()

num = int(300./0.01)
time = np.linspace(0,300., num)


eul_de=np.zeros(len(time),float)
for i in range(1,len(time)-1):
    eul_de[i]=abs((eul_E[i+1]-eul_E[i])/eul_E[i])

leap_de=np.zeros(len(time),float)
for i in range(1,len(time)-1):
    leap_de[i]=abs((leap_E[i+1]-leap_E[i])/leap_E[i])

eul_dl=np.zeros(len(time),float)
for i in range(1,len(time)-1):
    eul_dl[i]=abs((eul_L[i+1]-eul_L[i])/eul_L[i])

leap_dl=np.zeros(len(time),float)
for i in range(1,len(time)-1):
    leap_dl[i]=abs((leap_L[i+1]-leap_L[i])/leap_L[i])

plt.scatter(time,eul_de, color="blue", s=1, label="Euler")
plt.scatter(time,leap_de, color="red", s=1, label="leapfrog")
plt.xlabel("time")
plt.ylabel("$\mathrm{(E-E_{old})/E_{old}}$")

plt.legend()
plt.tight_layout()
plt.show()

plt.scatter(time,leap_dl, color="red", s=1, label="leapfrog")
plt.scatter(time,eul_dl, color="blue", s=1, label="Euler")
plt.xlabel("time")
plt.ylabel("$\mathrm{(L-L_{old})/L_{old}}$")

plt.legend()
plt.tight_layout()
plt.show()