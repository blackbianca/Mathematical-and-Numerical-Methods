import numpy as np
import matplotlib.pyplot as plt 

m1, m2 = np.genfromtxt("time_BHillustris1_30.dat", usecols=(6,7), unpack=True, max_rows=int(1e4))

N = int(len(m1))

for i in range(N):
    if (m1[i] < m2[i]):
        m1[i], m2[i] = m2[i], m1[i]

binx = np.linspace(0.5, 44.5, 45)
biny = np.linspace(0.5, 44.5, 45)

z = np.zeros([len(binx), len(biny)], float)

for i in range(N):
    index1 = int(m1[i])
    index2 = int(m2[i])

    z[index1][index2] += 1

z = np.transpose(z)

fig = plt.figure(figsize=plt.figaspect(0.4))
ax1 = fig.add_subplot(1,2,1)

ax1 = plt.contourf(binx, biny, z, levels=100)

cbar1 = plt.colorbar(ax1, orientation="vertical",spacing="proportional")
cbar1.solids.set_edgecolor("face")
cbar1.set_label('Nmerg')
plt.xlabel("M$_1$ [M$_{\odot}$]")
plt.ylabel("M$_2$ [M$_{\odot}$]")


mtot = m1 + m2
mchirp = (m1*m2)**(3./5.) * mtot**(-1./5.)

z1, xedges, yedges = np.histogram2d(mchirp, mtot, bins=25, density=False)
z1 = np.transpose(z1)

x = np.zeros(len(xedges)-1, float)
y = np.zeros(len(yedges)-1, float)

for i in range(len(xedges)-1):
    x[i] = (xedges[i]+xedges[i+1])/2.
    y[i] = (yedges[i]+yedges[i+1])/2.

ax2 = fig.add_subplot(1,2,2)
ax2 = plt.contourf(x, y, z1, levels=100)

cbar2 = plt.colorbar(ax2, orientation="vertical",spacing="proportional")
cbar1.solids.set_edgecolor("face")
cbar2.set_label('Nmerg')
plt.xlabel("M$_{tot}$ [M$_{\odot}$]")
plt.ylabel("M$_ {chirp}$ [M$_{\odot}$]")


plt.tight_layout()
plt.show()