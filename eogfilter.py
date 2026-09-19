import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks

# ==========================================
# 1. Simulate a Synthetic EOG Signal
# ==========================================
# In a real-world scenario, you would load your data from a CSV or EDF file using pandas/mne.
fs = 250  # Sampling frequency in Hz (250 samples per second)
duration = 10  # Duration in seconds
time = np.linspace(0, duration, fs * duration)

# Create a baseline signal with some random noise
np.random.seed(42)
eog_signal = np.random.normal(0, 0.1, len(time))

# Add low-frequency baseline wander (drift)
baseline_wander = 0.5 * np.sin(2 * np.pi * 0.2 * time)
eog_signal += baseline_wander

# Inject synthetic "blinks" or large peaks at specific time points
blink_indices = [int(2.5 * fs), int(5.0 * fs), int(8.2 * fs)]
for idx in blink_indices:
    # A typical blink looks like a sharp positive-negative deflection or prominent peak
    blink_shape = np.exp(-((np.arange(-50, 50))**2) / 200) * 2.5
    eog_signal[idx-50:idx+50] += blink_shape

# ==========================================
# 2. Design a Bandpass Filter
# ==========================================
# EOG signals typically contain useful energy between 0.1 Hz and 10 Hz.
def butter_bandpass(lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=4):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = filtfilt(b, a, data)
    return y

# Apply filter (0.1 Hz to 10 Hz)
lowcut = 0.1
highcut = 10.0
filtered_eog = bandpass_filter(eog_signal, lowcut, highcut, fs, order=4)

# ==========================================
# 3. Peak Detection (e.g., Blink Detection)
# ==========================================
# Find peaks in the filtered signal that exceed a certain threshold
peaks, _ = find_peaks(filtered_eog, height=1.0, distance=fs*0.5)

# ==========================================
# 4. Plotting the Results
# ==========================================
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(time, eog_signal, color='gray', label='Raw EOG with Noise & Drift')
plt.title('EOG Signal Processing Pipeline - Beginner Tutorial')
plt.ylabel('Amplitude (mV)')
plt.legend(loc='upper right')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(time, filtered_eog, color='blue', label='Filtered EOG (0.1 - 10 Hz)')
plt.plot(time[peaks], filtered_eog[peaks], 'ro', label='Detected Blinks')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude (mV)')
plt.legend(loc='upper right')
plt.grid(True)

plt.tight_layout()
plt.show()
