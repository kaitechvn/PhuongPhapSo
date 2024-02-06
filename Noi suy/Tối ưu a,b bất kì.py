import math
import random

x = []
a = 1
b = 7.35
n = 7 # can tim 7 moc noi suy -> n = 6

# t = (2x - (b+a)) / (b-a)

for i in range(0,n+1):
    x.append(((b-a)*(math.cos((math.pi)*(2*i+1)/(2*(n+1))))+a+b)/2)

x.sort()
print(x)


