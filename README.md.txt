# EOG Signal Processing & Blink Detection Pipeline

A simple Python script demonstrating a complete Electrooculography (EOG) signal processing and blink detection pipeline. This project is designed as a beginner-friendly tutorial for working with biosignals using Python.

## Features
- **Synthetic EOG Simulation**: Generates realistic EOG data complete with random noise, baseline drift (wander), and simulated eye blinks.
- **Bandpass Filtering**: Implements a Butterworth bandpass filter ($0.1\text{ Hz}$ to $10\text{ Hz}$) using SciPy to remove unwanted noise and baseline wander.
- **Blink Detection**: Utilizes peak detection algorithms to automatically locate eye blinks on the filtered signal.
- **Data Visualization**: Uses Matplotlib to plot side-by-side comparisons of the raw noisy signal versus the cleaned signal with detected peaks.

This project is open source and available under the MIT License.
