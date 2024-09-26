"""
import math
a = int(input())
b = 2*a*math.pi
c = math.pi*a**2
print(round(b, 2))
print(round(c, 2))
"""
"""
import math
L = int(input())
T = 2*math.pi*(L/9.81)**(1/2)
print(round(T, 2))
"""
x = int(input())
y = int(input())
print(x, y)
x, y = y, x 
print(x, y)