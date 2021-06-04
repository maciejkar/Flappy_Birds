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
        self.name = arcade.load_texture(LABELS['name'])
        self.play_label = arcade.load_texture(LABELS['how_to_play'])
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
        button_exit = buttons.ExiteButton(self.width - self.exit_texture.width //2  , self.exit_texture.height * 0.65 , self.exit_texture)
        self.ui_menager.add_ui_element(button_exit)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(self.width //2 , self.height // 2, self.width, self.height, self.background)
        arcade.draw_scaled_texture_rectangle(self.width // 2, self.height - self.name.height * 0.6, self.name)
        arcade.draw_scaled_texture_rectangle(self.width // 2, self.play_label.height * 0.65 , self.play_label)
    
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            game_view = flappy_bird.GameView()
            game_view.setup()
            self.window.show_view(game_view)

class GameOverView(arcade.View):
    """View with game over"""
    def __init__(self, score, score_width, pipes, bird):
        super().__init__()
        self.background = arcade.load_texture(BACKGROUNDS[0])
        self.width = GAME_WIDTH
        self.height = GAME_HEIGHT
        self.score_y = None
        self.score_x = None
        self.score_width = score_width
        self.score = score
        self.piepes = pipes
        self.bird = bird
        self.number_width = arcade.load_texture(SCORE['1b']).width
        self.game_over = arcade.load_texture(GAME_OVER[0])
        self.score_texture = arcade.load_texture(SCORE['textureb'])
        self.play_again_texture = arcade.load_texture(BUTTONS["play_again"])
        self.exit_texture = arcade.load_texture(BUTTONS["exit"])
        self.menu_texture = arcade.load_texture(BUTTONS['menu'])
        self.ui_menager = UIManager()

    def on_hide_view(self):
        self.ui_menager.unregister_handlers()

    def on_show_view(self):
        self.setup()

    def setup(self):
        self.ui_menager.purge_ui_elements()
        button_play_again = buttons.PlayAgainButton(self.width //2 , self.height // 4, self.play_again_texture)
        button_exit = buttons.ExiteButton(self.width - self.exit_texture.width //2  , self.exit_texture.height * 0.6 , self.exit_texture)
        button_menu = buttons.MenuButton(self.menu_texture.width // 2, self.menu_texture.height * 0.6)
        self.ui_menager.add_ui_element(button_play_again)
        self.ui_menager.add_ui_element(button_exit)
        self.ui_menager.add_ui_element(button_menu)
        self.score_y = (self.height - self.game_over.height  - button_play_again.height // 2) // 2 + button_play_again.height // 2 + self.height // 4
        self.score_x = (self.width - self.score_width - self.score_texture.width // 10)  //2 
        arcade.start_render()
        arcade.draw_texture_rectangle(self.width //2 , self.height // 2, self.width, self.height, self.background)
        self.piepes.draw()
        self.bird.draw()
        arcade.draw_scaled_texture_rectangle(self.width // 2 ,self.game_over.height, self.game_over,)
        arcade.draw_scaled_texture_rectangle(self.score_x, self.score_y, self.score_texture)
        left = self.score_x + self.score_texture.width // 2  +  self.number_width
        for digit in str(self.score):
            arcade.draw_scaled_texture_rectangle(center_x=left + self.number_width *1.2 // 2, center_y=self.score_y, texture=arcade.load_texture(SCORE[digit + 'b']))
            left += self.number_width *1.2
    