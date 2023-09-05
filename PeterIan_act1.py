import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data for the sound wave
sampling_rate = 1000  # Number of samples per second
frequency = 5  # Frequency of the wave in Hz
duration = 1  # Duration of the wave in seconds
t = np.linspace(0, duration, int(sampling_rate * duration))
wave = np.sin(2 * np.pi * frequency * t)

# Create the graph
plt.plot(t, wave)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sound Wave Graph')
plt.grid(True)
plt.show()