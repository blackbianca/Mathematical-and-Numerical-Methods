import numpy as np
import matplotlib.pyplot as plt 

N = int(1e5)
sigma = 2.

data1 = []
data2 = []

for i in range(N):
    z1 = np.random.rand()
    z2 = np.random.rand()

    r = np.sqrt(-2*sigma**2*np.log(1-z1))
    theta = 2*np.pi*z2

    x = r*np.cos(theta)
    y = r*np.sin(theta)

    data1.append(x)
    data2.append(y)

fig = plt.figure(figsize=plt.figaspect(0.4))

ax1 = fig.add_subplot(1,2,1)
ax1 = plt.hist(data1, bins=100)

ax2 = fig.add_subplot(1,2,2)
ax2 = plt.hist(data2, bins=100)


plt.tight_layout
plt.show()

