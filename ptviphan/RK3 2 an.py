import math

import matplotlib.pyplot as plt

# Example
# y' = z , z'= -2z - 4y ( 0< x < 100 )

x = 24
y = 24
t = 0

h = 0.01

print ('t', '\t', '\t', 'x','\t', '\t' , 'y', '\n')
print (t, '\t', '\t', x, '\t', '\t', y)

def f(x,y,t):
    return y
def g(x,y,t):
    return 3

while ( t < 3 ):
    k1 = f(x,y,t)
    l1 = g(x,y,t)

    t1 = x + h/2
    x1 = x + (h/2) * k1
    y1 = y + (h/2) * l1

    k2 = f(x1,y1,t1)
    l2 = g(x1,y1,t1)

    t2 = t + h
    x2 = x - k1 + 2*k2
    y2 = y - l1 + 2*l2

    k3 = f(x2,y2,t2)
    l3 = g(x2,y2,t2)


    t = x + h
    x = x + (h/6)* (k1 + 4*k2 + k3)
    y = y + (h/6)* (l1 + 4*l2 + l3)

    #print(k1, k2, k3, k4)
    print(t, '\t',x, '\t', y)
    plt.plot(x,y, 'rs')


#plt.show()




