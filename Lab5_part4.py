
import matplotlib.pyplot as plt

print("-----Exercise 4-------")

import numpy as np
data = np.random.normal(0, 1, 500) # 500 data points from normal distribution

plt.hist(data,bins=20)


plt.hist(data,color="blue",edgecolor="black")
plt.title("histogram")
plt.xlabel("x_axis")
plt.ylabel("y_axis")

plt.show()