import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(8, 5)

y_values=[]

x_values= np.arange(0,30,0.05)

for y in x_values:
    y_values.append(np.sin(y))


def animate(i):
    ax.clear()
    plt.plot(x_values, y_values)
    ax.plot(x_values[i], y_values[i], color='red',
            label='original', marker='o')
    ax.set_xlim([0, 30])
    ax.set_ylim([-2,2])


ani = FuncAnimation(fig, animate, frames=len(x_values),interval=1, repeat=True)
# plt.plot(x_values,y_values)
plt.show()
# plt.close()