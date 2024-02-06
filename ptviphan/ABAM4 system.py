import matplotlib.pyplot as plt

# # INPUT
y0 = 1
x0 = 2
h = 0.2
x_ = 3


# y' = f(x, y)
def f_x(x, y):
    result = ((4 - pow(y,2))/(2*x))
    return result


def cal_yp(x0, yn):
    yp = []
    for i in range(len(yn)):
        y_pn = f_x(x0 + i * h, yn[i])
        yp.append(y_pn)
    return yp


def cal_y_n(yp, yn, h, x_):
    times = int(x_ / h)
    y_n_ = []
    for i in range(4, times + 1):
        yns_ = yn[i - 1] + h / 24 * (55 * yp[i - 1] - 59 * yp[i - 2] + 37 * yp[i - 3] - 9 * yp[i - 4])
        ysp = f_x(x0 + h * i, yns_)
        y_n_.append(yns_)
        yp.append(ysp)
        yns = yn[i - 1] + h / 24 * (9 * ysp + 19 * yp[i - 1] - 5 * yp[i - 2] + 1 * yp[i - 3])
        yn.append(yns)
    return y_n_, yn


yN = [1, 1.1360684, 1.24811921, 1.34102]
yp = cal_yp(x0, yN)
yn_, yN = cal_y_n(yp, yN, h, x_)
print("x\t y du doan\t\t y hieu chinh")
for i in range(len(yN)):
    if i <= 3:
        print(f"{round(x0 + h * i, 1)}\t nan\t\t \t{yN[i]}")
    else:
        print(f"{round(x0 + h * i, 1)}\t {yn_[i - 4]} \t{yN[i]}")

x = [x0 + h * i for i in range(int(x_ / h) + 1)]
plt.plot(x, yN)
plt.scatter(x, yN)
plt.show()