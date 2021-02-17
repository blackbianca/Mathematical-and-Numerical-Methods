import numpy as np 
import matplotlib.pyplot as plt 

l = 1. 
Tc = 293. 
Th = 323.
N = int(100)
D = 4.25e-2
h = 0.001
a = 1./(N+1)

temp = np.zeros((N+1), float)
temp[0] = Th
temp[N] = Tc

for j in range(1, N, 1):
    temp[j] = (Th+Tc)/2.

tol = 1e-4
temp[N] = Tc
temp[0] = Th
k = h*D/a**2
x = np.linspace(0,1.,101)

plt.plot(x, temp, label="t = 0s")

t = 0.
while(t<=10.):
    for i in range(1,N,1):
        temp[i] = temp[i] + k*(temp[i+1] + temp[i-1] - 2*temp[i])

    if(abs(t-0.01)<tol):
        temp1 = np.copy(temp)

    elif(abs(t-0.1)<tol):
        temp2 = np.copy(temp)

    elif(abs(t-1.)<tol):
        temp3 = np.copy(temp)

    elif(abs(t-10.)<tol):
        temp4 = np.copy(temp)

    t += h

  
plt.plot(x, temp1, label="t = 0.01s")
plt.plot(x, temp2, label="t = 0.1s")
plt.plot(x, temp3, label="t = 1s")
plt.plot(x, temp4, label="t = 10s")

plt.show()