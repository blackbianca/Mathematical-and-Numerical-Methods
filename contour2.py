import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.colors import LogNorm


plt.rcParams.update({'font.size': 15})


m1,m2=np.genfromtxt("time_BHillustris1_30.dat", usecols=(6,7),unpack=True, max_rows=int(1e4))
#m1=m1[0:int(1e4)]
#m2=m2[0:int(1e4)]
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

fig = plt.figure()

cs=plt.contourf(binx,biny,nmerg, levels=10)
#cs=plt.contourf(binx,biny,nmerg, levels=100,norm = colors.LogNorm())

cbar = plt.colorbar(cs,orientation='vertical',spacing="proportional") # takes as argument the object returned by contour
cbar.solids.set_edgecolor("face") # edgecolor is the line that separates che spots, looks ugly, so we put this command to make it invisible
cbar.set_label('Nmerg')

plt.xlabel("m$_1$ [M$_\odot$]")
plt.ylabel("m$_2$ [M$_\odot$]")

plt.tight_layout() # this function automatically takes care of the box where the figure will appear, and sets it up properly, it's not mandatory
plt.show()



