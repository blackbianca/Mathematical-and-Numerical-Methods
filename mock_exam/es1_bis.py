import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.colors as colors

fname = "data_BBHs_0.0002.txt"
m1, m2 = np.genfromtxt(fname, dtype=float, usecols=(3,4), skip_header=1, unpack=True)

plt.scatter(m1,m2,s=0.1,color="red", label="dataset")
plt.legend()
plt.tight_layout()
plt.show()


tol=1e-2
for i in range(int(len(m1))):
    if(m1[i]<tol):
        m1[i] = tol
    if(m2[i]<tol):
        m2[i] = tol


min1 = min(m1)
max1 = max(m1)

if (min1<tol):
    min1 = tol

logbins = np.logspace(np.log10(min1), np.log10(max1), 50)
plt.hist2d(m1,m2,bins=logbins, norm=colors.LogNorm())
plt.xlabel("$M_1$ [$M_{\odot}$]")
plt.ylabel("$M_2$ [$M_{\odot}$]")
cbar = plt.colorbar()
cbar.set_label("N of BHS per cell")
plt.tight_layout()
plt.show()