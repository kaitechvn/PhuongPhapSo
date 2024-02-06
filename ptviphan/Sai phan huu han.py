# giải phương trình dạng sau (pu')' - qu + f = 0
# Trong đó p, q, f là các hàm cho trước, u là hàm lưới cần tìm
import math
import numpy as np
from scipy.linalg import solve_banded
import matplotlib.pyplot as plt
import os

os.startfile("C:/Users/Admin/Desktop/lmao.txt")
input("Complete input in text file then press ENTER: ")

with open("C:/Users/Admin/Desktop/lmao.txt", "r") as f:
    data = []
    while (True):
        line = f.readline()
        try:
            if line[0] == '=':
                data.append(line[1:])
        except:
            pass
        if line == "": break

a = float(data[3])
b = float(data[4])
n = int(data[5]) - 1  # n là chỉ số của x lớn nhất
h = (b - a) / n
x = np.array([a + i * h for i in range(n + 1)])

p = lambda x: eval(data[0])
q = lambda x: eval(data[1])
f = lambda x: eval(data[2])

A = lambda x: p(x - 0.5 * h)
B = lambda x: p(x + 0.5 * h) + p(x - 0.5 * h) + h ** 2 * q(x)
C = lambda x: p(x + 0.5 * h)

trueFuntion = lambda x: eval(data[6])


# boundary condition
#    p(a)u'(a) - phi1.u(a) = -m1
#    p(b)u'(b) - phi2.u(b) = -m2


def setUpGeneralSystem():
    solutionSystem = np.array([[0.0 for i in range(n + 2)] for j in range(n + 1)])
    for i in range(1, n):
        solutionSystem[i, i - 1] = A(x[i])
        solutionSystem[i, i] = -B(x[i])
        solutionSystem[i, i + 1] = C(x[i])
        solutionSystem[i, n + 1] = -h * h * f(x[i])
    return solutionSystem


def addboundaryCondition_Type1(solutionSystem):
    print("------------------------------------")
    print("|    boundary condition type 1      |")
    print("|     u(a) = m1                    |")
    print("|     u(b) = m2                    |")
    print("------------------------------------\n")
    m1 = float(input("Enter m1: "))
    m2 = float(input("Enter m2: "))
    solutionSystem[0][0], solutionSystem[n][n] = 1, 1
    solutionSystem[0][n + 1] = m1
    solutionSystem[n][n + 1] = m2
    return solutionSystem


def addboundaryCondition_Type2or3(solutionSystem):
    print("---------------------------------------")
    print("|    boundary condition type 2 or 3    |")
    print("|     p(a)u'(a) - phi1.u(a) = -m1      |")
    print("|     p(b)u'(b) - phi2.u(b) = -m2      |")
    print("---------------------------------------\n")
    phi1 = float(input("Enter phi1: "))
    phi2 = float(input("Enter phi2: "))
    m1 = float(input("Enter m1: "))
    m2 = float(input("Enter m2: "))
    solutionSystem[0][0] = -(phi1 + p(x[0] + h / 2) / h + q(x[0]) * h / 2)
    solutionSystem[0][1] = p(x[0] + h / 2) / h
    solutionSystem[0][n + 1] = -m1 - f(x[0]) * h / 2
    solutionSystem[n][n - 1] = -p(x[n] - h / 2) / h
    solutionSystem[n][n] = -phi2 + p(x[n] - h / 2) / h + q(x[n]) * h / 2
    solutionSystem[n][n + 1] = -m2 - f(x[n]) * h / 2
    return solutionSystem


def solveNumpy(solutionSystem):
    a = np.array([[solutionSystem[i][j] for j in range(n + 1)] for i in range(n + 1)])  # VT của hệ
    b = np.array([solutionSystem[i][n + 1] for i in range(n + 1)])  # VP của hệ
    return np.linalg.solve(a, b)


## Tri Diagonal Matrix Algorithm(a.k.a Thomas algorithm) solver
def TDMAsolver(solutionSystem):
    lowDiag = [solutionSystem[i + 1][i] for i in range(n)]  # Đường chéo dưới đường chép chính
    mainDiag = [solutionSystem[i][i] for i in range(n + 1)]  # ĐƯờng chéo chính
    upDiag = [solutionSystem[i][i + 1] for i in range(n)]
    rightSide = [solutionSystem[i][n + 1] for i in range(n + 1)]  # Vế phải
    nf = len(rightSide)  # number of equations
    lowDiag_copy, mainDiag_copy, upDiag_copy, rightSide_copy = map(np.array, (
    lowDiag, mainDiag, upDiag, rightSide))  # copy arrays

    for i in range(1, nf):
        mc = lowDiag_copy[i - 1] / mainDiag_copy[i - 1]
        mainDiag_copy[i] = mainDiag_copy[i] - mc * upDiag_copy[i - 1]
        rightSide_copy[i] = rightSide_copy[i] - mc * rightSide_copy[i - 1]

    result = mainDiag_copy
    result[-1] = rightSide_copy[-1] / mainDiag_copy[-1]

    for i in range(nf - 2, -1, -1):
        result[i] = (rightSide_copy[i] - upDiag_copy[i] * result[i + 1]) / mainDiag_copy[i]
    return result


def drawGraph(x, solution, name_solver):
    plt.figure(figsize=(12, 8))
    plt.plot(x, solution, 'bo--', label='Approximate')
    if trueFuntion(x[0]) != None:
        plt.plot(x, trueFuntion(x), 'g', label='Exact')
    plt.title('Approximate and Exact Solution # for ODE ' + name_solver)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.legend(loc='lower right')
    #  plt.xticks(np.arange(0, 10, 1)) #Điều chỉnh độ chi tiết của trục hoành, tung ở đây
    #  plt.yticks(np.arange(0, 10, 1))
    plt.xticks
    plt.show()


def main():
    solutionSystem = setUpGeneralSystem()
    boundary_type = int(input("Enter type of your boundary(1,2,3): "))
    if boundary_type == 1:
        solutionSystem = addboundaryCondition_Type1(solutionSystem)
    else:
        solutionSystem = addboundaryCondition_Type2or3(solutionSystem)
    solution = solveNumpy(solutionSystem)
    print(x, '\t', solution)
    drawGraph(x, solution, "NUMPY solver")

    # solution2 = TDMAsolver(solutionSystem)  #Nếu dữ liệu lớn vài nghìn đổ lên thì nên sử dụng hàm này thay vì numpy
    # drawGraph(x, solution2, "TDMA solver")


if __name__ == "__main__":
    main()