def horner(poly, n, x):
    result = poly[0]

    for i in range(1, n):
        result = result * x + poly[i]

    return result

#test
poly = [-0.00015375 , 0.00267583 ,-0.01744208 , 0.05244917 ,-0.07091417,  0.023575,
  0.89538]
n = len(poly)
x = 0.0848

print("Gia tri:", horner(poly, n, x))