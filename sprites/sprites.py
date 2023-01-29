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

# Image
goblin_image = pyglet.image.load('../assets/goblin.png')
goblin_image.anchor_x = goblin_image.width // 2
goblin_image.anchor_y = goblin_image.height // 2

# Sprite
goblin = pyglet.sprite.Sprite(
    goblin_image,
    x=center_x,
    y=center_y,
    batch=batch
)

# Flip horizontally
goblin.scale_x = -1

# rotate slightly to go uphill
goblin.rotation = 8

@window.event
def on_draw():
    window.clear();
    batch.draw();

app.run()
