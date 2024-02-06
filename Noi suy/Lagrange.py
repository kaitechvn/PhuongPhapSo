import numpy as np

np.set_printoptions(suppress=True)

a = np.array([3.2, 2, 1.6])
y = np.array([1, 2, 3])
n = len(a)
b = np.zeros(n+1)

# Gói tính tích
b[0] = 1
b[1] = -a[0]

for i in range (1,n):
    for j in range (n,0,-1):
        b[j] = b[j] - a[i] * b[j-1]

s = np.zeros(n)
# gói chia đa thức
for m in range(0,n):
    c = np.zeros(n+1)
    c[0] = 1
    for i in range (1,n+1):
        c[i] = a[m] * c[i-1] + b[i]
    c = np.delete(c,n)

    # gói tích mẫu dưới
    result = 1
    for j in range(0,n):
        if m == j:
            continue
        result = result * (a[m] - a[j])

    c = c * y[m] / result
    s = s + c

print(s)


