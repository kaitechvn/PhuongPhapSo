import numpy as np
from math import *
np.set_printoptions(suppress=True)

y = [3.1499801,3.169321,3.1959627,3.2306381,3.2739998,3.3266138

]

x = [3.8,3.9,4,4.1,4.2,4.3

]



yngang = 3.15
h = 0.1
eps = pow(10, -4)

# Tinh sai phan
n = len(x)
f = np.zeros([n, n + 1])
for i in range(n):
    f[i][0] = x[i]
    f[i][1] = y[i]
for j in range(1, n):
    for i in range(n - j):
        f[i][j + 1] = f[i + 1][j] - f[i][j]

delta = f[0, 2:]
print(delta)
# Phuong phap lap
t = (yngang - y[0])/delta[0]
print(t)
lap = 0
result = t

def Mul(s,i):
    kq = 1
    for i in range(0,i+1):
        kq = kq*(s-i)
    return kq

while (True):
    temp = result
    sum = 0
    lap = lap + 1
    for i in range(0,n-2):
        sum = sum - (delta[i+1] * Mul(result, i+1) / (delta[0] * factorial(i + 2)))
    result = t + sum
    print("Qua trình lap thu ", lap , result)
    if ( abs(result - temp) < eps):
        break

xngang = x[0] + h * result
print(xngang)
print(lap)

