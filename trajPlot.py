
"""
This is a program to plot the trajectary of Kitti groundtruth and evaluation
@author: Zhixing Hou <zxhou2016@gmail.com>
"""

import matplotlib.pyplot as plt

#-----------------------Configuration--------------------------
trajMono = './eval/pose_mono_00.txt'
trajStereo = './evaluation/pose_00_libviso_stereo.txt'
trajGT = '00.txt'
figName = './evaluation/pic/evaluation_00_libviso_fix.jpg'

evalMono = True
evalStereo = False
isSaveFig = False
#--------------------------------------------------------------


if evalMono:
    file = open(trajMono,'r')
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
    
    plt.figure()
    l1, = plt.plot(x,z,color = 'blue',label = "mono")

if evalStereo:
    file = open(trajStereo, 'r')
    linesList = file.readlines()
    file.close()
    linesList = [line.strip().split(' ') for line in linesList]
    x_stereo=[]
    y_stereo=[]
    z_stereo=[]
    for transList in linesList:
        x_stereo.append(transList[3])
        y_stereo.append(transList[7])
        z_stereo.append(transList[11])
    
    l2, = plt.plot(x_stereo,z_stereo,color = 'green',label = "stereo")


file = open(trajGT, 'r')
linesList = file.readlines()
file.close()
linesList = [line.strip().split(' ') for line in linesList]
x_GT=[]
y_GT=[]
z_GT=[]
for transList in linesList:
    x_GT.append(transList[3])
    y_GT.append(transList[7])
    z_GT.append(transList[11])

l3, = plt.plot(x_GT,z_GT,color = 'red',label = "ground truth")


if evalMono:
    plt.legend(handles = [l1, l3], labels = ['Monocular', 'Groundtruth'], loc = 'best')
elif evalStereo:
    plt.legend(handles = [l2, l3], labels = ['Stereo', 'Groundtruth'], loc = 'best')
elif evalMono and evalStereo:
    plt.legend(handles = [l1, l2, l3], labels = ['Mono', 'Stereo','Groundtruth'], loc = 'best')
    
plt.title('LIBVISO_00')

if isSaveFig:
    plt.savefig(figName)
else:
    plt.show()

