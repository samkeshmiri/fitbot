import datetime
import time

print(datetime.datetime.now())
# print('realData'+'{0_%Y_%m_%d-%H_%M_%S}'.format(datetime.datetime.now()))
print(time.strftime('%Y-%m-%d %H:%M:%S'))

baseName = 'Real'
dateTime = time.strftime('%Y-%m-%d_%H-%M-%S')
extention = '.txt'
fullName = baseName+ dateTime+ extention
print(fullName)
