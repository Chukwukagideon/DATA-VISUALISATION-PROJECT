import matplotlib.pyplot as plt


plt.style.use("classic")
fig, ax = plt.subplots()
ax.scatter(2,4, s=200)

# Set Chart title and label Axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()
