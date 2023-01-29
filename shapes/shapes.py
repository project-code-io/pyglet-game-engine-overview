import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__) + "/../util"))

from pyglet.window import Window
from pyglet import app, shapes
import pyglet
from util.constant import *

window = Window(width=screen_width, height=screen_height)
window.set_location(2250, 150)

batch = pyglet.graphics.Batch()

circle = shapes.Circle(
    x=center_x, y=center_y + radius * 1.1, 
    radius=radius, color=green, batch=batch
)

square = shapes.Rectangle(
    x=center_x, y=center_y - radius * 1.1, 
    width=radius * 2, height=radius * 2, color=blue, batch=batch
)
square.anchor_position = radius, radius


star = shapes.Star(
    x=center_x - radius * 2, 
    y=center_y, 
    outer_radius=radius, 
    inner_radius=radius / 2,
    num_spikes=5,
    rotation=55,
    color=mauve,
    batch=batch
)


star.scale = 0.5

square.rotation = 45

circle.color = (255, 255, 255)



@window.event
def on_draw():
    window.clear();
    batch.draw();

app.run()

