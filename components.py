import pygame

class Ball:
    def __init__(self, radius=0, init_x=0, init_y=0, hor_vel=0, ver_vel=0, color=None):
        self.radius = radius
        self.pos_x = init_x
        self.pos_y = init_y
        self.hor_vel = hor_vel
	self.ver_vel = ver_vel
        self.color = color

    def create(self):
        ball_config = [self.radius, self.hor_vel, self.ver_vel, self.color]
        return [pygame.Rect(self.pos_x, self.pos_y, self.radius, 0), ball_config]

class Pad:
    def __init__(self, width=0, height=0, init_x=0, init_y=0, color=None):
        self.width = width
        self.height = height
        self.pos_x = init_x
        self.pos_y = init_y
        self.color = color

    def create(self):
        pad_config = [self.width, self.height, self.color]
        return [pygame.Rect(self.pos_x, self.pos_y, self.width, self.height),pad_config]


class Brick:
    def __init__(self, width=0, height=0, init_x=0, init_y=0):
        self.width = width
        self.height = height
        self.pos_x = init_x
        self.pos_y = init_y
        
    def create(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

class Background(pygame.sprite.Sprite):
        def __init__(self, image_file, location):
                pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
                self.image = pygame.image.load(image_file)
                self.rect = self.image.get_rect()
                self.rect.left, self.rect.top = location

