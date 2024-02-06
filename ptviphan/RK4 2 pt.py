import math
import matplotlib.pyplot as plt

# Example
# y' = z , z'= -2z - 4y ( 0< x < 100 )

x = 0.8
y = 0.3
t = 0

h = 0.01

print ('t', '\t', '\t', 'x','\t', '\t' , 'y', '\n')
print (t, '\t', '\t', x, '\t', '\t', y)

def f(x,y,t):
    return x*(1-x)*(x-0.22)-0.2*x*y
def g(x,y,t):
    return 0.6*x*y - 0.45*y

while ( t < 100 ):
    k1 = f(x,y,t)
    l1 = g(x,y,t)

    t1 = t + h/2
    x1 = x + (h/2) * k1
    y1 = y + (h/2) * l1

    k2 = f(x1,y1,t1)
    l2 = g(x1,y1,t1)

    t2 = t + h/2
    x2 = x + (h/2) * k2
    y2 = y + (h/2) * l2

    k3 = f(x2,y2,t2)
    l3 = g(x2,y2,t2)

    t3 = t + h
    x3 = x + h * k3
    y3 = y + h * l3

    k4 = f(x3,y3,t3)
    l4 = g(x3,y3,t3)

    t = t + h
    x = x + (h/6)* (k1 + 2*k2 + 2*k3 + k4)
    y = y + (h/6)* (l1 + 2*l2 + 2*l3 +l4)

    #print(k1, k2, k3, k4)
    print(t, '\t',x, '\t', y)
    plt.plot(x,y, 'rs')


plt.show()




