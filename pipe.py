import random
import arcade
from game_variables import *

class Pipe(arcade.Sprite):

    def __init__(self, image, scale = 0.6):
        """ Initial pipes"""

        super().__init__(image, scale)

        self.horizontal_speed = -PIPE_SPEED

    @classmethod
    def random_size_pipe(cls, height, width):
        """ A class method creates two pipes each with minimum height of MIN_HEIGHT and minimum MIN_GAP distance
        between the two pipes."""
        bottom_pipe = cls(PIPES[0])
        bottom_pipe.top = random.randrange(0 + MIN_HEIGHT, height - GAP_SIZE - MIN_HEIGHT)
        bottom_pipe.left = width 

        top_pipe = cls(PIPES[0])
        top_pipe.angle = 180 #top pipe is upside down
        top_pipe.left = width  
        top_pipe.bottom = bottom_pipe.top + GAP_SIZE

        return bottom_pipe , top_pipe

    def update(self):
        self.center_x += self.horizontal_speed