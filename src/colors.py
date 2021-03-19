from cmath import tau

from math import sin
from src.graphics import color_rgb

def color_function(numerator, denominator):
    intensities = []
    for i in range(3):
        radians = tau * (numerator / denominator + i / 3)
        intensity = int((sin(radians) + 1) / 2 * 255)
        intensities.append(intensity)
    return color_rgb(intensities[0], intensities[1], intensities[2])
