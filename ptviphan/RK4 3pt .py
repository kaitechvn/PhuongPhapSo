import matplotlib.pyplot as plt

# Example
# y' = z , z'= -2z - 4y ( 0< x < 100 )

x = 1.23
y = 0.23
z = 0.12
t = 1

h = 0.1

print ('t', '\t', '\t', 'x', '\t', '\t', 'y','\t', '\t' , 'z', '\n')
print (t, '\t', '\t', x, '\t', '\t', y,'\t', '\t', z)

def f(x,y,z,t):
    return 1.3*x + 0.32*t*z + t*y + 1.23
def g(x,y,z,t):
    return z
def k(x,y,z,t):
    return x

while ( t < 2 ):
    k1 = f(x,y,z,t)
    l1 = g(x,y,z,t)
    m1 = k(x,y,z,t)

    t1 = t + h/2
    x1 = x + (h/2) * k1
    y1 = y + (h/2) * l1
    z1 = z + (h/2) * m1

    k2 = f(x1,y1,z1,t1)
    l2 = g(x1,y1,z1,t1)
    m2 = k(x1,y1,z1,t1)

    t2 = t + h/2
    x2 = x + (h/2) * k2
    y2 = y + (h/2) * l2
    z2 = z + (h/2) * m2

    k3 = f(x2,y2,z2,t2)
    l3 = g(x2,y2,z2,t2)
    m3 = k(x2,y2,z2,t2)


    t3 = t + h
    x3 = x + h * k3
    y3 = y + h * l3
    z3 = z + h * m3

    k4 = f(x3,y3,z3,t3)
    l4 = g(x3,y3,z3,t3)
    m4 = k(x3,y3,z3,t3)

    t = t + h
    x = x + (h/6)* (k1 + 2*k2 + 2*k3 + k4)
    y = y + (h/6)* (l1 + 2*l2 + 2*l3 +l4)
    z = z + (h/6)* (m1 + 2*m2 + 2*m3 +m4)

    print(t, '\t',x, '\t', y, '\t', z)


