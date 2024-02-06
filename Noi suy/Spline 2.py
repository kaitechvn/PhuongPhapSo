import math
import numpy as np

pi = math.pi

x = [0, pi/6, pi/4, pi/3, pi]
y = [0, 0.5, math.sqrt(2)/2, math.sqrt(3)/2, 0]
n = len(x)

alpha = np.zeros(n)
h = np.zeros(n-1)

for k in range(0, n-1):
    h[k] = x[k+1] - x[k]

alpha[0] = 1

for k in range(0, n-1):
    alpha[k+1] = 2 * (y[k+1] - y[k]) / h[k]

# xây dựng ma trận
A = np.zeros((n, n))
for i in range(n-1):
    A[i, i] = 1
    A[i, i+1] = 1
A = np.vstack((np.eye(1, n, k=0), A[:-1]))


# Solve the system of linear equations
m = np.linalg.solve(A, alpha)

print(f" m={m}.")

# tìm các hệ số k, bk, ck
a = np.zeros(n-1)
b = np.zeros(n-1)
c = np.zeros(n-1)
for k in range(0,n-1):
    a[k] = (m[k+1] - m[k]) / (2 * h[k])
    b[k] = (m[k] * x[k+1] - m[k+1] * x[k]) / h[k]
    c[k] = (-m[k]*pow(x[k+1],2) + m[k+1]*pow(x[k],2))/ (2*h[k]) + m[k]*h[k]/2 + y[k]

print(a)
print(b)
print(c)



