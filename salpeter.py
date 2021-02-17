import random as rn
import numpy as np
import matplotlib.pyplot as plt

def salpeter(Nmax, m_max, m_min):

    alfa = 2.3
    exp = 1.-alfa
    massvec = []

    rn.seed(190909)
    for i in range(int(Nmax)):
        x = rn.random()
        m = (m_max**exp + m_min**exp*(1.-x))**(1./exp)
        massvec.append(m)

    return(massvec)


if __name__ == "__main__":
# main

    fig = plt.figure()

    #mybins=np.logspace(0.1,float(150),num=25)
    #plt.hist(mvec, bins=mybins, density=True,histtype='step',log=True)

    y = []
    z = []
    mvec = salpeter(1e6, 150., 0.1)


    hist, bins = np.histogram(mvec, bins = 25)
    logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
    plt.hist(mvec, bins=logbins, density=True, histtype = "step", log=True, label="Montecarlo" )

    #logbins = np.delete(logbins, len(logbins)-1)
    #hist = hist/logbins



    for i in range(len(mvec)):
        y.append(mvec[i]**(-2.3))
        #z.append(mvec[i]**(-1.3))

    plt.plot(mvec,y, "r", label="Salpeter's law")
    #plt.plot(mvec,z, "g")


    #plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('Stellar Mass M$_\odot$')
    plt.ylabel("Population")


    plt.legend()
    plt.show()