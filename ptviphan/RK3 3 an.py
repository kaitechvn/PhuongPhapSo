import matplotlib.pyplot as plt

# Example
# y' = z , z'= -2z - 4y ( 0< x < 100 )

x = 20
y = 10
z = 7
t = 0

h = 0.1

print ('t', '\t', '\t', 'x', '\t', '\t', 'y','\t', '\t' , 'z', '\n')
print (t, '\t', '\t', x, '\t', '\t', y,'\t', '\t', z)

def f(x,y,z,t):
    return 0.5*x*(1-x/30) - (0.3*pow(x,2)*(y+z))/(1+2*pow(x,2))
def g(x,y,z,t):
    return -0.4*y + (0.35*pow(x,2)*y)/(1+2*pow(x,2))
def k(x,y,z,t):
    return -0.15*z + (0.25*pow(x,2)*y)/(1+2*pow(x,2)) + 0.5*y

count = 0
while ( t < 500 ):
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

    t2 = t + h
    x2 = x - k1 + 2*k2
    y2 = y - l1 + 2*l2
    z2 = z - m1 + 2*m2

    k3 = f(x2,y2,z2,t2)
    l3 = g(x2,y2,z2,t2)
    m3 = k(x2,y2,z2,t2)

    count = count + 1
    t = t + h
    x = x + (h/6)* (k1 + 4*k2 + k3)
    y = y + (h/6)* (l1 + 4*l2 + l3)
    z = z + (h/6)* (m1 + 4*m2 + m3)

    print(t, '\t',x, '\t', y, '\t', z)
print('\n',count)


