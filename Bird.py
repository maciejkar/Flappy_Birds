import arcade
from game_variables import GRAVITY, DY, JUMP_DY, SOUNDS


class Bird(arcade.Sprite):
    """Class of Bird"""

    def __init__(self, center_x, center_y, filename):
        """Init Bird class
        @pam center_x: x cord of center of Bird
        @pam center_y: y cord of center of Bird
        @pam filename: filename with Bird texture """

        super().__init__(filename=filename,center_x=center_x, center_y=center_y)
        self.cur_texture_index = 0
        self.velocity =  0
        self.dy = 0
        self.dead = False

    
    def update(self):
        
        if self.velocity > 0:
            self.center_y += DY
            self.velocity -= DY

        else:
            self.center_y -= GRAVITY

    def flap(self):
        self.velocity = JUMP_DY

    def die(self):
        arcade.play_sound(SOUNDS['die'], 0.4)
        self.dead = True