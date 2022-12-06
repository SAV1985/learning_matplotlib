import matplotlib.pyplot as plt


x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values,y_values, s=10) #c=y_values, cmap=plt.cm.Blues, s = 10)

ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, 6, 0, 150])

plt.show()