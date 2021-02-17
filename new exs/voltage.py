import numpy as np 
import matplotlib.pyplot as plt 

V = 1.
N = int(100)
tol = 1e-3
phi = np.zeros([N+1,N+1], float)
norm = 10.
phi[0,:] = V 
w = 0.9

while(norm>tol):

    phi0 = np.copy(phi)

    for i in range(1,N,1):
        for j in range(1,N,1):
            phi[i,j] = 0.25*(1.+w) * (phi[i+1,j]+phi[i-1,j]+phi[i,j+1]+phi[i,j-1]) - w*phi[i,j]

    norm = np.linalg.norm(phi-phi0)

plt.imshow(phi)
plt.gray()
plt.show()