import matplotlib.pyplot as plt

print("-----Exercise 6-------")

import numpy as np


x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]

data = np.random.randn(1000)

x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)




# Line Plot
plt.subplot(2,2,1)
plt.plot(x, y)
plt.title('Line Plot')

# Bar Plot
plt.subplot(2,2,2)
plt.bar(categories, values, color='yellow')
plt.title('Bar Plot')

# Histogram
plt.subplot(2,2,3)
plt.hist(data, bins=30, color='blue')
plt.title('Histogram')

# Scatter Plot
plt.subplot(2,2,4)
plt.scatter(x_scatter, y_scatter, color='red')
plt.title('Scatter Plot')

# Adjust layout
plt.tight_layout()
plt.show()