import numpy as np
import matplotlib.pyplot as plt

Msun= 1.97e30   #kg
ly = 1.057e-16  #meters
yr = 3.154e7    #seconds

G = 6.67e-11 * Msun * ly**3 *yr**2
c = 3e8 * ly * yr
m1 = 30.
m2 = 30.
aLSO = 6*G*(m1+m2)/c**2 # 3 times Schw radius (last stable orbit)

k = G**3*m1*m2*(m1+m2)/c**5

def eul(x, v, h):
    x = x + v * h
    return x

def der_a(a, e):
    da = -64./5. * k/(a**3*(1-e**2)**(7./2.)) * (1. + 73./24.*e**2 + 37./96.*e**4)
    return da

def der_e(a, e):
    de = -304./15.*e * k/(a**4*(1-e**2)**(5./2.)) * (1. + 121./304.*e**2)
    return de



# main

tol = 1e-2
h = 1e3 # 1000 years
hconst = 1e3
a = 1.
e = 0.7
count = 1
t = 0.

time = []
avec = []
evec = []
timeconst = []
aconst = []
econst = []

while((abs(a-aLSO)/aLSO>1e-1) and (count<1e5)):

    dadt = der_a(a, e)
    dedt = der_e(a, e)

    anew = eul(a, dadt, h)
    enew = eul(e, dedt, h)

    if(abs(a-anew)/a < 0.1*tol):
        h = h*2
        anew = eul(a, dadt, h)
        enew = eul(e, dedt, h)

    elif(abs(a-anew)/a > tol):
        while(abs(a-anew)/a > tol):
            h = h/10.
            anew = eul(a, dadt, h)
            enew = eul(e, dedt, h)

    a = anew
    e = enew

    t += h
    count += 1

    avec.append(a)
    evec.append(e)
    time.append(t)

print(count)

a = 1.
e = 0.7
count = 1
t = 0.

while((abs(a-aLSO)/aLSO>1e-1) and (count<1e6)):

    dadt = der_a(a, e)
    dedt = der_e(a, e)

    anew = eul(a, dadt, hconst)
    enew = eul(e, dedt, hconst)

    t += hconst
    count += 1

    aconst.append(anew)
    econst.append(enew)
    timeconst.append(t)

fig, axs = plt.subplots(2, 1, tight_layout=True)  # number of rows and columns, tight_layout improves the images displaying

axs[0].plot(time,avec, color = "blue", label = "adaptive step")
axs[0].plot(timeconst,aconst, color = "green", label = "constant step")
axs[0].set_ylabel("a (ly)")
axs[0].set_xlabel("time (s)")
axs[0].set_xscale("log")
plt.legend()

axs[1].plot(time, evec, color = "blue", label = "adaptive step")
axs[1].plot(timeconst,econst, color = "green", label = "constant step")
axs[1].set_ylabel("e")
axs[1].set_xlabel("time (s)")
axs[1].set_xscale("log")
plt.legend()

plt.tight_layout()
plt.show()

