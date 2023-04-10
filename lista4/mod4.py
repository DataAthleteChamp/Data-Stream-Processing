import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Parametryzowana funkcja kwadratowa do narysowania
def f(x, a, b, c):
    return a * x**2 + b * x + c

x = np.linspace(-10, 10, 1000)

# Zdefiniuj początkowe parametry
init_a = 1
init_b = 0
init_c = 0

# Utwórz rysunek oraz linię, którą będziemy modyfikować
fig, ax = plt.subplots()
line, = ax.plot(x, f(x, init_a, init_b, init_c), lw=2)
ax.set_xlabel('x')

# Dostosuj wykres główny, aby zrobić miejsce dla suwaków
fig.subplots_adjust(left=0.25, bottom=0.25)

# Dodaj poziomy suwak do sterowania parametrami a, b i c
ax_a = fig.add_axes([0.25, 0.15, 0.65, 0.03])
ax_b = fig.add_axes([0.25, 0.1, 0.65,0.03])
ax_c = fig.add_axes([0.25, 0.05, 0.65, 0.03])

a_slider = Slider(ax=ax_a, label='a', valmin=-10, valmax=10, valinit=init_a)
b_slider = Slider(ax=ax_b, label='b', valmin=-10, valmax=10, valinit=init_b)
c_slider = Slider(ax=ax_c, label='c', valmin=-10, valmax=10, valinit=init_c)

# Funkcja do wywołania za każdym razem, gdy wartość suwaka ulegnie zmianie
def update(val):
    line.set_ydata(f(x, a_slider.val, b_slider.val, c_slider.val))
    fig.canvas.draw_idle()

# Zarejestruj funkcję aktualizacji dla każdego suwaka
a_slider.on_changed(update)
b_slider.on_changed(update)
c_slider.on_changed(update)

# Utwórz przycisk `matplotlib.widgets.Button` do zresetowania suwaków do wartości początkowych
resetax = fig.add_axes([0.8,0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    a_slider.reset()
    b_slider.reset()
    c_slider.reset()

button.on_clicked(reset)

plt.show()


