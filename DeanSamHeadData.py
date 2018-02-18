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
y =[]
with open('data4WithNewMotion.txt') as f:
    for line in f:
        numbers_float = line.split()
        #get nan when no movement
        if not str(numbers_float[0]) =='nan':
            y.append(float((numbers_float[0])))

print(y)
x = [i for i in range(len(y))]
x, y = np.array(x),np.array(y)
x_smooth = np.linspace(x.min(),x.max(),100)
y_smooth = spline(x,y,x_smooth)

plt.plot(x,y)
plt.show()
