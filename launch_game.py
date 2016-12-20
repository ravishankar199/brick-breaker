import pygame
import random
from components import Pad, Ball, Brick
from main import BrickBreaker
from ConfigParser import RawConfigParser

CONFIG = RawConfigParser()
CONFIG.read('./.config')

def create_bricks(row_count, col_count, width, height, special_count):
    """
    Creates and returns a list of 2 lists - normal bricks and special bricks
    """
    
    # spaces between bricks
    space_y=5
    space_x=10
 
    # start placing bricks from these pointers
    hor_ptr = 5
    ver_ptr = -120
 
    bricks=[]

    for _ in range(row_count):
        hor_ptr = 5
        for __ in range(col_count):
	    # append a Brick to the list of bricks
            bricks.append(Brick(init_x=hor_ptr, init_y=ver_ptr, width=width, height=height).create())

            hor_ptr += width + space_x
        ver_ptr += height + space_y


    # get a random sample from all the bricks created
    # delete chosen sample from the original list of bricks
    special_bricks = random.sample(bricks, special_count)
    bricks = [brick for brick in bricks if brick not in special_bricks]

    all_bricks = [bricks, special_bricks]

    return all_bricks

if __name__=='__main__':
    """
    Initialize screen and all components and launch the game
    """

    # initializing from config
    game_config = {}
    game_config['screen_width'] = CONFIG.getint('SCREEN', 'WIDTH')
    game_config['screen_height'] = CONFIG.getint('SCREEN', 'HEIGHT')
    game_config['screen_bgcolor'] = [int(rgb) for rgb in CONFIG.get('SCREEN', 'BGCOLOR').split(',')]

    game_config['ball_init_x'] = CONFIG.getint('BALL', 'INIT_X')
    game_config['ball_init_y'] = CONFIG.getint('BALL', 'INIT_Y')
    game_config['ball_radius'] = CONFIG.getint('BALL', 'RADIUS')
    game_config['ball_color'] = [int(rgb) for rgb in CONFIG.get('BALL', 'COLOR').split(',')]
    game_config['ball_hor_velocity'] = CONFIG.getint('BALL', 'HORIZONTAL_VELOCITY')
    game_config['ball_ver_velocity'] = CONFIG.getint('BALL', 'VERTICAL_VELOCITY')
    
    game_config['brick_width'] = CONFIG.getint('BRICK', 'WIDTH')
    game_config['brick_height'] = CONFIG.getint('BRICK','HEIGHT')
    game_config['brick_row_count'] = CONFIG.getint('BRICK', 'ROWCOUNT')
    game_config['brick_col_count'] = CONFIG.getint('BRICK', 'COLCOUNT')
    game_config['brick_special_count'] = CONFIG.getint('BRICK', 'SPECIALCOUNT')

    game_config['pad_width'] = CONFIG.getint('PAD','WIDTH')
    game_config['pad_height'] = CONFIG.getint('PAD', 'HEIGHT')
    game_config['pad_init_x'] = CONFIG.getint('PAD', 'INIT_X')
    game_config['pad_init_y'] = CONFIG.getint('PAD', 'INIT_Y')
    game_config['pad_color'] = [int(rgb) for rgb in CONFIG.get('PAD', 'COLOR').split(',')]
 
    game_config['lives'] = CONFIG.getint('GAME', 'LIVES')

    # setting screen and creating ball and pad
    screen = pygame.display.set_mode((game_config['screen_width'], game_config['screen_height']),0,32)

    pad = Pad(width=game_config['pad_width'], height=game_config['pad_height'],
              init_x=game_config['pad_init_x'], init_y=game_config['pad_init_y'],
              color=game_config['pad_color']).create()

    ball = Ball(radius=game_config['ball_radius'], init_x=game_config['ball_init_x'],
                init_y=game_config['ball_init_y'], color=game_config['ball_color'],
                hor_vel=game_config['ball_hor_velocity'],
                ver_vel=game_config['ball_ver_velocity']).create()


    while True:
        # create new bricks before each game
	bricks = create_bricks(game_config['brick_row_count'],
	                       game_config['brick_col_count'],
			       game_config['brick_width'],
	                       game_config['brick_height'],
	                       game_config['brick_special_count'])


   	# initializing main game with components and their config
    	brick_breaker = BrickBreaker(screen=screen, ball=ball[0], pad=pad[0], bricks=bricks,
                                 ball_config=ball[1],pad_config=pad[1], lives=game_config['lives'],
				 bgcolor=game_config['screen_bgcolor'])

    	# launching the game
    	brick_breaker.main()
