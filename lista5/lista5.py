import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# definiowanie funkcji, którą chcemy wyświetlić na wykresie
def funkcja(x, a):
    return np.sin(a * x**2 -a)

# tworzenie danych do wyświetlenia na wykresie
x = np.linspace(0, 10, 1000)
y = funkcja(x, 1)

# tworzenie wykresu
fig, ax = plt.subplots()
l, = ax.plot(x, y, lw=2, color='red')

# dodawanie suwaka do skalowania osi x
axcolor = 'lightgoldenrodyellow'
ax_a = plt.axes([0.2, 0.05, 0.65, 0.03], facecolor=axcolor)
slider_a = Slider(ax_a, 'Skalowanie osi x', 0.1, 10.0, valinit=1)

# funkcja aktualizująca wykres w zależności od wartości suwaka
def update(val):
    a = slider_a.val
    x_min = 0
    x_max = 10 * a
    x_scaled = np.linspace(x_min, x_max, 1000)
    y = funkcja(x_scaled, 1)
    l.set_xdata(x_scaled)
    l.set_ydata(y)
    ax.set_xlim(x_min, x_max)
    fig.canvas.draw_idle()

slider_a.on_changed(update)

# dodanie przycisku resetującego suwak
resetax = plt.axes([0.8, 0.1, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

# funkcja resetująca wartość suwaka do wartości początkowej
def reset(event):
    slider_a.reset()
button.on_clicked(reset)

plt.show()
