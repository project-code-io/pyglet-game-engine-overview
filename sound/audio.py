import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__) + "/../util"))
sys.path.append(os.path.dirname(os.path.dirname(__file__) + "/../game"))

from pyglet.window import Window, key
from pyglet import app, math
import pyglet
from util.constant import *
from game.entity.firework import Firework
from game.managers.firework import FireworkManager
import random

window = Window(width=screen_width, height=screen_height)
window.set_location(2250, 150)

batch = pyglet.graphics.Batch()
fps_display = pyglet.window.FPSDisplay(window=window)

manager = FireworkManager(screen_width=screen_width, num=1000, batch=batch)

manager.add_firework(math.Vec2(screen_width // 2, 0), math.Vec2(0, 500), 1, False)

last = 0

def update(dt):
    global last
    if random.randint(0, 400 - last) == 1:
        last = 0
        x = random.randint(screen_width * 0.25, screen_width * 0.75)
        vel = math.Vec2().from_polar(random.randint(40, 80), random.randint(80, 100))
        time = random.randint(7, 11) / 10.0
        manager.add_firework(math.Vec2(x, 0), math.Vec2(vel.x, 600), time, False)
    manager.update(dt)
    last += 1

@window.event
def on_draw():
    window.clear();
    batch.draw();

pyglet.clock.schedule_interval(update, 1/60.0)

app.run()

