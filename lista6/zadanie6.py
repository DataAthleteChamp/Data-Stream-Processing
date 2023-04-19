import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
import wfdb
import os
from scipy.signal import resample


# Download and load ECG data from PhysioNet
ecg_record_name = 'f1o01'
local_ecg_record_path = os.path.join('data', ecg_record_name)
if not os.path.exists(local_ecg_record_path + '.hea'):
    wfdb.dl_database('fantasia', dl_dir='data', records=[ecg_record_name])

ecg_record = wfdb.rdrecord(local_ecg_record_path)
ecg_data = ecg_record.p_signal[:, 0]  # Choose the ECG channel

# Download and load respiration data from PhysioNet
resp_record_name = 'f1o01'
local_resp_record_path = os.path.join('data', resp_record_name)
if not os.path.exists(local_resp_record_path + '.hea'):
    wfdb.dl_database('fantasia', dl_dir='data', records=[resp_record_name])

resp_record = wfdb.rdrecord(local_resp_record_path)
resp_data = resp_record.p_signal[:, 1]  # Choose the respiration channel

# The rest of the code remains the same as in the previous example




def plot_data(data, sampling, title):
    def update(val):
        y = data[int(sampling * start_slider.val): int(sampling * stop_slider.val)]
        x = np.linspace(start_slider.val, stop_slider.val, int(sampling * (stop_slider.val - start_slider.val)))
        if len(x) > len(y):
            while len(x) != len(y):
                x = np.append(x, x[-1])
        elif len(x) < len(y):
            while len(x) != len(y):
                y = np.append(y, y[-1])
        data_plot.set_ydata(y)
        data_plot.set_xdata(x)
        ax2.set_xlim(start_slider.val, stop_slider.val)
        fig.canvas.draw_idle()

    downsample_factor = 10
    data = resample(data, len(data) // downsample_factor)
    sampling = sampling / downsample_factor


    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle(title)
    ax1.plot(np.linspace(0, len(data) / sampling, len(data)), data)

    data_plot, = ax2.plot(np.linspace(0, len(data) / sampling, len(data)), data, color='red')
    fig.subplots_adjust(left=0.25, bottom=0.25)
    axstart = fig.add_axes([0.25, 0.1, 0.65, 0.03])
    axstop = fig.add_axes([0.25, 0.15, 0.65, 0.03])

    start_slider = Slider(
        ax=axstart,
        label='Start of data (s)',
        valmin=0,
        valmax=len(data) / sampling / 2,
        valinit=0,
        valstep=0.1)

    stop_slider = Slider(
        ax=axstop,
        label='Stop of data (s)',
        valmin=len(data) / sampling / 2,
        valmax=len(data) / sampling,
        valinit=len(data) / sampling,
        valstep=0.1)

    start_slider.on_changed(update)
    stop_slider.on_changed(update)
    plt.show()


# Plot ECG and respiration data
plot_data(data=ecg_data, sampling=ecg_record.fs, title='ECG Signal')
plot_data(data=resp_data, sampling=resp_record.fs, title='Respiration Signal')
