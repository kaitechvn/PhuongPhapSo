import numpy as np
from math import *
np.set_printoptions(suppress=True)

x = [4.5,4.625,4.75,4.875,5,5.125,5.25
]

y = [0.89538,0.88557,0.87518,0.86934,0.85692,0.85488,0.84192
]

n = len(x)
result = np.zeros([n, n + 1])
for i in range(n):
    result[i][0] = x[i]
    result[i][1] = y[i]
for j in range(1, n):
    for i in range(n - j):
        result[i][j + 1] = result[i + 1][j] - result[i][j]

f = result[0, 1:]
print(f)

s = np.zeros(n)
b = np.array([1, 0 ])
s[n-1] = f[0]
s[n-2:n] = s[n-2:n] + b * f[1]

b = np.append(b, 0)
for i in range(1,n-1):
    for j in range(len(b)-1, 0, -1):
        b[j] = b[j] - i * b[j-1]
    print(b)
    s[n - len(b):n] = s[n - len(b):n] + b * f[i + 1] / factorial(i+1)
    b = np.append(b, 0)


print(s)
