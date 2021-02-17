import matplotlib.pyplot as plt
from matplotlib import cm #importing color map
import matplotlib.colors as colors
import numpy as np

plt.rcParams.update({'font.size': 15})


m1,m2=np.genfromtxt("time_BHillustris1_30.dat", usecols=(6,7),unpack=True, max_rows=int(1e4))
#m1,m2=np.genfromtxt("time_BHillustris1_30.dat", usecols=(6,7),unpack=True)
a=0.0

binx=np.zeros(50,float)
biny=np.zeros(50,float)
binx=np.arange(0.5,50.5,1)
biny=np.arange(0.5,50.5,1)
nmerg = np.zeros([len(binx),len(biny)], float)

for i in range(len(m1)):
    if m1[i]<m2[i]:
        m1[i], m2[i] = m2[i], m1[i]
    index1 = int(m1[i])
    index2 = int(m2[i])
    nmerg[index1][index2]+=1

nmerg = np.transpose(nmerg)


fig = plt.figure(figsize=plt.figaspect(0.4))
ax1 = fig.add_subplot(1, 2, 1)

ax1 = plt.contourf(binx,biny,nmerg, levels=100)

cbar = plt.colorbar(ax1,orientation='vertical',spacing="proportional") 
cbar.solids.set_edgecolor("face") # edgecolor is the line that separates che spots, looks ugly, so we put this command to make it invisible
cbar.set_label('Nmerg')
#axs[0].set_xlim(0, 2)
plt.xlabel("m$_1$ [M$_\odot$]")
plt.ylabel("m$_2$ [M$_\odot$]")
#ax1.grid(True)

Mt=m1+m2
mchirp=(m1*m2)**(3./5.)*(m1+m2)**(-1./5.)

Z,xedges,yedges=np.histogram2d(Mt,mchirp,bins=25,density=False)
x=np.zeros(len(xedges)-1)
y=np.zeros(len(yedges)-1)
for i in range(len(xedges)-1):
    x[i]=(xedges[i]+xedges[i+1])/2.
    y[i]=(yedges[i]+yedges[i+1])/2.

Z = np.transpose(Z)


ax2 = fig.add_subplot(1,2,2)
ax2 = plt.contourf(x,y,Z, levels=100)

cbar = plt.colorbar(ax2,orientation='vertical',spacing="proportional") 
cbar.solids.set_edgecolor("face") # edgecolor is the line that separates che spots, looks ugly, so we put this command to make it invisible
cbar.set_label('Nmerg')

plt.xlabel("M$_{tot}$ [M$_\odot$]")
plt.ylabel("m$_{chirp}$ [M$_\odot$]")


fig.tight_layout()
plt.show()