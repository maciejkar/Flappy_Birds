import arcade
from game_variables import *


class Bird(arcade.Sprite):

    def __init__(self, center_x, center_y, filename):
        super().__init__(filename=filename,center_x=center_x, center_y=center_y)

        self.textures = []
        # self.textures.append(arcade.load_texture(BIRDS[0]))

        self.cur_texture_index = 0
        self.velocity =  0
        self.dy = 0
        self.dead = False

    def set_velocity(self, velocity):
        self.velocity = velocity

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