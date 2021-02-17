import numpy as np 
import matplotlib.pyplot as plt 

Msun = 1.97e30 # = 1Msun/kg
ly = 1.057e-16 # = 1m/ly
yr = 3.154e7   # = 1yr/s

G = 6.67e-11*Msun*ly**3*yr**2
m1 = 30.
m2 = 30.
c = 1. # beacuse I'm working in lightyears per year
UA = 1.58125e-5

k = G**3*m1*m2*(m1 + m2)/c**5

def func(a,e):
    da = -64./5. * k/a**3./(1.-e**2)**3.5 * (1. + 73./24.*e**2 + 37./96.*e**4.)
    de = -304./15. * e *  k/a**4./(1.-e**2)**2.5 * (1 + 121./304.*e**2.)

    return da, de 

h = 1e3 
aLSO = 6.*G*(m1 + m2)/c**2
counter = int(0)
a = 1.58125e-5 #UA
e = 0.7
t = 0.

avec=[]
evec=[]
time=[]
tol = 1e-3

while((abs(a-aLSO)/aLSO>1e-1) and (counter<1e5)): 
    
    avec.append(a)
    evec.append(e)
    time.append(t)
    
    da, de = func(a,e)
    anew = a + h*da  
    enew = e + h*de

    if(abs((anew-a)/a) < (0.1*tol)):
        h *= 2
        anew = a + h*da  
        enew = e + h*de  
    
    elif(abs(a-anew)/a > tol):
        while(abs(a-anew)/a > tol):
            h = h/10.
            anew = a + h*da
            enew = e + h*de

    a = anew 
    e = enew
    t += h 
    counter += 1

print(counter)

avec = np.array(avec, float)
avec = avec/UA

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax1 = plt.plot(time, avec)
ax1 = plt.xscale("log")
ax1 = plt.ylabel("a [AU]")

ax2 = fig.add_subplot(2,1,2)
ax2 = plt.plot(time, evec)
ax2 = plt.xscale("log")
ax2 = plt.xlabel("time [yr]")
ax2 = plt.ylabel("e")
plt.show()


    


