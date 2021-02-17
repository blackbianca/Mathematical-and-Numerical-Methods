import numpy as np

a = [[4.,-1.,1.],[-1.,4.,-2.],[1.,-2.,4.]]
A = np.array(a, float)

b = np.array([12.,-1.,5.], float)
#x = np.array([1.,1.,1.], float)
x = np.zeros(3, float)
xold = np.zeros(3, float)

th = 1e-10
norm = 10.

while(norm>th):
    xold = np.copy(x)
    for i in range(len(x)):
        temp = b[i]
        for j in range(len(x)):
            if j!=i:
                temp -= A[i,j]*x[j]
        x[i] = 1./A[i,i] * temp

    norm = np.linalg.norm(xold-x)

# I definde a temporary variable: I don't want to modify
# the vector b in any way because I'm gonna use i tmultiple times
# within the while cycle

print(x)