import numpy as np

a = [[2.,1.,4.,1.], [3.,4.,-1.,-1.], [1., -4., 1., 5.], [2.,-2.,1.,3.]]
b = [-4.,3.,9.,7.]

a = np.array(a, float)
b = np.array(b, float)


N = int(len(b))
x = np.zeros(N, float)


for i in range(N):
    temp = a[i,i]

    a[i,:]/=temp
    b[i]/=temp

    for j in range(i+1, N, 1):
        temp = a[j,i]
        a[j,:] = a[j,:]-temp*a[i,:]
        b[j] = b[j]-temp*b[i]

# it is very important to set the temporary variable, otherwise 
# in both cycles we'll be modifying b with elements of a which 
# have already been modified!

for i in range(N-1, -1, -1):
    x[i] = x[i] +b[i]

    for j in range(N-1, i, -1):
        x[i] = x[i] - a[i,j]*x[j]

print(x)