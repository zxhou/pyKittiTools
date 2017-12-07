# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:30:46 2017

@author: zxhou
"""


import numpy as np
import matplotlib.pyplot as plt

savePath = "distribution10.jpg"
figureTitle = "Distribution of Lidar at Different Distances on 10"
filename = './dataset/10/000000.bin'

interval = 10
start = 0
X = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
nb_dffrtDst = {'dist5':0,'dist10':0,'dist15':0,'dist20':0,'dist25':0,'dist30':0,'dist35':0,'dist40' : 0,'dist45':0, 'dist50' : 0,'dist55':0, 'dist60' : 0,'dist65':0, 'dist70' : 0,'dist75':0,'dist80' : 0,'dist85':0,'dist90' : 0,'dist95':0,'dist100' : 0}
count = 0

scan = np.fromfile(filename, dtype=np.float32)
scan = np.reshape(scan,(-1,4))

barWidth = 3
for num in scan:
#,    print(num)
    distance = (scan[count][0]**2 + scan[count][1]**2 + scan[count][2]**2)**0.5
#    distance = abs(scan[count][2])
    if distance < 5:
        nb_dffrtDst['dist5'] += 1
    if distance >= 5 and distance < 10:
        nb_dffrtDst['dist10'] += 1
    elif distance >= 10 and distance < 15:
        nb_dffrtDst['dist15'] += 1
    elif distance >= 15 and distance < 20:
        nb_dffrtDst['dist20'] += 1
    elif distance >= 20 and distance < 25:
        nb_dffrtDst['dist25'] += 1
    elif distance >= 25 and distance < 30:
        nb_dffrtDst['dist30'] += 1
    elif distance >= 30 and distance < 35:
        nb_dffrtDst['dist35'] += 1
    elif distance >= 35 and distance < 40:
        nb_dffrtDst['dist40'] += 1
    elif distance >= 40 and distance < 45:
        nb_dffrtDst['dist45'] += 1
    elif distance >= 45 and distance < 50:
        nb_dffrtDst['dist50'] += 1
    elif distance >= 50 and distance < 55:
        nb_dffrtDst['dist55'] += 1
    elif distance >= 55 and distance < 60:
        nb_dffrtDst['dist60'] += 1
    elif distance >= 60 and distance < 65:
        nb_dffrtDst['dist65'] += 1
    elif distance >= 65 and distance < 70:
        nb_dffrtDst['dist70'] += 1
    elif distance >= 70 and distance < 75:
        nb_dffrtDst['dist75'] += 1
    elif distance >= 75 and distance < 80:
        nb_dffrtDst['dist80'] += 1
    elif distance >= 80 and distance < 85:
        nb_dffrtDst['dist85'] += 1
    elif distance >= 85 and distance < 90:
        nb_dffrtDst['dist90'] += 1
    elif distance >= 90 and distance < 95:
        nb_dffrtDst['dist95'] += 1
    elif distance >= 95:
        nb_dffrtDst['dist100'] += 1
    count += 1
 
Y=[nb_dffrtDst['dist5'],nb_dffrtDst['dist10'],nb_dffrtDst['dist15'],nb_dffrtDst['dist20'],nb_dffrtDst['dist25'],nb_dffrtDst['dist30'],nb_dffrtDst['dist35'],nb_dffrtDst['dist40'],nb_dffrtDst['dist45'],nb_dffrtDst['dist50'],nb_dffrtDst['dist55'],nb_dffrtDst['dist60'],nb_dffrtDst['dist65'],nb_dffrtDst['dist70'],nb_dffrtDst['dist75'],nb_dffrtDst['dist80'],nb_dffrtDst['dist85'],nb_dffrtDst['dist90'],nb_dffrtDst['dist95'],nb_dffrtDst['dist100']]    
plt.figure()  
print(Y)
print(X)
plt.bar(X,Y,barWidth,color="green")  
plt.xlabel("Distance")  
plt.ylabel("Points Number")  
plt.title(figureTitle) 

plt.savefig(savePath) 