import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a Figure and an Axes object
fig, ax = plt.subplots()

# Define the data to be plotted
x = [0, 1, 2, 3, 4]
y = [0, 1, 2, 3, 4]

# Define a function that updates the plot
def update(num):
  ax.plot(x[:num], y[:num], 'r')
  ax.set_xlabel('X-axis')
  ax.set_ylabel('Y-axis')
  ax.set_title('Animation')

# Create an Animation object
ani = animation.FuncAnimation(
  fig, update, frames=5,
  interval=1000, repeat=False
)

# Show the plot
plt.show()
