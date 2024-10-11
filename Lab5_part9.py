import matplotlib.pyplot as plt

print("-----Exercise 9-------")

import numpy as np

dataset1 = np.random.normal(60, 10, 100) # 100 data points around mean 60
dataset2 = np.random.normal(70, 15, 100) # 100 data points around mean 70
dataset3 = np.random.normal(80, 5, 100) # 100 data points around mean 80


data =[dataset1,dataset2,dataset3]
labels =["Dataset1","Dataset2","Dataset3"]

plt.boxplot(data,labels=labels)



plt.xlabel("x_label")
plt.ylabel("y_label")
plt.title("Box plot")

plt.show()
