# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:27:38 2017

@author: zxhou
"""

import matplotlib.pyplot as plt


file = open("00.txt", 'r')
linesList = file.readlines()
file.close()
linesList = [line.strip().split(' ') for line in linesList]
x=[]
y=[]
z=[]
for transList in linesList:
    x.append(transList[3])
    y.append(transList[7])
    z.append(transList[11])

#plt.plot(x, z, linewidth = '1', label = "test", color=' coral ', linestyle=':', marker='|')
plt.plot(x,z,color = 'red',label = "ground truth")
plt.show()
