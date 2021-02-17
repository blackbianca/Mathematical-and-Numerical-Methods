import numpy as np 

M = 5.974e27
m = 7.348e25 
G = 6.674e-8 
R = 3.844e10 
w = 2.662e-6

threshold = 1e-3
# looks like relaxation method does not work 

# bisection method

def func(x):
    y = G*M/x**2 - G*m/(R-x)**2 - w**2*x
    return y 

r1 = 1. 
r2 = R 
norm = 1.

while(norm>threshold):
    rm = 0.5*(r1+r2)
    fm = func(rm) 
    f1 = func(r1)

    if(fm*f1 > 0):
        r1 = rm
    else:
        r2 = rm

    norm = abs(r1-r2)

print((r1+r2)*0.5*1e-5) 


# newton rhapson

def dfunc(x):
    y = -2*G*M/x**3 - 2*G*m/(R-x)**3 - w**2
    return y

r = 1. 
rold = 1. 
norm = 1. 

while(norm>threshold):
    rold = r 
    r = r - func(r)/dfunc(r)

    norm = abs(r-rold)

print(r*1e-5)