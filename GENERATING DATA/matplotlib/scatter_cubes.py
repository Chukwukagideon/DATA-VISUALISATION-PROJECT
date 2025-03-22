import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3  for x in x_values]

plt.style.use("seaborn-v0_8-dark")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# Set Chart title and label Axes
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# set tick params
ax.tick_params(axis="both", which="major", labelsize=14)

# set the range of each axis
ax.axis([0, 5500, 0, None])


plt.show()
