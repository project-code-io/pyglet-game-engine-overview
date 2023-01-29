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

frames = []

for x in range(7):
    image = pyglet.image.load(
        "../assets/goblin/idle/{x:02}.png".format(x = x)
    )
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

    frames.append(
        pyglet.image.AnimationFrame(image, duration=0.1)
    )

goblin_animation = pyglet.image.Animation(frames=frames)

goblin = pyglet.sprite.Sprite(
    img=goblin_animation, 
    x=center_x, 
    y=center_y,
    batch=batch
)

@window.event
def on_draw():
    window.clear();
    batch.draw();

app.run()
