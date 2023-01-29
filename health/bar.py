from pyglet import graphics, shapes

background = graphics.Group(0)
midground = graphics.Group(1)
foreground = graphics.Group(2)

class Bar:
    def __init__(self, x, y, width, height, color, value=1, max=1, batch=graphics.Batch()):
        self.__background = shapes.Rectangle(
            x=x, y=y, width=width, height=height, color=(0,0,0), batch=batch, group=background
        )
        self.__mid = shapes.Rectangle(x=x, y=y, width=width, height=height, color=(69, 69, 69, 150), batch=batch, group=midground)
        self.__foreground = shapes.Rectangle(x=x, y=y, width=width, height=height, color=color, batch=batch, group=foreground)
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__value = value
        self.__max = max
        self.batch = batch
        self.__set_width()

    def __set_width(self):
        percentage = self.__value / self.__max
        width = self.__width * percentage
        self.__foreground.width = width

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def max(self):
        return self.__max

    @max.setter
    def max(self, value):
        self.__max = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    def draw():
        self.batch.draw()

