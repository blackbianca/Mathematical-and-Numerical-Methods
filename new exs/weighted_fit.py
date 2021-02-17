import numpy as np 
import matplotlib.pyplot as plt 

def data_set():
    x = np.logspace(0,4,10000)
    b = -2.0 
    a =3.0 
    y = 10.**a*x**b
    x = np.log10(x)
    y = np.log10(y)

    sigma = np.zeros(len(x), float)
    w = np.zeros(len(x), float)
    for i in range(len(y)):
        sigma[i] = 10*np.random.random()
        y[i] = np.random.normal(y[i],sigma[i])
        w[i] = 1./sigma[i]**2
    return x,y,w

def least_square(x,y,w):
    N = int(len(x))
    xm = sum(x*w)/sum(w) 
    ym = sum(y*w)/sum(w) 

    num = np.zeros(N, float)
    den = np.zeros(N, float)
    num[:] = w[:]*y[:]*(x[:]-xm)
    den[:] = w[:]*x[:]*(x[:]-xm)

    B = sum(num)/sum(den)
    A = ym - xm*B

    temp = np.zeros(N, float)
    temp[:] = (y[:]-A-B*x[:])**2. 

    sigma_y = np.sqrt(1./(N-1) * sum(temp))

    temp[:] = x[:]**2*w[:]
    D = sum(w)*sum(temp) - (sum(x*w))**2
    sigma_A = sigma_y*np.sqrt(sum(temp)/D)
    sigma_B = sigma_y*np.sqrt(N/D)


    return A,B,sigma_A,sigma_B,sigma_y


#------main-------#

xdata, ydata, err = data_set()
A,B,sigma_A,sigma_B,sigma_y = least_square(xdata,ydata,err)
print(sigma_y)
print(sigma_A)
print(sigma_B)

y = lambda x : A + B*x


plt.plot(xdata, y(xdata), label="fit", color="red")
plt.scatter(xdata, ydata, s=1., label="dataset")

labels = []
labels.append("A = {0:.4g}".format(A)+"$\pm${0:.4g}".format(sigma_A))
labels.append("B = {0:.4g}".format(B)+"$\pm${0:.4g}".format(sigma_B))
labels.append("$sigma$_y = {0:.4g}".format(sigma_y))

plt.legend(labels, loc='best', fontsize='small', 
          fancybox=True, framealpha=0.7, 
          handlelength=0, handletextpad=0)


plt.tight_layout()
plt.show()