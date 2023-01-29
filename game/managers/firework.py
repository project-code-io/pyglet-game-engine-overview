import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__) + "/../util"))
sys.path.append(os.path.dirname(os.path.dirname(__file__) + "/../game"))

import random
from game.entity.firework import Firework
from pyglet import math, media

class FireworkManager:
    def __init__(self, screen_width, num, batch):
        self.fireworks = [Firework(batch=batch) for x in range(num)]

        self.explosions = []
        for x in range(1, 7):
            self.explosions.append(
                media.load(
                    '../assets/audio/fw_{x:02}.ogg'.format(x=x), 
                    streaming=False
                )
            )

    def update(self, dt):
        for f in self.fireworks:
            exploded = f.update(dt)
            if exploded: 
                rand_idx = random.randint(0, len(self.explosions)-1)

                explosion = self.explosions[rand_idx]
                explosion.play()

                sparks = random.randint(20, 180)

                for i in range(sparks):
                    vec = math.Vec2()
                    vec = vec.from_polar(random.randint(50, 100), random.randint(0, 360))
                    self.add_firework(math.Vec2(f.x, f.y), vec, random.randint(10, 20), True)

    def add_firework(self, position, velocity, time, exploded):
        for firework in self.fireworks:
            if firework.active:
                continue

            firework.init(position, velocity, time, exploded)
            return True
        return False
