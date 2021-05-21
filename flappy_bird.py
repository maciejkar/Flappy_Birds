#!/usr/bin/env python
from Bird import Bird
import arcade
import os
from game_variables import *

class Game(arcade.Window):

    def __init__(self, width, height):
        """ Inite game window"""
        super().__init__(width, height, title="Flappy Birds")

        self.bird = None
        # Background texture
        self.background = None
        #List of birds
        self.bird_list = None

        self.flapped = False

    def setup(self):
        self.background = arcade.load_texture(BACKGROUNDS[0])
        self.bird_list = arcade.SpriteList()
        self.bird =Bird(self.width // 5, self.height // 2, self.height, BIRDS[0]) 
        self.bird_list.append(self.bird)
        self.sprites = dict()
        self.sprites['background'] = self.background
        
    def draw(self):
        """Funcion draw background"""
        arcade.draw_texture_rectangle(self.width // 2, self.height // 2, self.width, self.height, self.background, alpha=200 )

    def on_draw(self):
        """ This is the method called when the drawing time comes."""

        #render all objects
        arcade.start_render()

        self.draw()
        self.bird_list.draw()

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            self.flapped = True

    def update(self, dt):
        self.bird.update()

        if self.flapped:
            self.bird.flap()
            self.flapped = False

        # Check if bird is too high
        if self.bird.top > self.height:
            self.bird.top = self.height

        # Check if bird is too low
        if self.bird.bottom <= 0:
            self.bird.bottom = 0





def run_game():
    os.chdir(os.path.split(os.path.realpath(__file__))[0])
    game = Game(GAME_WIDTH, GAME_HEIGHT )
    game.setup()
    arcade.run()

if __name__ == "__main__":
    run_game()
    