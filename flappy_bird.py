#!/usr/bin/env python
import arcade
import os

class Game(arcade.Window):

    def __init__(self, width, height):
        """ Inite game window"""
        super().__init__(width, height, title="Flappy Birds")

        self.birds = None

def run_game():
    os.chdir(os.path.split(os.path.realpath(__file__))[0])
    game = Game(576, 712)
    arcade.run()

if __name__ == "__main__":
    run_game()
    