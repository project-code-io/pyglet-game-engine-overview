from util.constant import *
from enum import Enum

class State(Enum):
    IDLE = 1
    RUNNING = 2

class Goblin:

    def __init__(self, batch):
        self.current_state = State.IDLE
        self.animations = {
            State.IDLE: load_animation(entity="goblin", state="idle", frames=8),
            State.RUNNING: load_animation(entity="goblin", state="run", frames=8)
        }

        ani = self.animations[self.current_state]

        self.sprite = pyglet.sprite.Sprite(
            img=ani,
            x = ani.get_max_width() // 2, 
            y = ani.get_max_height() // 2,
            batch=batch
        )

    def set_state(self, state):
        if self.current_state != state:
            self.current_state = state
            self.sprite.image = self.animations[state]

    def move_left(self, amount):
        self.sprite.x -= amount
        self.set_state(State.RUNNING)
        self.sprite.scale_x = -1
        animation = self.animations[self.current_state]
        if self.sprite.x - animation.get_max_width() // 2 < 0:
            self.sprite.x = animation.get_max_width() // 2

    def move_right(self, amount):
        self.sprite.x += amount
        self.set_state(State.RUNNING)
        self.sprite.scale_x = 1
        animation = self.animations[self.current_state]
        if self.sprite.x + animation.get_max_width() // 2 > screen_width:
            self.sprite.x = screen_width - animation.get_max_width() // 2
