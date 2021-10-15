
"""
This is a small tool to plot the trajectary of Kitti groundtruth
@author: Zhixing Hou <hzx@njust.edu.cn>
"""

import os
import matplotlib.pyplot as plt
import numpy as np

#-----------------------Configuration--------------------------
pose_path = '/media/hzx/data/Kitti/poses/'
result_path = './results/'
sequence = '00'
poseName = os.path.join(pose_path, sequence+'.txt')
figName = os.path.join(result_path, sequence+'.jpg')

isSaveFig = False
#--------------------------------------------------------------

file = open(poseName, 'r')
linesList = file.readlines()
file.close()
linesList = [line.strip().split(' ') for line in linesList]
x_GT=[]
y_GT=[]
z_GT=[]

for transList in linesList:
    x_GT.append(float(transList[3]))
    y_GT.append(float(transList[7]))
    z_GT.append(float(transList[11]))

# 设置坐标轴的取值范围
#plt.xlim((-100, 1000))
#plt.ylim((-100, 1000))

plt.figure()
plt.plot(x_GT,z_GT,color = 'red',label = "ground truth")
plt.xlabel('x')
plt.ylabel('z')

#plt.legend(handles = l3, labels = 'Groundtruth', loc = 'best')
    
#plt.title('sequence '+ sequence)
print('save sequence '+sequence)

if isSaveFig:
    plt.savefig(figName)
    print('trajectory is saved!')
else:
    plt.show()



