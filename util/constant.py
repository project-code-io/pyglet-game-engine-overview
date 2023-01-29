import pyglet

screen_size = screen_width, screen_height = 1200, 900
center_x, center_y = screen_width/2, screen_height/2
radius = 200

green = (64, 160, 43)
blue = (30, 102, 245)
mauve = (136, 57, 239)

def load_animation(entity, state, frames):
    images = [pyglet.image.load("../assets/sprites/{e}/{s}/{e}-{s}-{x:02}.png".format(x=x, e=entity, s=state)) for x in range(frames)]

    for image in images:
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2

    frames = [pyglet.image.AnimationFrame(x, duration=0.1) for x in images]
    return pyglet.image.Animation(frames=frames)
