import random
import arcade
from game_variables import *

class Pipe(arcade.Sprite):
    """Class of pipes"""
    def __init__(self, image, difficulty, scale = 0.6):
        """ Initial pipes
        @pam image: image of pipe
        @pam difficulty : 'easy' or 'hard' level of difficulty
        @pam scale: scale of image"""
        
        super().__init__(image, scale)
        self.difficulty = difficulty
        self.alpha = 255
        self.horizontal_speed = -PIPE_SPEED
        self.vertically_speed = PIPE_UP
        self.scored = False # Boolen expresion if bird passed this pipe

    @classmethod
    def random_size_pipe(cls, height, width, difficulty):
        """ A class method creates two pipes each with minimum height of MIN_HEIGHT and minimum MIN_GAP distance
        between the two pipes.
        @pam height: height of screen
        @pam width: width of screen
        @pam difficulty : 'easy' or 'hard' level of difficulty"""
        
        bottom_pipe = cls(PIPES[0], difficulty)
        bottom_pipe.top = random.randrange(0 + MIN_HEIGHT, height - GAP_SIZE - MIN_HEIGHT)
        bottom_pipe.left = width 

        top_pipe = cls(PIPES[0], difficulty)
        top_pipe.angle = 180 #top pipe is upside down
        top_pipe.left = width  
        top_pipe.bottom = bottom_pipe.top + GAP_SIZE

        return bottom_pipe , top_pipe

    def update(self):
        self.center_x += self.horizontal_speed
        if self.difficulty == 'hard':
            if self.angle == 180:
                if self.bottom > self.height - MIN_HEIGHT:
                    self.vertically_speed = -PIPE_UP
                elif self.bottom < MIN_HEIGHT + GAP_SIZE:
                    self.vertically_speed =  PIPE_UP
            else:
                if self.top < MIN_HEIGHT:
                    self.vertically_speed = PIPE_UP
                elif self.top > self._height - MIN_HEIGHT - GAP_SIZE:
                    self.vertically_speed = -PIPE_UP
            self.center_y += self.vertically_speed
