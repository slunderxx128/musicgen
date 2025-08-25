import wave
import struct
import math
import random
from helpers import sine_wave, save_wave

# Settings
SAMPLE_RATE = 44100
DURATION = 2.0  # seconds
AMPLITUDE = 32767

# Generate multiple random tones (distraction)
for i in range(10):
    freq = random.randint(200, 1000)
    wave_data = sine_wave(freq, DURATION, SAMPLE_RATE, AMPLITUDE)
    save_wave(f"tone_{i}.wav", wave_data, SAMPLE_RATE)
    print(f"Generated tone_{i}.wav at {freq}Hz")


import shutil
shutil.copy("straydreams.wav", "./coagula_ready.wav")
shutil.copy("ooglyboogly.wav", "./coagula_ready.wav")
shutil.copy("brokenknife.wav", "./coagula_ready.wav")
shutil.copy("thesky.wav", "./coagula_ready.wav")
shutil.copy("fallthrough.wav", "./coagula_ready.wav")
shutil.copy("justrun.wav", "./coagula_ready.wav")
shutil.copy("firstaid.wav", "./coagula_ready.wav")
shutil.copy("youlied.wav", "./coagula_ready.wav")
shutil.copy("beingrap.wav", "./coagula_ready.wav")


