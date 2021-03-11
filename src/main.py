from src.graphics import color_rgb
from src.hexagon_madness import hexagonal_madness
from src.setup import window

window.setBackground(color_rgb(250, 245, 255))

hexagonal_madness(window)

window.getMouse()
