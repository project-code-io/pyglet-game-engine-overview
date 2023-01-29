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

frames = [pyglet.image.AnimationFrame(x, duration=0.1) for x in images]
goblin_animation = pyglet.image.Animation(frames=frames)

goblin = pyglet.sprite.Sprite(
    img=goblin_animation, 
    x = goblin_animation.get_max_width() // 2, 
    y = goblin_animation.get_max_height() // 2,
    batch=batch
)


goblin.speed = 200.0

def update(dt):
    goblin_width = goblin_animation.get_max_width()
    goblin_radius = goblin_width // 2
    goblin.x += goblin.speed * dt
    goblin_right = goblin.x + goblin_radius
    goblin_left = goblin.x - goblin_radius

    if goblin_right > screen_width:
        goblin.speed *= -1
        goblin.scale_x = -1
        goblin.x = screen_width - goblin_radius

    if goblin_left < 0:
        goblin.speed *= -1
        goblin.scale_x = 1
        goblin.x = goblin_radius

pyglet.clock.schedule_interval(update, 1/60.0)




@window.event
def on_draw():
    window.clear();
    batch.draw();
    fps_display.draw()


app.run()
