
from __future__ import division
from numpy.fft import rfft
from numpy import argmax, mean, diff, log
from matplotlib.mlab import find
from time import time
import matplotlib.pyplot as plt
import sys

MainLit =[]
with open('data1.txt') as f:
    for line in f:
        numbers_float = line.split()
        MainLit.append(float((numbers_float[0])))

print(MainLit)
x = MainLit
y = [i for i in range(len(y))]

plt.plot(x,y)
plt.show()

f = x/y
print(f)