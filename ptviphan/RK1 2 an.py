import matplotlib.pyplot as plt

# Example
# y' = z , z'= -2z - 4y ( 0< x < 100 )

x = 1.23
y = 0.23
t = 1

h = 0.1

print ('t', '\t', '\t', 'x', '\t', '\t', 'y', '\n')
print (t, '\t', '\t', x, '\t', '\t', y)

def f(x,y,t):
    return 1.3*x + 0.32*t +t*y +1.23
def g(x,y,t):
    return x


while ( t < 2 ):
    k1 = f(x,y,t)
    l1 = g(x,y,t)


    t = t + h
    x = x + h*k1
    y = y + h*l1

    print(t, '\t',x, '\t', y)


