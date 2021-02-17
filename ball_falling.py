import math

print("Suppose a ball is falling from a tower of height h.")
h = int(input("Insert height of the tower (meters):  "))
t = int(input("Insert time passed (sec): "))

g = 9.81

s = 1/2 * g * t**2
t2 = math.sqrt(2*h/g)

print("The ball has covered a distance of", s, "meters")
print("The ball hits the ground after", t2, "seconds")