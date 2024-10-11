import matplotlib.pyplot as plt


categories = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']
values = [10, 15, 7, 12, 5]

plt.bar(categories,values)

plt.xlabel("categories")
plt.ylabel("values")
plt.title("Data")

plt.show()