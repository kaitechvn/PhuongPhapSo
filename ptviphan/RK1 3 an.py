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

    t = t + h
    x = x + h*k1
    y = y + h*l1
    z = z + h*m1

    print(t, '\t',x, '\t', y, '\t', z)


