import math
x = [] # List
n = 2 # can tim 6 moc noi suy -> n = 5

for i in range(0,n+1):
    x.append(math.cos((math.pi)*(2*i+1)/(2*(n+1))))

x.sort() # Sort

print(x)