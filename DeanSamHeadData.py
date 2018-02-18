#
# from __future__ import division
# from numpy.fft import rfft
# from numpy import argmax, mean, diff, log
# from matplotlib.mlab import find
# from time import time

# import sys
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import numpy as np
import statistics
import math
import glob
import os
import MotionDetectorContours


list_of_files = glob.glob('data/*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)

y =[]
with open(latest_file) as f:
    for line in f:
        numbers_float = line.split()
        #get nan when no movement
        if not str(numbers_float[0]) =='nan':
            y.append(float((numbers_float[0])))



# x, y = np.array(x),np.array(y)
# x_smooth = np.linspace(x.min(),x.max(),100)
# y_smooth = spline(x,y,x_smooth)
def cleanY(y_data):
    #removing the messy data you get at the start and end
    dataToReturn = y_data[20:-20]
    sizeToRomove  =  20
    dataMean = statistics.mean(y_data)
    std =  statistics.stdev(y_data)
    uppedstd = dataMean+std
    lowerstd = dataMean-std
    for i in range(0,len(dataToReturn)):
        if dataToReturn[i]>uppedstd:
            dataToReturn[i] =uppedstd
        elif dataToReturn[i]<lowerstd:
            dataToReturn[i] =  lowerstd

    return dataToReturn
y = cleanY(y)

def FindNumberOfOs(y_data):
    dataMean = statistics.mean(y_data)
    numOfOs = 0
    sizeOfBlock = 10
    for i in range(0,len(y_data)-sizeOfBlock*2,10):
        if statistics.mean(y_data[i+sizeOfBlock:i+sizeOfBlock*2]) > dataMean and statistics.mean(y_data[i:i+sizeOfBlock]) < dataMean:
            numOfOs += 1
    return numOfOs

print('Number of push-ups:\t{}'.format(FindNumberOfOs(y)))


#un hash to plot graph!!!!
x = [i for i in range(len(y))]
# plt.plot(x,y)
# plt.show()

def sinMatching(y_data):
    amp = max(y_data)-min(y_data)
    c = statistics.mean(y_data)
    w = 1/(len(y_data)//2)
    matchDif =[]
    for i in range(0,len(y_data)//10):
        sinData = [amp*math.sin(w*x)+c for x in range(len(y_data))]
        matchDif.append([0])
        for j in range(len(y_data)):
            matchDif[i][0] = abs(sinData[i]- y_data[j]) + matchDif[i][0]
    return matchDif

plt.plot(y)
plt.show()
