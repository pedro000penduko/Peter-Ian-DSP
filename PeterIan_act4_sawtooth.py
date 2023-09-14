from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
import numpy as np


class SawtoothSignal(Sinusoid):
    """Represents a sawtooth signal."""
    
    def evaluate(self, ts):
        """Evaluates the signal at the given times.

        ts: float array of times
        
        returns: float wave array
        """
        cycles = self.freq * ts + self.offset / np.pi / 2
        frac, _ = np.modf(cycles)
        ys = normalize(unbias(frac), self.amp)
        return ys

sawtooth = SawtoothSignal().make_wave(duration=0.5, framerate=40000)
sawtooth.make_audio()


import os
from thinkdsp import decorate
sawtooth.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')