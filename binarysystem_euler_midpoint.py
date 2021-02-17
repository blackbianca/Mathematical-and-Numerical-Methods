import numpy as np
import matplotlib.pyplot as plt

G = 1.

def accel(N, x, m):
    a = np.zeros([N,2], float)
    for i in range(N):
        for j in range(N):
            if(i!=j):
                rij = np.linalg.norm((x[i,:]-x[j,:]))
                a[i,:] += - G * m[j] * (x[i,:] - x[j,:])/rij**3.

    return a


def eul_steppos(N, x, v, h):
    for i in range(N):
        x[i,:] = x[i,:] + v[i,:]*h
    return x

def mid_steppos(N,v,x,h):
    k1 = np.zeros([N,2], float)
    k2 = np.zeros([N,2], float)
    #a = accel(N, x)
    #for i in range(N):
    #    k1[i,:] = h/2. * v[i, :]
    #    k2[i,:] = h * (v[i,:] + k1[i,:])
    #    x[i,:] += k2[i,:]
    k1 = h/2. * v 
    k2 = h * v
    x = x + k2
    return x

def eul_stepvel(N,a,v,h):
    for i in range(N):
        v[i,:] = v[i,:] + a[i,:]*h
    return v

def mid_stepvel(N,v,x,h):
    k3 = np.zeros([N,2], float)
    k4 = np.zeros([N,2], float)
    a = accel(N, x, m)
    #for i in range(N):
    #    k3[i,:] = h/2. * a[i, :]
    
    #for i in range(N):
    #    k4[i,:] = h * a2[i,:]
    #    v[i,:] += k4[i,:]
    k3 = h/2. * a
    a2 = accel(N, x+k3, m)
    k4 = h * a2
    v = v + k4
    return v

# main
N = int(2)
m = [1., 1.]
eul_x = np.array([[1.0,1.0], [-1.0,-1.0]], float)   # (x,y)_1 and (x,y)_2
eul_v = np.array([[-0.5,0.], [0.5,0.0]], float)     # initial velocities

mid_x = np.copy(eul_x)
mid_v = np.copy(eul_v)

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

mid_x1=[]
mid_x2=[]
mid_y1=[]
mid_y2=[]

while(t<t_f):

    #f.write(str(t+h)+" ")
    #for i in range(len(x)):
    #    f.write(str(x[0,0])+" "+str(x[0,1])+" "+str(v[0,0])+" "+str(v[0,1])+str(x[1,0])+" "+str(x[1,1])+" "+str(v[1,0])+" "+str(v[1,1]))
    #f.write("\n")

    a = accel(N, eul_x, m)
    
    eul_x = eul_steppos(N, eul_x, eul_v, h)
    eul_v = eul_stepvel(N, a, eul_v, h)

    #♣old = np.copy(mid_x)

    mid_x = mid_steppos(N, mid_v, mid_x, h)
    mid_v = mid_stepvel(N, mid_v, mid_x, h)

    t+=h
    
    eul_x1.append(eul_x[0,0])
    eul_y1.append(eul_x[0,1])
    eul_x2.append(eul_x[1,0])
    eul_y2.append(eul_x[1,1])

    mid_x1.append(mid_x[0,0])
    mid_y1.append(mid_x[0,1])
    mid_x2.append(mid_x[1,0])
    mid_y2.append(mid_x[1,1])

    
#f.close()

plt.scatter(eul_x1,eul_y1, color="blue", s=1, label="Euler")
plt.scatter(eul_x2,eul_y2, color="blue", s=1)
plt.xlabel("$\mathrm{x}$")
plt.ylabel("$\mathrm{y}$")

plt.scatter(mid_x1,mid_y1, color="red", s=1, label="Midpoint")
plt.scatter(mid_x2,mid_y2, color="red", s=1)
plt.xlabel("$\mathrm{x}$")
plt.ylabel("$\mathrm{y}$")

plt.legend()
plt.tight_layout()
plt.show()

