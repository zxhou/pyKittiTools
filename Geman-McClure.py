# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 11:04:22 2017

@author: zxhou
"""

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5, 5, 1004)

mu1 = 16
mu2 = 4
mu3 = 1
mu4 = 0.25

y1 = x**2/(mu1 + x**2)
y2 = x**2/(mu2 + x**2)
y3 = x**2/(mu3 + x**2)
y4 = x**2/(mu4 + x**2)

plt.figure()

l1, = plt.plot(x,y1)
l2, = plt.plot(x,y2)
l3, = plt.plot(x,y3)
l4, = plt.plot(x,y4)

# 设置坐标轴的取值范围
#plt.xlim((-1, 1))
#plt.ylim((0, 2))

# 设置坐标轴的lable
plt.xlabel('x')
plt.ylabel('ρ')

plt.legend(handles = [l1, l2, l3, l4], labels = ['μ = 16', 'μ = 4','μ = 1','μ = 0.25'], loc = 'best')

plt.show()
