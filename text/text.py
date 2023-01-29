import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__) + "/../util"))
sys.path.append(os.path.dirname(os.path.dirname(__file__) + "/../game"))

from pyglet.window import Window, key
from pyglet import app, shapes
import pyglet
from util.constant import *
from game.entity.goblin import Goblin, State

window = Window(width=screen_width, height=screen_height)
window.set_location(2250, 150)
batch = pyglet.graphics.Batch()
fps_display = pyglet.window.FPSDisplay(window=window)


label = pyglet.text.Label(
    'HELLO, YOUTUBE',
    font_name='Lilita One',
    font_size=72,
    x=center_x,
    y=center_y,
    anchor_x='center', 
    anchor_y='center',
    batch=batch
)

label.rotation = 180





@window.event
def on_draw():
    window.clear();
    batch.draw();
    fps_display.draw()

app.run()

