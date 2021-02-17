from numpy import sqrt
import numpy as np

t = int(input("Insert time: "))
h = int(input("Insert height: "))
g = 9.81

s = 0.5*g*t**2
t = float(sqrt(2*h/g)) 

print(s)
print(t)

