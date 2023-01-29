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

goblin_animation = pyglet.image.load_animation(
    '../assets/goblin-idle.gif'
)

goblin = pyglet.sprite.Sprite(
    img=goblin_animation,
    x = center_x - goblin_animation.get_max_width() // 2,
    y = center_y - goblin_animation.get_max_height() // 2,
    batch=batch
)

@window.event
def on_draw():
    window.clear();
    batch.draw();

app.run()
