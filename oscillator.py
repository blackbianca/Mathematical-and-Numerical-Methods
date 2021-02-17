import numpy as np

N=int(1e6)
T=100.
E=np.zeros(N,float)
Z=0.0
Em=0.0
beta=1./T
integ=np.arange(0,N,1)

E=integ+0.5
Exp = np.exp(-beta*E)
Z=sum(Exp)
Em=sum(E*Exp)

Em/=Z
print(Em)

#this is an example of avoiding for loops by using the properties of arrays