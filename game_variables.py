from os import sep

import arcade

GAME_WIDTH = 480 * 2
GAME_HEIGHT = 322 * 2
BACKGROUNDS = ["asserts" + sep + "Images" + sep + "background1.png"]
BIRDS = ["asserts" + sep + "Images" + sep + "bird1.png"]
PIPES = ["asserts" + sep + "Images" + sep + "green_pipe.png"]
GAME_OVER = ["asserts" + sep + "Images" + sep + "game_over.png"]
BUTTONS = {
    "play_again": "asserts" + sep + "Images" + sep + "play_again.png",
    "exit": "asserts" + sep + "Images" + sep + "exit.png",
    "play": "asserts" + sep + "Images" + sep + "play.png"}


SOUNDS = {
    'wing': arcade.load_sound('asserts' + sep + 'Sounds' + sep + 'wing.wav'),
    'die': arcade.load_sound('asserts' + sep + 'Sounds' + sep + 'die.wav'),
    'hit': arcade.load_sound('asserts' + sep + 'Sounds' + sep + 'hit.wav'),
    'point': arcade.load_sound('asserts' + sep + 'Sounds' + sep + 'point.wav'),
}

JUMP_DY = 60 # how many pixels bird per flap
DY = 2.4 # how many pixels bird per frame
GRAVITY = 2.45 #how many pixels gravity go down for frame
PIPE_SPEED = 1.7 #how fast pipes move
MIN_HEIGHT = 50 #minimum height od pipes
GAP_SIZE = 150 #minimum height of gap between top and bottom pipe
MIN_DISTACE_OF_PIPES = 320 # minimum distance between two pipes
MAX_DISTACE_OF_PIPES = 360 # maximum distance between two pipes

LIVES = 3
SCORE = {
    '0': 'asserts' + sep + 'Images' + sep + '0.png',
    '1': 'asserts' + sep + 'Images' + sep + '1.png',
    '2': 'asserts' + sep + 'Images' + sep + '2.png',
    '3': 'asserts' + sep + 'Images' + sep + '3.png',
    '4': 'asserts' + sep + 'Images' + sep + '4.png',
    '5': 'asserts' + sep + 'Images' + sep + '5.png',
    '6': 'asserts' + sep + 'Images' + sep + '6.png',
    '7': 'asserts' + sep + 'Images' + sep + '7.png',
    '8': 'asserts' + sep + 'Images' + sep + '8.png',
    '9': 'asserts' + sep + 'Images' + sep + '9.png',
    'texture': 'asserts' + sep + 'Images' + sep + 'score.png',
    '0b': 'asserts' + sep + 'Images' + sep + '0b.png', # The same but in black
    '1b': 'asserts' + sep + 'Images' + sep + '1b.png',
    '2b': 'asserts' + sep + 'Images' + sep + '2b.png',
    '3b': 'asserts' + sep + 'Images' + sep + '3b.png',
    '4b': 'asserts' + sep + 'Images' + sep + '4b.png',
    '5b': 'asserts' + sep + 'Images' + sep + '5b.png',
    '6b': 'asserts' + sep + 'Images' + sep + '6b.png',
    '7b': 'asserts' + sep + 'Images' + sep + '7b.png',
    '8b': 'asserts' + sep + 'Images' + sep + '8b.png',
    '9b': 'asserts' + sep + 'Images' + sep + '9b.png',
    'textureb': 'asserts' + sep + 'Images' + sep + 'scoreb.png',
}
