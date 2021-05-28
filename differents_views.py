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
    def __init__(self, score, score_width):
        super().__init__()
        self.background = arcade.load_texture(BACKGROUNDS[0])
        self.width = GAME_WIDTH
        self.height = GAME_HEIGHT
        self.score_y = None
        self.score_x = None
        self.score_width = score_width
        self.score = score
        self.number_width = arcade.load_texture(SCORE['1b']).width
        self.game_over = arcade.load_texture(GAME_OVER[0])
        self.score_texture = arcade.load_texture(SCORE['textureb'])
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
        self.score_y = (self.height - self.game_over.height  - button_play_again.height // 2) // 2 + button_play_again.height // 2 + self.height // 4
        self.score_x = (self.width - self.score_width - self.score_texture.width // 10)  //2 
        arcade.start_render()
        arcade.draw_texture_rectangle(self.width //2 , self.height // 2, self.width, self.height, self.background)
        arcade.draw_scaled_texture_rectangle(self.width // 2 ,self.game_over.height, self.game_over,)
        arcade.draw_scaled_texture_rectangle(self.score_x, self.score_y, self.score_texture)
        left = self.score_x + self.score_texture.width // 2  +  self.number_width
        for digit in str(self.score):
            arcade.draw_scaled_texture_rectangle(center_x=left + self.number_width *1.2 // 2, center_y=self.score_y, texture=arcade.load_texture(SCORE[digit + 'b']))
            left += self.number_width *1.2
    