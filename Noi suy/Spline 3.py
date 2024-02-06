import math
import numpy as np

x = [1, 2, 3, 4, 5]
y = [1, 0, -1, 2, 3]
n = len(x)

alpha = np.zeros(n)
h = np.zeros(n-1)

for k in range(0, n-1):
    h[k] = x[k+1] - x[k]

alpha[0] = (y[1] - y[0])/h[0] - 0
alpha[n-1] = 0 - (y[n-1] - y[n-2])/h[n-2]

for k in range(0, n-2):
    alpha[k+1] = (y[k+2] - y[k+1])/h[k+1] - (y[k+1] - y[k])/h[k]

# Create the matrix
A = np.zeros((n - 2, n))
for i in range(n - 2):
    A[i, i] = h[i] / 6
    A[i, i + 1] = (h[i] + h[i + 1]) / 3
    A[i, i + 2] = h[i + 1] / 6

h1 = h[0]
new_row = np.array([h1 / 3, h1 / 6] + [0] * (n - 2))
A = np.insert(A, 0, new_row, axis=0)

hn = h[-1]
last_row = np.array([0] * (n - 2) + [hn / 6, hn / 3])
A = np.append(A, [last_row], axis=0)

# Solve the system of linear equations
m = np.linalg.solve(A, alpha)

print(f" m={m}.")

print(alpha)
print(A)

# tìm các hệ số k, bk, ck
a = np.zeros(n-1)
b = np.zeros(n-1)
c = np.zeros(n-1)
d = np.zeros(n-1)

for k in range(0,n-1):
    a[k] = (m[k+1] - m[k]) / (6 * h[k])
    b[k] = (3*m[k]*x[k+1] - 3*m[k+1]*x[k])/ (6*h[k])
    c[k] = (-3*m[k]*pow(x[k+1],2) + 3*m[k+1]*pow(x[k],2))/ (6*h[k]) + (y[k]) + (y[k+1] - y[k])/h[k] - (m[k+1] - m[k])*h[k]/6
    d[k] = (m[k]*pow(x[k+1],3) - m[k+1]*pow(x[k],3))/ (6*h[k]) + (y[k]*x[k+1] - y[k+1]*x[k]) / h[k] + (m[k+1]*x[k] - m[k]*x[k+1])*h[k]/6

print(a)
print(b)
print(c)
print(d)



