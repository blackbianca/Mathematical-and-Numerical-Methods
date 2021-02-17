import random as rn
import numpy as np

def func(x):
    y = np.sin(1./(x*(2.-x)))**2
    return y

N = [int(1e3), int(5e3), int(1e4), int(5e4), int(1e5), int(5e5), int(1e6), int(5e6)]
f = [0.] * int(N[-1])
s = 0.


for i in range(int(N[-1])):
    a = rn.random()
    f[i] = func(2*a)

I = [0.]*8


for k in range(len(I)):
    I[k] = 2./N[k]*sum(f[0:N[k]])

print(I)