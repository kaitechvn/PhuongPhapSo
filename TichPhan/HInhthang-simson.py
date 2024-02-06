from sympy import sympify, symbols
from sympy import *
import math


# Công thức hình thang

def Hinh_thang(A):
    k = 1 / 2 * (A[0] + A[n])
    for i in range(1, n):
        k = k + A[i]
    print("Tích phân bằng công thức hình thang      :", k * h)


# sai số ct hình thang
def E_hinh_thang():
    m = max(f, 2)
    print("Sai số công thức hình thang              :", m / 12 * (b - a) * (h ** 2))


# Số khoảng chia để thỏa mãn sai số cho trước trong công thức hình thang
def skc_hinh_thang():
    m = max(f, 2)
    print((abs(((m * (b - a) ** 3) * (1 / 12) * (1 / eps)))) ** (1 / 2))
    print("Số khoảng chia cần thiết (Hình thang)    :",
          math.floor((abs(((m * (b - a) ** 3) * (1 / 12) * (1 / eps)))) ** (1 / 2)) + 1)


# Công thức Simpson

def simpson(A):
    simp_dau = A[0] + A[n]
    simp_odd = 0
    simp_even = 0
    for i in range(1, n, 2):
        simp_odd += A[i]
    for i in range(2, n, 2):
        simp_even += A[i]
    simp = h / 3 * (simp_dau + 4 * simp_odd +  2 * simp_even )
    print("Tích phân bằng công thức Simpson         :", simp)
    print("hệ số lẻ: ", simp_odd)
    print("hệ số chẵn: ", simp_even)
    print("hệ số đầu: ",simp_dau)


# sai số của ct simpson
def E_simpson():
    m = max(f, 4)
    print("Sai số công thức Simpson                 :", m / 180 * (b - a) * (h ** 4))


# số khoảng chia
def skc_simpson():
    m = max(f, 4)
    print((abs((m * (b - a) ** 5) * (1 / 180) * (1 / eps))) ** (1 / 4))
    n = math.floor((abs((m * (b - a) ** 5) * (1 / 180) * (1 / eps))) ** (1 / 4))
    if n % 2 == 1:
        print("Số khoảng chia cần thiết (Simpson)       :", n + 1)
    else:
        print("Số khoảng chia cần thiết (Simpson)       :", n + 2)


# Công thức Newton - Cotes

def multiply_horner(A, i) -> list:
    """ Nhân một đa thức với (x-i) """
    A.append(0)
    for j in range(len(A) - 1, 0, -1):
        A[j] = A[j] - A[j - 1] * i
    return A


def devide_horner(A, i) -> list:
    """ Chia một đa thức với (x-i) """
    X = A.copy()
    X.pop()
    for j in range(1, len(X)):
        X[j] = i * X[j - 1] + X[j]
    return X


def poly_integral(A, a, b) -> float:
    I = 0
    """ Tính tích phân xác định của đa thức """
    for j in range(0, len(A)):
        if (A[j] == 0):
            continue
        else:
            A[j] = A[j] / (len(A) - j)
        I = I + A[j] * (b ** (len(A) - j) - a ** (len(A) - j))
    return I


# tính hệ số H(i)
def H(i) -> float:
    X = devide_horner(D, i)
    h = (1 / n) * ((-1) ** (n - i)) / (math.factorial(i) * math.factorial(n - i)) * poly_integral(X, 0, n)
    return h


def newton_cotez() -> float:
    E = 0
    Hs = [1] * (n + 1)
    for i in range(0, n + 1):
        Hs[i] = H(i) * n
        E = E + Hs[i] * A[i]
    print(f'Hệ số Cotes ứng với n = {n}                :', Hs)
    print('Tích phân bằng công thức Newton - Cotez  :', E * (b - a))


# sai số newton_cotez
def E_newton_cotez() -> float:
    g = Derivative(f, (x, n), evaluate=True)
    if (n % 2 == 0):
        D1 = D.copy()
        multiply_horner(D1, n + 1)
        m2 = max(g, 2)
        print("Sai số công thức Newton - Cotez          :",
              abs(float(m2) * poly_integral(D1, 0, n) * (h ** (n + 3)) / math.factorial(n + 2)))
    else:
        m1 = max(g, 1)
        print("Sai số công thức Newton - Cotez          :",
              abs(float(m1) * poly_integral(D, 0, n) * (h ** (n + 2)) / math.factorial(n + 1)))


# tìm max của đạo hàm cấp i của hàm f sử dụng sympy
def max(fx, i):
    g = Derivative(fx, (x, i), evaluate=True)
    m1 = abs(maximum(g, x, Interval(a, b)))
    m2 = abs(minimum(g, x, Interval(a, b)))
    if m1 > m2:
        m = m1
    else:
        m = m2
    return m

def f(x):
    # Define your function here
    return  1/(1 + x**2)

def main():
    global n, a, b, f, h, x, D, A, eps
    de_bai = int(input('đề bài có cho hàm f không? (Nhập số theo bài toán)''\n''(1) có (2) không '))
    if de_bai == 1:
        x = symbols('x')
        func = input('Nhập hàm f(x): ')
        f = sympify(func)
        init_value = input('Nhập khoảng lấy tích phân a, b (a < b) cách nhau bởi dấu cách: ')
        a, b = [float(i) for i in init_value.split()]
        q = int(input(
            'Chọn bài toán bạn muốn giải quyết (Nhập số theo bài toán)''\n''(1) Tính tích phân (2) Tính số khoảng chia cần thiết: '))
        if q == 1:
            n = int(input('Nhập số khoảng chia n: '))
            h = (b - a) / n

            D = [1]
            for i in range(0, n + 1):
                multiply_horner(D, i)  # Tích các (t-j), j từ 0 đến n

            A = [f.subs(x, a + i * h) for i in range(n + 1)]  # Tạo mảng lưu giá trị hàm tại các mốc nội suy

            if n % 2 == 0:
                Hinh_thang(A)
                E_hinh_thang()
                print()
                simpson(A)
                E_simpson()
                print()
                newton_cotez()
                E_newton_cotez()
            else:
                Hinh_thang(A)
                E_hinh_thang()
                print()
                newton_cotez()
                E_newton_cotez()

        if q == 2:
            eps = float(input('Nhập hệ số ép si lon: '))
            skc_hinh_thang()
            skc_simpson()
    else:
        init_value = input('Nhập khoảng lấy tích phân a, b (a < b) cách nhau bởi dấu cách: ')
        n = int(input('Nhập số khoảng chia n: '))
        a, b = [float(i) for i in init_value.split()]
        h = (b - a) / n

        D = [1]
        for i in range(0, n + 1):
            multiply_horner(D, i)  # Tích các (t-j), j từ 0 đến
        A = (input('nhập mảng giá trị tại các mốc nội suy cách nhau bởi dấu cách (n+1 mốc): '))

        A = A.split()
        for i in range(len(A)):
            A[i] = float(A[i])
        if n % 2 == 0:
            Hinh_thang(A)
            print()
            simpson(A)
            print()
            newton_cotez()
        else:
            Hinh_thang(A)
            print()
            newton_cotez()


if __name__ == '__main__':
    main()
