import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import neurokit2 as nk

data = nk.data("bio_eventrelated_100hz")["ECG"]


fig, ax = plt.subplots()
fig.set_size_inches(8, 5)


def animate(i):
    ax.clear()
    ax.plot(data, "green")  # Zmiana koloru wykresu na zielony
    ax.set_xlim(left=i, right=i + 400)
    ax.set_ylim([-2, 2])


num_frames = len(data) - 400
interval = 50
ani = FuncAnimation(fig, animate, frames=num_frames, interval=interval, repeat=True)

plt.show()
