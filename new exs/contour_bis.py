import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.colors import LogNorm 

m1, m2 = np.genfromtxt("time_BHillustris1_30.dat", usecols=(6,7), unpack=True, max_rows=int(1e5))

N1 = int(len(m1))
N2 = int(len(m2))

for i in range(N1):
    if (m1[i] < m2[i]):
        m1[i], m2[i] = m2[i], m1[i]


#binx = np.logspace(np.log10(0.5), np.log10(44.5), 45)
#biny = np.logspace(np.log10(0.5), np.log10(44.5), 45)

max1 = max(m1)
max2 = max(m2)
min1 = min(m1)
min2 = min(m2)

print(min1, max1)
print(min2, max2)

N = int(75)
dm1 = (max1-min1)/N
dm2 = (max2-min2)/N
binx = np.linspace(min1,max1+dm1,N)
biny = np.linspace(min2,max2+dm2,N)

z = np.zeros([N+1, N+1], float)

for i in range(N1):
    index1 = int((m1[i]-min1)/dm1)
    index2 = int((m2[i]-min2)/dm2)
    z[index1][index2] += 1

z = np.transpose(z)
tol = 1e-3
for i in range(len(binx)):
    for j in range(len(biny)):
        if(z[i,j]<tol):
            z[i,j] = 1e-3

z = z[0:-1, 0:-1]
print(len(binx))
print(len(biny))
print(z.shape)
cs = plt.contourf(binx, biny, z, levels=100, norm=colors.LogNorm())
#cs = plt.contourf(binx, biny, z, levels=100)
cbar = plt.colorbar(cs, orientation="vertical", spacing="proportional")
cbar.set_label("Nmerg")

plt.xlabel("m$_1$ [M$_\odot$]")
plt.ylabel("m$_2$ [M$_\odot$]")

plt.tight_layout()
plt.show()


