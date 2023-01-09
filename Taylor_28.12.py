import math
import numpy as np
import matplotlib.pyplot as plt

def f_sin(num):
    x = np.linspace(-5, 5, 50)
    y = []
    for i in x:
        y1 = 0
        for j in range(1,num+1):
            y1 += ((((-1) ** (j-1))) * (i**(2*j-1)))/math.factorial(2*j-1)
        y.append(y1)
    return y

def f_cos(num):
    x = np.linspace(-5, 5, 50)
    y = []
    for i in x:
        y1 = 0
        for j in range(1,num+1):
            y1 += ((((-1) ** (j-1))) * (i**(2*j-2)))/math.factorial(2*j-2)
        y.append(y1)
    return y

def f_exp(num): 
    x = np.linspace(-5, 5, 50)
    y = []
    for i in x:
        y1 = 0        
        for j in range(num):
            y1 += i**j/math.factorial(j)
        y.append(y1)
    return y

n = input('Введите функцию(sin,cos,exp): ')
nums = [1,2,3,4,5,6,7]
x = np.linspace(-5, 5, 50)
y_Tay = []
if (n == 'exp'):
    y = np.exp(x)
    for num in nums:
        y_Tay.extend([f_exp(num)])
elif (n == 'sin'):
    y = np.sin(x)
    for num in nums:
        y_Tay.extend([f_sin(num)])
elif (n == 'cos'):
    y = np.cos(x)
    for num in nums:
        y_Tay.extend([f_cos(num)])

plt.plot(x, y, label = 'original')
for p in range(len(nums)):
    plt.plot(x, y_Tay[p], label = f"n = {nums[p]}")
plt.legend()
plt.show()