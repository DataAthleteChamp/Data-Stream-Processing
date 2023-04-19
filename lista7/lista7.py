import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Definicja funkcji
def funkcja(x):
    return np.sin(x)

# Przesunięcie wykresu
def update(num, xdata, ydata, line, ax):
    xdata.append(xdata[-1] + np.pi/15)
    ydata.append(funkcja(xdata[-1]))
    line.set_data(xdata, ydata)

    ax.set_xlim(xdata[-1] - 2*np.pi, xdata[-1] + 2*np.pi)

    return line,

# Utworzenie wykresu
fig, ax = plt.subplots()
xdata, ydata = [0], [funkcja(0)]
line, = ax.plot(xdata, ydata, 'r-')

# Ustawienie osi
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)

# Animacja
ani = FuncAnimation(fig, update, frames=range(10000), fargs=(xdata, ydata, line, ax), interval=120, blit=True)

plt.show()
