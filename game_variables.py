from os import sep

GAME_WIDTH = 480 * 2
GAME_HEIGHT = 322 * 2
BACKGROUNDS = ["asserts" + sep + "Images" + sep + "background1.png"]
BIRDS = ["asserts" + sep + "Images" + sep + "bird1.png"]
PIPES = ["asserts" + sep + "Images" + sep + "green_pipe.png"]
GAME_OVER = ["asserts" + sep + "Images" + sep + "game_over.png"]
BUTTONS = {"play_again": "asserts" + sep + "Images" + sep + "play_again.png" }

JUMP_DY = 60 # how many pixels bird per flap
DY = 2.4 # how many pixels bird per frame
GRAVITY = 2.45 #how many pixels gravity go down for frame
PIPE_SPEED = 1.5 #how fast pipes move
MIN_HEIGHT = 50 #minimum height od pipes
GAP_SIZE = 150 #minimum height of gap between top and bottom pipe
MIN_DISTACE_OF_PIPES = 320 # minimum distance between two pipes
MAX_DISTACE_OF_PIPES = 360 # maximum distance between two pipes
