import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib import cm
from matplotlib.colors import LogNorm

plt.rcParams.update({'font.size': 15})

tmerg = np.genfromtxt("tmerg_bin.dat")
chirpm = np.genfromtxt("chirpmass_bin.dat")
Z = np.genfromtxt("chirpmass_tmerg_tot.dat")

x=np.zeros(len(tmerg))
y=np.zeros(len(chirpm))
for i in range(len(tmerg)-1):
    x[i]=(tmerg[i]+tmerg[i+1])/2. # storing the middle points of the bin
for i in range(len(chirpm)-1):
    y[i]=(chirpm[i]+chirpm[i+1])/2.

x[len(tmerg)-1]=tmerg[len(tmerg)-1]
y[len(chirpm)-1]=chirpm[len(chirpm)-1]

cs = plt.contourf(x,y,Z,levels=100,cmap="Reds",drawedges=False,norm=LogNorm())
cbar = plt.colorbar(cs,orientation='vertical',spacing="proportional") # takes as argument the object returned by contour
cbar.solids.set_edgecolor("face") # edgecolor is the line that separates che spots, looks ugly, so we put this command to make it invisible
cbar.set_label('Number of black holes per cell')

#plt.xlim(0,14.0)
plt.ylim(0.0,40.0)
plt.xlabel("t$_{merg}$")
plt.ylabel("m$_{chirp}$")

plt.tight_layout() # this function automatically takes care of the box where the figure will appear, and sets it up properly, it's not mandatory
plt.show()