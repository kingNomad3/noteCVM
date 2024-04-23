import math
import time

def smooth_wave(elapsed_time, min, max, frequency):
    return (math.sin(elapsed_time * math.tau * frequency) * 0.5 + 0.5) * (max - min) + min

def step_wave(elapsed_time, min, max, frequency):
    return round((elapsed_time % frequency) / frequency) * (max - min) + min

def sawtooth_wave(elapsed_time, min, max, frequency):
    return (elapsed_time % frequency) / frequency * (max - min) + min

def blend_color(c1, c2, percent):
    inv_percent = 1.0 - percent
    return tuple(round(i1 * percent + i2 * inv_percent) for i1, i2 in zip(c1, c2))

def alternate_blend(color1, color2, percent):
    blend1 = blend_color(color1, color2, percent)
    blend2 = blend_color(color1, color2, 1.0 - percent)
    return (blend1, blend2)

def color_text(text, color):
    return f'\033[38;2;{color[0]};{color[1]};{color[2]}m{text}\033[0m'


block_char = '█'
block_length = 15
block_text = block_char * block_length
frequency = 1.0 / 1.0
color1 = (255, 0, 0)
color2 = (0, 0, 255)
wave = sawtooth_wave



while True:
    percent = wave(time.perf_counter(), 0.0, 1.0, frequency)
    blend1, blend2 = alternate_blend(color1, color2, percent)
    print(f"\r{color_text(block_text, blend1)}{color_text(block_text, blend2)}", sep = "", end="")
