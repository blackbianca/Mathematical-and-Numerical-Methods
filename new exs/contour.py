import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

chirpm = np.genfromtxt("chirpmass_bin.dat")
tmerg = np.genfromtxt("tmerg_bin.dat")
Z = np.genfromtxt("chirpmass_tmerg_tot.dat")
#print(Z)


Ny = int(len(chirpm))
Nx = int(len(tmerg))

x = np.zeros(Nx, float)
y = np.zeros(Ny, float)


for i in range(1, Ny, 1):
    y[i] = (chirpm[i]+chirpm[i-1])/2. 
for j in range(1, Nx, 1):
    x[j] = (tmerg[j]+tmerg[j-1])/2. 

tol = 1e-5

for j in range(Nx):
    if (x[i]<tol):
        x[i]=1e-5
#    x[i] = np.log10(x[i])

for j in range(Ny):
    if (y[i]<tol):
        y[i]=1e-5
#    y[i] = np.log10(y[i])

a = len(Z[0,:])
b = len(Z[:,0])

for i in range(b):
    for j in range(a):
        if (Z[i,j]<tol):
            Z[i,j] = 1e-5
#        Z[i,j] = np.log10(Z[i,j])

#cs = plt.contourf(x, y, Z, levels=25, cmap="Reds")
cs = plt.contourf(x, y, Z, levels=100, cmap="Reds", norm = colors.LogNorm())
cs.zscale=("log")
cbar = plt.colorbar(cs, orientation="vertical")
cbar.solids.set_edgecolor("face")
cbar.set_label("Number of BNSs per cell")

plt.ylim(0., 40.)

plt.xlabel("t$_{merg}$ [Gyr]")
plt.ylabel("m$_{chirp}$ [M$_{\odot}$]")

plt.tight_layout
plt.show()

