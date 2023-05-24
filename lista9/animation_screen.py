import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import neurokit2 as nk
import pyautogui


class ECGAnimation:
    def __init__(self, data):
        self.data = data
        self.animation_running = False
        self.current_index = 0
        self.setup_plot()

    def setup_plot(self):
        gs = dict(height_ratios=[1], width_ratios=[7, 1])
        self.fig, self.ax = plt.subplots(1, 2, gridspec_kw=gs)
        self.fig.set_size_inches(9, 6)

        self.ax[1].set_yticks([])
        self.ax[1].set_xticks([])
        self.ax[1].spines['top'].set_visible(False)
        self.ax[1].spines['bottom'].set_visible(False)
        self.ax[1].spines['right'].set_visible(False)
        self.ax[1].spines['left'].set_visible(False)

        self.stop_button = self.create_button('START', [0.8, 0.8, 0.1, 0.05], self.toggle_animation)
        self.move_right_button = self.create_button('MOVE RIGHT', [0.8, 0.6, 0.1, 0.05], self.move_right)
        self.move_left_button = self.create_button('MOVE LEFT', [0.8, 0.4, 0.1, 0.05], self.move_left)
        self.screenshot_button = self.create_button('PrtSc', [0.8, 0.2, 0.1, 0.05], self.take_screenshot)

    def create_button(self, label, position, function):
        button_ax = plt.axes(position)
        button = Button(button_ax, label)
        button.on_clicked(function)
        return button

    def update_plot(self):
        self.ax[0].clear()
        self.ax[0].plot(self.data, "green", label='EKG')
        self.ax[0].set_xlim(left=self.current_index, right=self.current_index + 400)
        self.ax[0].set_ylim([-2, 2])
        self.ax[0].legend()
        plt.pause(0.001)  # Pauza dla odświeżenia wykresu
        plt.draw()

    def animate(self):
        while self.animation_running:
            self.current_index += 1  # Inkrementuj indeks
            self.update_plot()

    def toggle_animation(self, event):
        if self.animation_running:
            self.stop_button.label.set_text('START')
            self.animation_running = False
        else:
            self.stop_button.label.set_text('STOP')
            self.animation_running = True
            self.animate()  # Uruchom animację

    def move_right(self, event):
        if not self.animation_running:
            self.current_index += 50
            self.update_plot()

    def move_left(self, event):
        if not self.animation_running:
            self.current_index -= 50
            # Zapewnia, że indeks nie spadnie poniżej zera
            if self.current_index < 0:
                self.current_index = 0
            self.update_plot()

    # def take_screenshot(self, event):
    #     if not self.animation_running:
    #         self.fig.savefig('screenshot.png', dpi=300, bbox_inches='tight')
    #     else:
    #         print("nie mozna zrobic ss")

    def take_screenshot(self, event):
        if not self.animation_running:
            myScreenshot = pyautogui.screenshot(region=(100, 100, 1130, 700))
            myScreenshot.save(r'screenshot.png')
        else:
            print("nie mozna zrobic ss")

    def run(self):
        self.update_plot()
        plt.show()


def main():
    data = nk.data("bio_resting_8min_100hz")["ECG"]
    ECGAnimation(data).run()


if __name__ == "__main__":
    main()
