# A * x = b matrix problem

import numpy as np
N=4

a=[[2.,1.,4.,1.],[3.,4.,-1.,-1.],[1.,-4.,1.,5.],[2.,-2.,1.,3.]]

a = np.array(a,float)     #here i'm converting my list of lists into a numpy array, which is more usable
b = np.array([-4.,3.,9.,7.], float)  #same thing here with the known term

x = np.zeros(N, float)



for i in range(N):
    temp = a[i,i]
    #for j in range(N): # here either i can use a for loop on index j or i can just delete the k using arrays properties:
    # python will know there is a for loop. Instead of putting nothing i could also write ":". These simplification can be
    # done only with a simple for, with steps of 1, in the range of existence of the index. In fact, in the following, we will
    # omit only the simple range(N) loop
    a[i,]/=temp  # here dividing each line for the diagonal term
    b[i]/=temp

    for k in range(i+1,N):
        temp = a[k,i]
        #for j in range(N):
        a[k,] = a[k,] - temp*a[i,]
        b[k] = b[k] - temp*b[i]

print(a)
print(b)        # printing to check the matrix is upper diagonal

# back substitution
#--------------brutal way--------------#

#x[3] = b[3]
#x[2] = -a[2,3]*x[3] + b[2]
#x[1] = -a[1,2]*x[2] -a[1,3]*x[3] + b[1]
#x[0] = -a[0,1]*x[1] - a[0,2]*x[2] - a[0,3]*x[3] +b[0]

#----------smart way with the loop-----#

for i in range(N-1,-1,-1):     # in range command the right end (second argument) is always excluded. Third argument tells me I'm counting backwards
    x[i] = x[i] + b[i]
    for j in range(N-1,i,-1):  # first time i don't even enter this loop
        x[i] = x[i] - a[i,j]*x[j]

print(x)        # final solution
