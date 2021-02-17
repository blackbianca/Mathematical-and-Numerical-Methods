import random as rn
import numpy as np
import matplotlib.pyplot as plt

def gauss(x, sigma):
    x = 1./(np.sqrt(2*sigma**2*np.pi))*np.exp(-x**2/(2.*sigma**2))
    return x

def box_mueller(Nmax, sigma):
    r = []
    theta = []
    x = []
    y = [] # x and y will both be gaussian distibuted variables

    rn.seed(190909)
    for i in range(int(Nmax)):
        a = rn.random()
        r.append(np.sqrt(-2*sigma**2*np.log(1-a)))

    for i in range(int(Nmax)):
        b = rn.random()
        theta.append(2*np.pi*b)

    x = r*np.cos(theta)
    y = r*np.sin(theta)

    return(x,y)

if __name__ == "__main__":
# main

    fig, axs = plt.subplots(1,2, tight_layout=True, figsize=plt.figaspect(0.5))

    xx = np.linspace(-8, 8, 100)
    x, y = box_mueller(1e5, 2.)

    axs[0].hist(x, bins=50, density=True)
    axs[0].plot(xx, gauss(xx, 2.), "r")
    axs[1].hist(y, bins=50, density=True)
    axs[1].plot(xx, gauss(xx, 2.), "r")

    plt.show()