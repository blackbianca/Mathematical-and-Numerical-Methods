import numpy as np
from numpy import sqrt

print("ax^2+bc+c=0")
a = float(input("Insert a:    "))
b = float(input("Insert b:    "))
c = float(input("Insert c:    "))

x1 = (-b + sqrt(b**2-4*a*c))/(2*a)
x2 = (-b - sqrt(b**2-4*a*c))/(2*a)

y1 = 2*c/(-b-sqrt(b**2-4*a*c))
y2 = 2*c/(-b+sqrt(b**2-4*a*c))


print("x1=",x1,"x2=",x2)
print("y1=",y1,"y2=",y2)