import arcade
import flappy_bird
from arcade.gui import  UIImageButton
from game_variables import *
import sys

class PlayAgainButton(UIImageButton):
    def __init__(self, center_x, center_y,normal_texture=arcade.load_texture(BUTTONS["play_again"]) ):
        super().__init__(normal_texture,center_x=center_x, center_y=center_y,)
    def on_click(self):
        view = flappy_bird.GameView()
        view.setup()
        view.window.show_view(view)
class ExiteButton(UIImageButton):
    def __init__(self, center_x, center_y,normal_texture=arcade.load_texture(BUTTONS["exit"]) ):
        super().__init__(normal_texture,center_x=center_x, center_y=center_y,)
    def on_click(self):
        sys.exit()
