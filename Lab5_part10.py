import matplotlib.pyplot as plt

print("-----Exercise 10-------")

x = range(0, 20)
y = [value ** 2 for value in x]



plt.plot(x,y,marker="o")

plt.annotate('Highest', xy=(x[-1], y[-1]), xytext=(x[-1]-3, y[-1]+50))
plt.annotate('Lowest', xy=(x[0], y[0]), xytext=(x[0]+1, y[0]+50))


plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot ')


plt.show()
