import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__) + "/../util"))

from pyglet.window import Window
from pyglet import app, shapes
import pyglet
from util.constant import *
import bar

window = Window(width=screen_width, height=screen_height)

batch = pyglet.graphics.Batch()
background = pyglet.graphics.Group(0)
foreground = pyglet.graphics.Group(1)

health_bg = shapes.Rectangle(
    x = center_x - 400,
    y = center_y - 50,
    width = 800,
    height = 100,
    color = (88, 69, 69),
    batch=batch,
    group=background
)

health = shapes.Rectangle(
    x = center_x - 400,
    y = center_y - 50,
    width = 500,
    height = 100,
    color = (255, 69, 69),
    batch=batch,
    group=foreground
)

@window.event
def on_draw():
    window.clear()
    batch.draw()

app.run()

