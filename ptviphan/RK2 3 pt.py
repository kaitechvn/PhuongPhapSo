import matplotlib.pyplot as plt

# Example
# y' = z , z'= -2z - 4y ( 0< x < 100 )

x = 20
y = 10
z = 7
t = 0

h = 0.1

print ('t', '\t', '\t', 'x','\t', '\t' , 'y', '\n')
print (t, '\t', '\t', x, '\t', '\t', y)

def f(x,y,z,t):
    return 0.5*x*(1-x/30) - (0.3*pow(x,2)*(y+z))/(1+2*pow(x,2))
def g(x,y,z,t):
    return -0.4*y + (0.35*pow(x,2)*y)/(1+2*pow(x,2))
def k(x,y,z,t):
    return -0.15*z + (0.25*pow(x,2)*y)/(1+2*pow(x,2)) + 0.5*y

while ( t < 500 ):
    k1 = f(x,y,z,t)
    l1 = g(x,y,z,t)
    m1 = k(x,y,z,t)

    t1 = t + h
    x1 = x + h * k1
    y1 = y + h * l1
    z1 = z + h * m1

    k2 = f(x1,y1,z1,t1)
    l2 = g(x1,y1,z1,t1)
    m2 = k(x1,y1,z1,t1)


    t = t + h
    x = x + (h/2)* (k1 + k2)
    y = y + (h/2)* (l1 + l2)
    z = z + (h/2)* (m1 + m2)

    print(t, '\t',x, '\t', y , '\t', z)
    plt.plot(x,y, 'rs')


plt.show()


