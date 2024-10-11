import matplotlib.pyplot as plt


print("-----Exercise 7-------")


categories = ['Marketing', 'Development', 'Sales', 'Support']
values = [20, 35, 25, 20]

plt.pie(values,labels=categories)
plt.title("pie")
plt.legend()

plt.show()

