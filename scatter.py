import matplotlib.pyplot as plt
from matplotlib import cm #importing color map
import matplotlib.colors as colors
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams.update({'font.size': 8})


Z,m1,m2,delay=np.genfromtxt("time_BHillustris1_30.dat", usecols=(3,6,7,8),unpack=True, max_rows=int(1e4+1))
# Z is metallicity, m1 and m2 masses, delay is delay time


for i in range(len(m1)):
    if m1[i]<m2[i]:
        m1[i], m2[i] = m2[i], m1[i]
    

M=m1+m2
mchirp=(m1*m2)**(3./5.)*(m1+m2)**(-1./5.)

fig = plt.figure()
graph = fig.add_subplot(111, projection='3d',)

ax = graph.scatter(M, Z, zs=delay, c=mchirp,cmap="viridis")

cbar = fig.colorbar(ax,orientation='vertical') 
cbar.solids.set_edgecolor("face") # edgecolor is the line that separates che spots, looks ugly, so we put this command to make it invisible
cbar.set_label('M$_{chirp}$ [M$_\odot$]')

#plt.xlabel("m$_{tot}$ [M$_\odot$]")
#plt.ylabel("metallicity Z")
#plt.zslabel("delay time [Gyr]")

graph.set_xlabel("m$_{tot}$ [M$_\odot$]")
graph.set_ylabel("metallicity Z")
graph.set_zlabel("delay time [Gyr]")


plt.show()