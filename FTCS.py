import numpy as np
import matplotlib.pyplot as plt 

# main
M = int(100)
Th = 323
Tc = 273
phi = np.zeros((M+1), float)
phi[0] = Th
phi[M] = Tc

for j in range(1, M, 1):
    phi[j] = (Th+Tc)/2.

D = 4.25e-2
h = 0.001
a = 1./(M+1)
t = 0.
tf = 10.
k = h*D/a**2

thickness = np.linspace(0, 1., M+1)

plt.plot(thickness, phi, color="blue", label="t=0 s")

while(t<=tf):
    t += h
    for i in range(1,M,1):
        phi[i] = phi[i] + k*(phi[i+1]+phi[i-1]-2*phi[i])

    if(abs(t-0.01)<1e-4):
        plt.plot(thickness, phi, color="green", label="t=0.01 s")
    elif(abs(t-0.1)<1e-4):
        plt.plot(thickness, phi, color="yellow", label="t=0.1 s")
    elif(abs(t-1.)<1e-4):
        plt.plot(thickness, phi, color="orange", label="t=1 s")
    elif(abs(t-10.)<1e-4):
        plt.plot(thickness, phi, color="red", label="t=10 s")

plt.legend()
plt.tight_layout()
plt.show()