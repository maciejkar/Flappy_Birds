import arcade 
import flappy_bird
import buttons
from game_variables import *
from arcade.gui import UIManager

class StartView(arcade.View):
    """View with start"""
    def __init__(self):
        super().__init__()
        self.background = arcade.load_texture(BACKGROUNDS[0])
        self.width = GAME_WIDTH
        self.height = GAME_HEIGHT
        self.exit_texture = arcade.load_texture(BUTTONS["exit"])
        self.ui_menager = UIManager()


    def on_show(self):
        arcade.start_render()

    def on_hide_view(self):
        self.ui_menager.unregister_handlers()
    
    def on_show_view(self):
        self.setup()
        
    def setup(self):
        self.ui_menager.purge_ui_elements()
        button_exit = buttons.ExiteButton(self.width - self.exit_texture.width //2  , self.exit_texture.height //2 , self.exit_texture)
        self.ui_menager.add_ui_element(button_exit)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(self.width //2 , self.height // 2, self.width, self.height, self.background)

    
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            game_view = flappy_bird.GameView()
            game_view.setup()
            self.window.show_view(game_view)

class GameOverView(arcade.View):
    """View with game over"""
    def __init__(self):
        super().__init__()
        self.background = arcade.load_texture(BACKGROUNDS[0])
        self.width = GAME_WIDTH
        self.height = GAME_HEIGHT
        self.game_over = arcade.load_texture(GAME_OVER[0])
        self.play_again_texture = arcade.load_texture(BUTTONS["play_again"])
        self.exit_texture = arcade.load_texture(BUTTONS["exit"])
        self.ui_menager = UIManager()

    def on_hide_view(self):
        self.ui_menager.unregister_handlers()

    def on_show_view(self):
        self.setup()

    def setup(self):
        self.ui_menager.purge_ui_elements()
        button_play_again = buttons.PlayAgainButton(self.width //2 , self.height // 4, self.play_again_texture)
        button_exit = buttons.ExiteButton(self.width - self.exit_texture.width //2  , self.exit_texture.height //2 , self.exit_texture)
        self.ui_menager.add_ui_element(button_play_again)
        self.ui_menager.add_ui_element(button_exit)
        
    def on_draw(self):
       
        arcade.start_render()
        arcade.draw_texture_rectangle(self.width //2 , self.height // 2, self.width, self.height, self.background)
        arcade.draw_scaled_texture_rectangle(self.width //2 ,self.game_over.height, self.game_over,)
