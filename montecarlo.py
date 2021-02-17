import random as rn
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    y = np.sin(1./(x*(2.-x)))**2
    return y

def sqrt(x):
    y = x**0.5
    return y

N = [1e3, 5e3, 1e4, 5e4, 1e5, 5e5, 1e6, 5e6]
N_count = [0] * 8
I = [0.] * 8

for k in range(len(N)):
    for i in range(int(N[k])):
        a = rn.random()
        b = rn.random()
        if(a<func(2*b)):
            N_count[k] += 1


for j in range(len(I)):
    I[j] = float(N_count[j]/N[j]) * 2.

print(I)

res = [0]*8

for h in range(len(res)):
    res[h] = I[h] - I[7]

fig, axs = plt.subplots(1, 2)

axs[0].plot(N, I, color='r', marker="o")
axs[0].set_xscale("log")
axs[0].set_xlabel('N')
axs[0].set_ylabel('I')

axs[1].scatter(N, res, color="b")
axs[1].set_xscale("log")
axs[1].set_xlabel("N")
axs[1].set_ylabel("Residuals")

fig.tight_layout()
plt.show()