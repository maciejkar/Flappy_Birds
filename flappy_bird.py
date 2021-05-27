#!/usr/bin/env python
from pipe import Pipe
from Bird import Bird
from pipe import Pipe
import differents_views
import random
import arcade
import os
from game_variables import *

class GameView(arcade.View):

    def __init__(self):
        """ Inite game window"""
        super().__init__()
        self.width = GAME_WIDTH
        self.height = GAME_HEIGHT
        self.sprites = None
        self.pipe_sprites = None
        self.bird = None
        # Background texture
        self.background = None
        #List of birds
        self.bird_list = None
        self.flapped = False
        self.score = 0
        self.dx = 0 # how many pixels pipes move

    def setup(self):
        
        self.background = arcade.load_texture(BACKGROUNDS[0])
        self.bird_list = arcade.SpriteList()
        self.pipe_sprites = arcade.SpriteList()
        self.bird =Bird(self.width // 5, self.height // 2, BIRDS[0]) 
        self.bird_list.append(self.bird)
        self.sprites = dict()
        self.sprites['background'] = self.background

        # Create starts pipes
        start_pipes = Pipe.random_size_pipe(self.height,self.width)
        self.pipe_sprites.extend(start_pipes)

        
    def draw(self):
        """Funcion draw background"""
        arcade.draw_texture_rectangle(self.width // 2, self.height // 2, self.width, self.height, self.background, alpha=200 )

    def on_draw(self):
        """ This is the method called when the drawing time comes."""
        #render all objects
        arcade.start_render()

        self.draw()
        self.pipe_sprites.draw()
        self.bird_list.draw()

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            self.flapped = True


    def update(self,dt):
        
        if self.flapped:
            self.bird.flap()
            self.flapped = False

        # Check if bird is too high
        if self.bird.top > self.height:
            self.bird.top = self.height

        # Check if bird is too low
        if self.bird.bottom <= 0:
            self.bird.bottom = 0
        
        self.dx += PIPE_SPEED
        if self.dx > random.randrange(MIN_DISTACE_OF_PIPES, MAX_DISTACE_OF_PIPES):
            self.dx = 0
            new_pipe = Pipe.random_size_pipe(self.height, self.width)
            self.pipe_sprites.extend(new_pipe)

        for pipe in self.pipe_sprites:
            if pipe.right <= 0:
                pipe.kill()

        self.pipe_sprites.update()
        self.bird.update()

        hit = arcade.check_for_collision_with_list(self.bird, self.pipe_sprites)
        if any(hit):
            self.bird.die()
            view = differents_views.GameOverView()
            self.window.show_view(view)
        


def run_game():
    os.chdir(os.path.split(os.path.realpath(__file__))[0])
    window = arcade.Window(GAME_WIDTH, GAME_HEIGHT, "Flappy Bird")
    start_view = differents_views.StartView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    run_game()
    