import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.colors as colors

fname = "data_BBHs_0.0002.txt"
m1, m2 = np.genfromtxt(fname, usecols=(3,4), dtype=float, skip_header=1, unpack=True)

plt.scatter(m1,m2, s = 0.1)
plt.show()

plt.hist2d(m1,m2,bins=25, norm=colors.LogNorm())
cbar = plt.colorbar()
cbar.set_label("N")
plt.show()

mass1 = sum(m1)/len(m1)
mass2 = sum(m2)/len(m2)

sq1 = (m1-mass1)**2
s1 = np.sqrt(sum(sq1)/len(m1))

sq2 = (m2-mass2)**2
s2 = np.sqrt(sum(sq2)/len(m2))

print(mass1, s1)
print(mass2, s2)