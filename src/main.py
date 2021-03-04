from setup import window, draw_axes
from src.exercises.music_circle import music_circle
from src.fractals.rectangles import rectangle_fractal
from src.fractals.tree import tree_rotate

draw_axes()

music_circle(window)
# rectangle_fractal(window)
# tree_rotate(window)

window.getMouse()