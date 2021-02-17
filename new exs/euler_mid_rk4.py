import numpy as np 
import matplotlib.pyplot as plt

def dfunc(x, t):
    y = -x**3 + np.sin(t)
    return y 

#euler method

t_0 = 0. 
t_f = 100 
x = 0. 
h = 0.4
eul = []

N = int((t_f-t_0)/h)

for i in range(N):
    x = x + h*dfunc(x, t_0+i*h)
    eul.append(x)

#midpoint method

t_0 = 0. 
t_f = 100 
x = 0.
mid = []

for i in range(N):
    k1 = 0.5*h*dfunc(x,t_0+i*h)
    k2 = h*dfunc(x+k1, t_0+i*h + h/2.)
    x = x + k2
    mid.append(x)

#RK 4th order method

t_0 = 0. 
t_f = 100 
x = 0.
rk = []

for i in range(N):
    k1 = 0.5*h*dfunc(x,t_0+i*h)
    k2 = 0.5*h*dfunc(x + k1, t_0 + i*h + h/2.)
    k3 = h*dfunc(x + k2, t_0 + i*h + h/2.)
    k4 = h*dfunc(x + k3, t_0 + (i+1)*h)
    x = x + 1./6.*(2.*k1 + 4.*k2 + 2.*k3 + k4)
    rk.append(x)

time = np.linspace(t_0, t_f, N)
plt.plot(time, eul, color="blue", label="Euler")
plt.plot(time, mid, color="green", label="midpoint")
plt.plot(time, rk, color="red", label="Runge-Kutta 4th order")

plt.xlabel("time")
plt.ylabel("x(t)")
plt.tight_layout()
plt.show()