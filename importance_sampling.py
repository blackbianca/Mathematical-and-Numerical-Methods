import numpy as np
import random as rn
import matplotlib.pyplot as plt


#----------------IMPORTANCE SAMPLING------------------

def func(x):                    # weighted integrand function, corresponds to f(x)/w(x)
    f = 1./(np.exp(x) + 1.)
    return f

def p(y):                       # inverse random sampling formula
    x = y**2
    return x

w_int = 2.                      # intregral fo the weighting function


# main

w_int = 2.0                     # integral of the weighting function

N = int(5e6)
N1 = int(1e3)
N2 = int(5e3)
N3 = int(1e4)
N4 = int(5e4)
N5 = int(1e5)
N6 = int(5e5)
N7 = int(1e6)

Ni = [N1, N2, N3, N4, N5, N6, N7, N]

y = np.random.rand(N)

x = p(y)                        # calculating random points distibuted as p(x), i-e normalized w(x)
g = func(x)                     # g = f/w, to calculate average mean
g1 = func(x[0:N1])              # calculating only for the first 1e3 numbers
g2 = func(x[0:N2])
g3 = func(x[0:N3])
g4 = func(x[0:N4])
g5 = func(x[0:N5])
g6 = func(x[0:N6])
g7 = func(x[0:N7])

I = sum(g)*w_int/float(N)       # final integral
I1 = sum(g1)*w_int/float(N1)
I2 = sum(g2)*w_int/float(N2)
I3 = sum(g3)*w_int/float(N3)
I4 = sum(g4)*w_int/float(N4)
I5 = sum(g5)*w_int/float(N5)
I6 = sum(g6)*w_int/float(N6)
I7 = sum(g7)*w_int/float(N7)

Ii = [I1, I2, I3, I4, I5, I6, I7, I]


print(I, I2, I3, I4)


#----------------MEAN VALUE METHOD------------------

def complete(x):
    y = x**(-0.5)/(np.exp(x)+1)
    return y

Nm = [int(1e3), int(5e3), int(1e4), int(5e4), int(1e5), int(5e5), int(1e6), int(5e6)]
f = [0.] * int(Nm[-1])
s = 0.


for i in range(int(Nm[-1])):
    a = rn.random()
    f[i] = complete(a)

Im = [0.]*8


for k in range(len(Im)):
    Im[k] = 1./Nm[k]*sum(f[0:Nm[k]])

print(Im)


plt.plot(Ni, Ii, color='r', marker="o", label="Importance Sampling")
plt.plot(Nm, Im, color='b', marker="o", label="Mean Value")
plt.xscale("log")
plt.xlabel('N')
plt.ylabel('I')


plt.legend()
plt.show()