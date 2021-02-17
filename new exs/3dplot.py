import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


met, m1, m2, time = np.genfromtxt("time_BHillustris1_30.dat", usecols=(3,6,7,8), unpack=True, max_rows=int(1e4))
mtot= m1+m2 
mchirp = (m1*m2)**(3./5.)*(m1+m2)**(-1./5.)

fig = plt.figure()
im = fig.add_subplot(111, projection='3d')

cs = im.scatter(mtot, met, time, c=mchirp, cmap=cm.viridis, linewidth=0, antialiased=False)
im.set_xlabel("M$_{tot}$ [M$_{\odot}$]")
im.set_ylabel("Z (metallicity)")
im.set_zlabel("t$_{merg}$ [Gyr]")

cbar = fig.colorbar(cs)
cbar.set_label("M$_{chirp}$ M$_{\odot}$]")

plt.tight_layout()
plt.show()

