import matplotlib.pyplot as plt

# Example
# y' = z , z'= -2z - 4y ( 0< x < 100 )

x = 0
y = 2
t = 0

h = 0.01

print ('t', '\t', '\t', 'x','\t', '\t' , 'y', '\n')
print (t, '\t', '\t', x, '\t', '\t', y)

def f(x,y,t):
    return y
def g(x,y,t):
    return -2*y - 4*x

while ( t < 100 ):
    k1 = f(x,y,t)
    l1 = g(x,y,t)

    t1 = t + h
    x1 = x + h * k1
    y1 = y + h * l1

    k2 = f(x1,y1,t1)
    l2 = g(x1,y1,t1)


    t = t + h
    x = x + (h/2)* (k1 + k2)
    y = y + (h/2)* (l1 + l2)

    print(t, '\t',x, '\t', y)
    plt.plot(x,y, 'rs')


plt.show()


