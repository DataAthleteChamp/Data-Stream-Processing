import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import neurokit2 as nk
import numpy as np
import pyautogui


class ECGAnimation:
    def __init__(self, data):
        self.data = data
        self.animation_running = False
        self.current_index = 0
        self.r_peaks = self.detect_r_peaks()
        self.rr_min, self.rr_max, self.rr_diff = self.calculate_rr_stats()
        self.setup_plot()

    def detect_r_peaks(self):
        _, rpeaks = nk.ecg_peaks(self.data, sampling_rate=100)
        r_peaks = np.array(rpeaks['ECG_R_Peaks'])
        r_intervals = np.diff(r_peaks)
        return r_intervals

    def calculate_rr_stats(self):
        first_100_intervals = self.r_peaks[:100]
        return first_100_intervals.min(), first_100_intervals.max(), first_100_intervals.ptp()

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
        self.ax[1].axis('off')

        self.stop_button = self.create_button('START', [0.8, 0.5, 0.1, 0.05], self.toggle_animation)
        self.move_right_button = self.create_button('MOVE RIGHT', [0.8, 0.4, 0.1, 0.05], self.move_right)
        self.move_left_button = self.create_button('MOVE LEFT', [0.8, 0.3, 0.1, 0.05], self.move_left)
        self.screenshot_button = self.create_button('PrtSc', [0.8, 0.2, 0.1, 0.05], self.take_screenshot)

    def update_plot(self):
        self.ax[0].clear()
        self.ax[0].plot(self.data, "green", label='EKG')
        self.ax[0].set_xlim(left=self.current_index, right=self.current_index + 400)
        self.ax[0].set_ylim([-2, 2])
        self.ax[0].legend()

        self.ax[1].clear()
        self.ax[1].text(0.1, 0.9, 'RR min: {}'.format(self.rr_min))
        self.ax[1].text(0.1, 0.8, 'RR max: {}'.format(self.rr_max))
        self.ax[1].text(0.1, 0.7, 'RR diff: {}'.format(self.rr_diff))
        self.ax[1].axis('off')
        
        plt.pause(0.001)
        plt.draw()

    def create_button(self, label, position, function):
        button_ax = plt.axes(position)
        button = Button(button_ax, label)
        button.on_clicked(function)
        return button

    def animate(self):
        while self.animation_running:
            self.current_index += 1
            self.update_plot()

    def toggle_animation(self, event):
        if self.animation_running:
            self.stop_button.label.set_text('START')
            self.animation_running = False
        else:
            self.stop_button.label.set_text('STOP')
            self.animation_running = True
            self.animate()

    def move_right(self, event):
        if not self.animation_running:
            self.current_index += 50
            self.update_plot()

    def move_left(self, event):
        if not self.animation_running:
            self.current_index -= 50
            if self.current_index < 0:
                self.current_index = 0
            self.update_plot()

    def take_screenshot(self, event):
        if not self.animation_running:
            myScreenshot = pyautogui.screenshot(region=(100, 100, 1130, 700))
            myScreenshot.save(r'screenshot.png')
        else:
            print("Nie można zrobić screenshot")

    def run(self):
        self.update_plot()
        plt.show()


def main():
    data = nk.data("bio_resting_8min_100hz")["ECG"]
    ECGAnimation(data).run()


if __name__ == "__main__":
    main()
