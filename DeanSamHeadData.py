import matplotlib.pyplot as plt
MainLit =[]
with open('data1.txt') as f:
    for line in f:
        numbers_float = line.split()
        MainLit.append(float((numbers_float[0])))

print(MainLit)
y = MainLit
x = [i for i in range(len(y))]

plt.plot(x,y)
plt.show()

