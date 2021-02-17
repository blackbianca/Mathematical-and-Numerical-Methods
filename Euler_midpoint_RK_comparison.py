import numpy as np
import matplotlib.pyplot as plt

def func(x,t):
    y = - x**3 + np.sin(t)
    return y

#---------EULER-------------
t_i = 0.
t_f = 100.
h = 0.4
N = int((t_f-t_i)/h)

euler = [0.] * (N+1)
time = np.linspace(t_i, t_f, N)

for i in range(N):
    euler[i+1] = euler[i] + h* func(euler[i], time[i])

euler.pop(-1)



#------------MIDPOINT----------------

midpoint = [0.] * (N+1)
k1 = 0.
k2 = 0.

for i in range(N):
    k1 = h/2 * func(midpoint[i], time[i])
    k2 = h * func(midpoint[i]+k1,time[i]+h/2)
    midpoint[i+1] = midpoint[i] + k2

midpoint.pop(-1)

#-----------RUNGE-KUTTA4---------------

RK = [0.] * (N+1)
k1 = 0.
k2 = 0.
k3 = 0.
k4 = 0.

for i in range(N):
    k1 = h/2 * func(RK[i], time[i])
    k2 = h/2 * func(RK[i]+k1,time[i]+h/2)
    k3 = h * func(RK[i]+k2, time[i]+h/2)
    k4 = h * func(RK[i]+ k3, time[i]+h)
    RK[i+1] = RK[i] + 1./6. * (2*k1 + 4*k2 + 2*k3 + k4)

RK.pop(-1)

plt.plot(time, euler, color= "r", label="Euler")
plt.plot(time, midpoint, color= "g", label="midpoint")
plt.plot(time, RK, color= "b", label="4-th order RK")

plt.legend()
plt.tight_layout
plt.show()