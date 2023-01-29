import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__) + "/../util"))

from pyglet.window import Window
from pyglet import app, shapes
import pyglet
from util.constant import *

window = Window(width=screen_width, height=screen_height)
window.set_location(2250, 150)

# Image
goblin_image = pyglet.image.load('../assets/goblin.png')
goblin_image.anchor_x = goblin_image.width // 2
goblin_image.anchor_y = goblin_image.height // 2

@window.event
def on_draw():
    window.clear();
    goblin_image.blit(center_x, center_y);

app.run()

























