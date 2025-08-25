import wave
import struct
import math

def sine_wave(frequency, duration, sample_rate=44100, amplitude=32767):
    """Generate a sine wave of a given frequency and duration"""
    num_samples = int(duration * sample_rate)
    wave_data = []
    for i in range(num_samples):
        value = int(amplitude * math.sin(2 * math.pi * frequency * i / sample_rate))
        wave_data.append(value)
    return wave_data

def save_wave(filename, wave_data, sample_rate=44100):
    """Save wave_data to a WAV file"""
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        for sample in wave_data:
            wf.writeframes(struct.pack('<h', sample))
