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


goblin = Goblin(batch)

keys = key.KeyStateHandler()
window.push_handlers(keys)

goblin.speed = 400.0

def update(dt):
    if keys[key.D]:
        goblin.move_right(goblin.speed * dt)
    elif keys[key.A]:
        goblin.move_left(goblin.speed * dt)
    else:
        goblin.set_state(state=State.IDLE)

pyglet.clock.schedule_interval(update, 1/60.0)



@window.event
def on_draw():
    window.clear();
    batch.draw();
    fps_display.draw()

app.run()
