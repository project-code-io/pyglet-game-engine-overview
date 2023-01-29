import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__) + "/../util"))

from pyglet.window import Window
from pyglet import app, shapes
import pyglet
from util.constant import *

window = Window(width=screen_width, height=screen_height)
window.set_location(2250, 150)
fps_display = pyglet.window.FPSDisplay(
    window=window
)

batch = pyglet.graphics.Batch()

images = [pyglet.image.load("../assets/sprites/goblin/run/goblin-run-{x:02}.png".format(x = x)) for x in range(7)]
for image in images:
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2








def update(dt):
    print("Do something: {x}".format(x=dt))


pyglet.clock.schedule_interval(update, 1/60.0)















@window.event
def on_draw():
    window.clear();
    batch.draw();
    fps_display.draw()


app.run()
