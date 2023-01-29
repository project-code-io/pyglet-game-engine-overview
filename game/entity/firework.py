from pyglet import math, shapes
import random

class Firework(shapes.Rectangle):
    def __init__(self, batch):
        color_rgb = (random.randint(55, 255), random.randint(55, 255), random.randint(55, 255))
        super().__init__(x=0, y=0, width=5, height=5, color=color_rgb, batch=batch)
        self.exploded = False
        self.active = False
        self.gravity = 100
        self.velocity = math.Vec2(0, 0)
        self.timer = 0
        self.width = 10
        self.height = 10
        self.visible = False

    def init(self, position, velocity, time, exploded):
        self.active = True
        self.visible = True
        self.x = position.x
        self.y = position.y
        self.velocity = velocity
        self.timer = time
        self.exploded = exploded
        if not self.exploded:
            self.width = 10
            self.height = 10
        else:
            self.width = 5
            self.height = 5
                
    def update(self, dt):
        if not self.active:
            return False

        self.x = self.x + self.velocity.x * dt
        self.y = self.y + self.velocity.y * dt
        self.timer -= dt

        if self.timer <= 0:
            self.active = False
            self.visible = False

            if not self.exploded:
                return True

        return False
