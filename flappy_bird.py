#!/usr/bin/env python
import arcade
import os
from game_variables import *

class Game(arcade.Window):

    def __init__(self, width, height):
        """ Inite game window"""
        super().__init__(width, height, title="Flappy Birds")

        self.birds = None
        # Background texture
        self.background = None

    def setup(self):
        self.background = arcade.load_texture(BACKGROUNDS[0])

    def draw(self):
        """Funcion draw background"""
        arcade.draw_texture_rectangle(self.width // 2, self.height // 2, self.width, self.height, self.background, alpha=200 )

    def on_draw(self):
        """ This is the method called when the drawing time comes."""

        #render all objects
        arcade.start_render()

        self.draw()

def run_game():
    os.chdir(os.path.split(os.path.realpath(__file__))[0])
    game = Game(GAME_WIDTH, GAME_HEIGHT )
    game.setup()
    arcade.run()

if __name__ == "__main__":
    run_game()
    