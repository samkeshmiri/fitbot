import matplotlib.pyplot as plt
from fakePushUpData import fakeData

y = fakeData()
x = [i for i in range(len(y))]

plt.plot(x,y)
plt.show()

