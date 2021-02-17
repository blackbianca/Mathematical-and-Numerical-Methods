import scipy.integrate as integrate
import matplotlib.pyplot as plt 

Mpc = 3.086e19  #Mpc to km

c = 3.e5/Mpc*1e-3
H0 = 67./Mpc
Om = 0.27
Ol = 0.73


integrand = lambda x: 1./((1.+x)**3*Om + Ol)**0.5 * c/H0

def lookback(z):
    cdist = integrate.quad(integrand, 0.0, z)
    ldist = (1+z)*cdist[0]

    return cdist[0], ldist


z = 10.

redshift = []
cdist = []
ldist = []

z = 30.

while(z>0.):

    cd, ld = lookback(z)

    redshift.append(z)
    cdist.append(cd)
    ldist.append(ld)


    z-=0.1

print(redshift)
print(cdist)
print(ldist)

a = plt.plot(redshift, cdist, color="red", linestyle="--")
b = plt.plot(redshift, ldist, color="blue")
plt.legend([a,b], ["Comoving distance", "Luminosity distance"], loc ="upper right")
plt.xlabel("Redshift")
plt.ylim([0.,140.])
plt.tight_layout()
plt.show()

