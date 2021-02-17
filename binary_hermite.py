import numpy as np
import matplotlib.pyplot as plt

G = 1.

def accel(N,x,m):
    a = np.zeros([N, 2], float)
    rij = 0.
    for i in range(N):
        for j in range(N):
            if(i!=j):
                rij = np.linalg.norm((x[i,:]-x[j,:]))
                a[i,:] += -G * m[j] * (x[i,:]-x[j,:])/rij**3.

    return a

def jerk(N,x,v,m):
    j = np.zeros([N,2], float)
    xvx = 0.
    for i in range(N):
        for k in range(N):
            if(i!=k):
                rik = np.linalg.norm((x[i,:]-x[k,:]))
                xvx = np.dot((x[i,:]-x[k,:]),(v[i,:]-v[k,:]))
                j[i,:] += -G * m[k] * ((v[i,:] - v[k,:])/rik**3. - 3.*xvx*(x[i,:]-x[k,:])/rik**5.)
    return j

def predictor(N,x,v,m,h):
    xp=np.zeros([N,2],float)
    vp=np.zeros([N,2],float)
    a = accel(N,x,m)
    j = jerk(N,x,v,m)
    for i in range(N):
        xp[i,:] = x[i,:] + h*v[i,:] + 0.5*h**2*a[i,:] + h**3/6.*j[i,:]
    for i in range(N):
        vp[i,:] = v[i,:] + h*a[i,:] + 0.5*h**2*j[i,:]
    return xp, vp

def correct(N,x,v,m,h):
    a = accel(N,x,m)
    j = jerk(N,x,v,m)
    xp, vp = predictor(N,x,v,m,h)
    ap = accel(N,xp,m)
    jp = jerk(N, xp, vp, m)
    
    vold=np.copy(v) # need to make a copy of v because I'm going to overwrite it but I still need it for position
    v[:,:]=v[:,:]+0.5*h*(a[:,:]+ap[:,:])+(1./12.)*h*h* (j[:,:]-jp[:,:])
         
    x[:,:]=x[:,:]+0.5*h*(vold[:,:]+v[:,:])+(1./12.)*h*h*(a[:,:]-ap[:,:])
    return x,v


def leap_steppos(N, x, v, m, h):
    a = accel(N, x, m)
    for i in range(N):
        x[i,:] = x[i,:] + h*v[i,:] + h**2/2. * a[i,:]

    return x

def leap_stepvel(N, a1, a2, v, h):
    for i in range(N):
        v[i,:] = v[i,:] + h/2.*(a1[i,:] + a2[i,:])
    
    return v

# main

t = 0.
t_f = 300. 
h = 0.01
m = [1.,1.]
N = int(2)

leap_x = np.array([[1.0, 1.0], [-1.0, -1.0]], float)   # initializin a position matrix, with (x,y)_1 and (x,y)_2
leap_v = np.array([[-0.5,0.0],[0.5,0.0]], float)       # same with velocities

her_x = np.copy(leap_x)
her_v = np.copy(leap_v)

leap_x1 = []
leap_x2 = []
leap_y1 = []
leap_y2 = []

her_x1 = []
her_x2 = []
her_y1 = []
her_y2 = []

while(t < t_f):

    #----------------LEAP-FROG----------------#

    a1 = accel(N, leap_x, m)
    leap_x = leap_steppos(N, leap_x, leap_v, m, h)

    a2 = accel(N, leap_x, m)
    leap_v = leap_stepvel(N, a1, a2, leap_v, h)

    t += h

    leap_x1.append(leap_x[0,0])
    leap_x2.append(leap_x[1,0])
    leap_y1.append(leap_x[0,1])
    leap_y2.append(leap_x[1,1])

    #-------------HERMITE-----------------#


    xp, vp = predictor(N, her_x, her_v, m, h)
    her_x, her_v = correct(N, her_x, her_v, m, h)

    her_x1.append(her_x[0,0])
    her_x2.append(her_x[1,0])
    her_y1.append(her_x[0,1])
    her_y2.append(her_x[1,1])



plt.scatter(leap_x1, leap_y1, s=0.5, color="red", label="leap-frog")
plt.scatter(leap_x2, leap_y2, s=0.5, color="red")
plt.scatter(her_x1, her_y1, s=0.5, color="blue", label="Hermite")
plt.scatter(her_x2, her_y2, s=0.5, color="blue")
plt.legend()
plt.tight_layout()
plt.show()