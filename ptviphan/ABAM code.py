import math

x0 = 0
def f_x(x, y, z):
    return (4*pow(x,3)-6*pow(x,2)+2.25*x)*y - 9*pow(math.e,-pow(x,2))*(1.25*pow(x,2)-2.75*x-2)

def g_x(x, y, z):
    return z / (1+ pow(x,2))

somoc = 30
y_n_ = []
g_n_ = []
h = 0.1
gn = [9,9.18222894408873,9.36883110810194,9.55967850426681]
yn = [9,9.09090440213152,9.18363442822041,9.27821351467108]
yp = []
gp = []

for i in range(len(yn)):
    y_pn = f_x(x0 + i * h, yn[i], gn[i])
    yp.append(y_pn)

for i in range(len(gn)):
    g_pn = g_x(x0 + i * h, yn[i], gn[i])
    gp.append(g_pn)

for i in range(4, somoc + 1):
    yns_ = yn[i - 1] + (h / 24) * (55 * yp[i - 1] - 59 * yp[i - 2] + 37 * yp[i - 3] - 9 * yp[i - 4])
    gns_ = gn[i - 1] + (h / 24) * (55 * gp[i - 1] - 59 * gp[i - 2] + 37 * gp[i - 3] - 9 * gp[i - 4])
    ysp = f_x(x0 + h * i, yns_, gns_)
    gsp = g_x(x0 + h * i, yns_, gns_)
    y_n_.append(yns_)
    g_n_.append(gns_)

    yns = yn[i - 1] + (h / 720 )* (251 * ysp + 646 * yp[i - 1] - 264 * yp[i - 2] +106 * yp[i - 3] - 19 *yp[i - 4])
    gns = gn[i - 1] + (h / 720) * (251 * gsp + 646 * gp[i - 1] - 264 * gp[i - 2] + 106 * gp[i - 3] - 19 * gp[i -4])
    yn.append(yns)
    gn.append(gns)

    a = f_x(x0 + i * h, yns, gns)
    yp.append(a)

    b = g_x(x0 + i * h, yns, gns)
    gp.append(b)

print( y_n_)
print("hieu chinh y:", yn)
print( g_n_)
print("hieu chinh z: ", gn)