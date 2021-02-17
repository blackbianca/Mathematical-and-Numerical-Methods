import numpy as np
import matplotlib.pyplot as plt 

# main
M = int(100)
V = 1.
phi = np.zeros([M+1, M+1], float)
phi[0,:] = V

tol = 1e-3
norm = 10.
counts = 0.
w = 0.9

while(norm > tol):
    phiold = np.copy(phi)
    for i in range(1, M, 1):
        for j in range(1, M, 1):
            phi[i,j] = (1+w)/4.*(phi[i+1,j]+phi[i-1,j]+phi[i,j+1]+phi[i,j-1]) -w*phi[i,j]

    norm = np.linalg.norm(phi-phiold)
    counts += 1

print(counts)

plt.imshow(phi)
plt.gray()
plt.show()