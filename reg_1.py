def minor(m,shag):
    result = []
    for r in m[1:]:
        row = []
        for j in range(len(r)):
            if j != shag:
                row.append(r[j])
        result.append(row)
    return result



def det(m):
    len_m = len(m)
    if len_m == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    result = 0
    znak = 1
    for i in range(len_m):
        result += znak * m[0][i] * det(minor(m,i))
        znak =-znak
    return result



def kramer(m, svobod):
    m_fix = tuple(m)
    result = []
    for i in range(len(m_fix)):
        m_trans = list(zip(*m))
        m_trans[i] = svobod
        result.append(det(list(zip(*m_trans)))/det(m_fix))
        m = list(m_fix)
    return result



import matplotlib.pyplot as plt
import numpy as np


x_orig = np.linspace(0, 15, 30)
y_orig = ((np.sin(x_orig/5))*(np.exp(x_orig/10))+(5*(np.exp(-x_orig/2))))


def func(x):
    return ((np.sin(x/5))*(np.exp(x/10))+(5*(np.exp(-x/2))))


def matrix_r(x_orig, num):
        x = np.linspace(0, 15, num)
        matr = []
        for i in range(num):
            matr_prom = []
            for j in range(num):
                matr_prom.append((x[i])**j)
            matr.extend([matr_prom])
        b = np.array(func(x))
        c = kramer(matr, b)
        regr_y = []
        for i in range(len(x_orig)):
            regr_prom = 0
            for j in range(num):
                regr_prom += ((c[j])*(x_orig[i])**j)
            regr_y.append(regr_prom)
        return regr_y

plt.plot(x_orig, y_orig, label='original')
plt.plot(x_orig, matrix_r(x_orig, 2), label=f"n = 2")
plt.plot(x_orig, matrix_r(x_orig, 3), label=f"n = 3")
plt.plot(x_orig, matrix_r(x_orig, 4), label=f"n = 4")
plt.plot(x_orig, matrix_r(x_orig, 5), label=f"n = 5")
plt.legend()
plt.show()



