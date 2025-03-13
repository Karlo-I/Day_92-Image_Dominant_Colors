import numpy as np

# Convert RGB to HEX
def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

# Euclidean distance between two RGB colors
def rgb_distance(rgb1, rgb2):
    return np.sqrt(sum((a - b) ** 2 for a, b in zip(rgb1, rgb2)))