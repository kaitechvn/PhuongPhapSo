import numpy as np
np.set_printoptions(suppress=True)

y = [6.715	,6.842,	6.969,	7.096,	7.223,	7.35]


x = [-1.26577	,-2.29201	,-3.18016,	-3.87081,	-4.31704,	-4.48762]



n = len(x)
result = np.zeros([n, n + 1])
for i in range(n):
        result[i][0] = x[i]
        result[i][1] = y[i]
for j in range(1, n):
    for i in range(n - j):
        result[i][j + 1] = (result[i + 1][j] - result[i][j]) / (x[i + j] - x[i])


f = result[0 , 1:]
print(f)

s = np.zeros(n)
b = np.array([1, -x[0] ])
s[n-1] = f[0]
s[n-2:n] = s[n-2:n] + b*f[1]

b = np.append(b, 0)
for i in range(1,n-1):
    for j in range(len(b)-1, 0, -1):
        b[j] = b[j] - x[i] * b[j-1]
    s[n - len(b):n] = s[n - len(b):n] + b * f[i + 1]
    b = np.append(b, 0)

print(s)



