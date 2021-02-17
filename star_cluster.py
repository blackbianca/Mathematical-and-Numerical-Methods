import random as rn
import numpy as np
import matplotlib.pyplot as plt
from salpeter import salpeter
from box_mueller import box_mueller

N = int(1e4)

mvec = salpeter(N, 150, 0.1)
Mtot = sum(mvec)
print(Mtot)

G = 6.67408e-11 * 1e-9 * 2e30 #grav const in units of km^3 Msun^-1 s^-2
a = 1.
phi = []
phi2 = []
theta = []
theta2 = []
radii = []

#rn.seed(190909)

# first we sample randomly the polar coordinates of the masses

for i in range(len(mvec)):
    q = rn.random()
    b = rn.random()
    c = rn.random()
    phi.append(2*np.pi*q)
    theta.append(np.arccos(1-2*b))
    radii.append(np.sqrt(a**2/(c**(-2./3.)-1)))

# then we use the imported function box_mueller to sample the
# velocities according to a maxwellian

vx, vy = box_mueller(N, 265.)
vz, useless = box_mueller(N, 2.)

vel = [0] * len(vx)

for j in range(len(vx)):
    vel[j] = np.sqrt( vx[j]**2 + vy[j]**2 + vz[j]**2 )

for i in range(len(mvec)):
    n = rn.random()
    m = rn.random()
    phi2.append(2*np.pi*n)
    theta2.append(np.arccos(1-2*m))

vx = vel * np.sin(theta2) * np.cos(phi2)
vy = vel * np.sin(theta2) * np.sin(phi2)
vz = vel * np.cos(theta2)



# kinetic energy
vel2 = [0] * len(vel)
for k in range(len(vel)):
    vel2[k] = vel[k] * vel[k]

vms = np.sqrt(sum(vel2)/len(vel))

K = 0.5*Mtot*vms # Msun * km^2 / s^2

# gravitational energy
R = sum(radii)/(len(radii)) # pc
R = R * 3.086e13 # from pc to km

W = 3./5. * G * Mtot**2 / R

# virial ratio
Q = 2*K/W
print(Q) # Q =/= 1 so the system is not at virial equilibrium

vx = vx/np.sqrt(Q)
vy = vy/np.sqrt(Q)
vz = vz/np.sqrt(Q)  # virilized system


fig, axs = plt.subplots(2, 2)

r_min = min(radii)
r_max = max(radii)
logbins1 = np.logspace(np.log10(r_min),np.log10(r_max),25)
axs[0][0].hist(radii, bins = logbins1, density=True, histtype = "step", log=True)
axs[0][0].set_xscale("log")
#axs[0][0].set_yscale("log") 
# no need for previous line since stating log=True in the hist already implies the y axis is log
#axs[0][0].set_xlim(0, 2)
axs[0][0].set_xlabel('r (pc)')
axs[0][0].set_ylabel('PDF')
#axs[0][0].grid(True)

v_min = min(vel)
v_max = max(vel)
logbins2 = np.logspace(np.log10(v_min),np.log10(v_max),25)
axs[0][1].hist(vel, bins=logbins2, density=True, histtype = "step", log=True)
axs[0][1].set_xscale("log")
#axs[0][1].set_xlim(0, 2)
axs[0][1].set_xlabel('v (km/s)')
axs[0][1].set_ylabel('PDF')
#axs[0][1].grid(True)

Nbin=100
rho=np.zeros(Nbin,float)
rbin=np.zeros(Nbin,float)      #defining an bins array for radii
rbin[0]=0.0                     #setting the first bin to begin at 0
delta=20./Nbin                  #setting a step delta (bin width), knowing that the values of radii spread around for about 20 pc
for i in range(1,Nbin,1):
    rbin[i]=rbin[i-1]+delta     #filling the bins


for i in range(len(radii)):
    for j in range(1,Nbin,1):
        if(radii[i]<rbin[j]):   #here we have to keep in mind that we made a randomic association betewwn the i-th mass and i-th radius
            rho[j]+=mvec[i]     #so when the radius is smaller than bin end, we put a mass inside the corresponding rho entry
                                #we're basically adding up every mass we find at a given radius bin j

xx=np.zeros(N,float)            #in this section we just write the theoretical function rho(r)
yy=np.zeros(N,float)            #in order to see if it fits our array rho
xx[0]=0.0
yy[0]=Mtot*(xx[0]/a)**3 * (1.+(xx[0]/a)**2)**(-1.5)
delta=20./N
for i in range(1,N,1):
    xx[i]=xx[i-1]+delta
    yy[i]=Mtot*(xx[i]/a)**3 * (1.+(xx[i]/a)**2)**(-1.5)

axs[1,0].step(rbin,rho,linewidth=3, color="orange")
axs[1,0].plot(xx,yy,color="green",linestyle="--")
#axs[1][0].set_xlim(0, 2)
axs[1][0].set_xlabel('r (pc)')
axs[1][0].set_ylabel('M(r) (M$_\odot$)')
#axs[1][0].grid(True)


x = radii * np.sin(theta) * np.cos(phi)
y = radii * np.sin(theta) * np.sin(phi)
z = radii * np.cos(theta)

axs[1][1].scatter(x, y, s = 0.5, color = "r")
#axs[1][1].legend(["s3","s4"],ncol=2)
#axs[1][1].set_xlim(0, 2)
axs[1][1].set_xlabel('x (pc)')
axs[1][1].set_ylabel('y (pc)')
#axs[1][1].grid(True)

fig.tight_layout()
plt.show()