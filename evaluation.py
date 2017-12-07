# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 09:13:14 2017

@author: zxhou
"""

import matplotlib.pyplot as plt
import numpy as np


file = open("./evaluation/pose00.txt", 'r')
linesList = file.readlines()
file.close()
linesList = [line.strip().split(' ') for line in linesList]

R = np.mat(np.eye(3,3,dtype = float))
trans = np.mat(np.zeros((3,1)))
x = []
y = []
z = []
r = []
t = []
count = 0
for transList in linesList:
    
    R[0,0] = float(transList[0])
    R[0,1] = float(transList[1])
    R[0,2] = float(transList[2])
    R[1,0] = float(transList[4])
    R[1,1] = float(transList[5])
    R[1,2] = float(transList[6])
    R[2,0] = float(transList[8])
    R[2,1] = float(transList[9])
    R[2,2] = float(transList[10])
    trans[0,0] = float(transList[3])
    trans[1,0] = float(transList[7])
    trans[2,0] = float(transList[11])
        
    if count == 0:
        x.append(trans[0,0])
        y.append(trans[1,0])
        z.append(trans[2,0])

        r.append(R)
        t.append(trans)
        print(R)
        print(t)
        
    else:
        R = r[count - 1]*R
        trans = r[count - 1]*trans + t[count - 1]
        
        x.append(trans[0,0])
        y.append(trans[1,0])
        z.append(trans[2,0])
        
        r.append(R)
        t.append(trans)
        
    count += 1  

#plt.plot(x, z, linewidth = '1', label = "test", color=' coral ', linestyle=':', marker='|')
plt.plot(x,z,color = 'red')
#plt.plot(xx,zz,color = 'blue')
plt.show()