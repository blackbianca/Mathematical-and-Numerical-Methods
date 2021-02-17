import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.colors as colors

fname = "time_BHillustris1_30.dat"
m1, m2 = np.genfromtxt(fname, dtype=float, usecols=(6,7), comments="#", unpack=True)

N = int(len(m1))
for i in range(N):
    if (m1[i]<m2[i]):
        m1[i], m2[i] = m2[i], m1[i]

#------------------method-1----------------#

Z,xedges,yedges=np.histogram2d(m1,m2,bins=25,density=False)

x=np.zeros(len(xedges)-1)
y=np.zeros(len(xedges)-1)
for i in range(len(xedges)-1):
    x[i]=(xedges[i]+xedges[i+1])/2. # storing the middle points of the bin
    y[i]=(yedges[i]+yedges[i+1])/2.

# to have the matrix in the form needed by contourf you have to transpose
Z = np.transpose(Z)

cs = plt.contourf(x,y,Z, levels=25)
cbar = plt.colorbar(cs, orientation="vertical")
plt.tight_layout()
plt.show()


#--------------------method-2-------------------#

NN = int(25)
max1 = max(m1)
min1 = min(m1)
max2 = max(m2)
min2 = min(m2)

dm1 = (max1-min1)/NN
dm2 = (max2-min2)/NN


Z = np.zeros([NN,NN], float)
for i in range(N):
    index1 = int((m1[i]-1e-3-min1)/dm1)
    index2 = int((m2[i]-1e-3-min2)/dm2)
    Z[index1,index2] += 1

Z = np.transpose(Z)

binx = np.linspace(min1, max1, NN)
biny = np.linspace(min2, max2, NN)

cs = plt.contourf(x,y,Z, levels=25)
cbar = plt.colorbar(cs, orientation="vertical")
plt.tight_layout()
plt.show()