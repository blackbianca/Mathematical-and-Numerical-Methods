import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.colors as colors

chirpm = np.genfromtxt("chirpmass_bin.dat")
tmerg = np.genfromtxt("tmerg_bin.dat")
Z = np.genfromtxt("chirpmass_tmerg_tot.dat")

cs = plt.contourf(tmerg, chirpm, Z, cmap="Reds", norm = colors.LogNorm())
cbar = plt.colorbar(cs, orientation="vertical")
cbar.solids.set_edgecolor("face")
cbar.set_label("Number of BNSs per cell")

plt.xlabel("t$_{merg}$ [Gyr]")
plt.ylabel("m$_{chirp}$ [M$_{\odot}$]")

plt.ylim(0., 40.)

plt.tight_layout
plt.show()
