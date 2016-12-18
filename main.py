#!/bin/python2

"""
Script to run the game
"""

import pygame
import sys
import time
import random

pygame.init()

class BrickBreaker:
        clock = pygame.time.Clock()

	def __init__(self, screen=None, ball=None, pad=None, bricks=None,
	             ball_config=None, pad_config=None, bgcolor=None):
		"""
		Initializes screen, ball, pad, bricks, background color and font
		"""
		self.screen = screen
		self.ball = ball
		self.ball_config = ball_config
		self.pad = pad
		self.pad_config = pad_config
		self.bricks = bricks
		self.brick_colors = [(201,41,76), (255,215,0)]
		self.bgcolor = bgcolor
		self.font = pygame.font.Font(None, 50)

        def draw_bricks(self):
		"""
		Draws the bricks on the screen and remove a brick if ball collides.
		"""
                for brick in self.bricks[0]:
			if self.ball.colliderect(brick):
				self.ball_config[2] = -self.ball_config[2]
				self.bricks[0].remove(brick)
			else:
				pygame.draw.rect(self.screen,self.brick_colors[0],brick)

		for spcl_brick in self.bricks[1]:
			if self.ball.colliderect(spcl_brick):
				self.ball_config[2] = -self.ball_config[2]
				self.bricks[1].remove(spcl_brick)
				self.bricks[0].append(spcl_brick)
				pygame.draw.rect(self.screen,self.brick_colors[0],spcl_brick)
			else:
				pygame.draw.rect(self.screen,self.brick_colors[1],spcl_brick)
				
	def draw_pad(self):
		"""
		Draws the pad on the screen
		"""
		pygame.draw.rect(self.screen, self.pad_config[2], self.pad)

	def draw_ball(self):
		"""
		Draws the ball on the screen
		"""
		pygame.draw.circle(self.screen, self.ball_config[3],
		                   (self.ball.left, self.ball.top), self.ball_config[0])

	def draw_components(self):
		"""
		Draws all components on the screen
		"""
		self.draw_bricks()
		self.draw_ball()
		self.draw_pad()

        def msg(self,message, pos_x, pos_y, fontcolor=(255,255,255)):
		"""
		Writes any colored message on the screen at position provided in arguments
		"""
                if self.font:
                        text = self.font.render(message, 1, fontcolor)
                        textpos = (pos_x, pos_y)
                        self.screen.blit(text, textpos)
 
        def main(self):
		"""
		Loops the game until user quits

		A row of bricks is added every 3.5 minutes of play
		"""
                                
		move = False
                
		pad_left = False
                pad_right = False
                                
		lives = 3
                flag = False

		now = pygame.time.get_ticks()
                
                while True:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
					sys.exit()
                                elif event.type  == pygame.KEYDOWN:
                                        if event.key == pygame.K_LEFT:
                                                pad_left = True
                                        elif event.key == pygame.K_RIGHT:
                                                pad_right = True

                                elif event.type == pygame.KEYUP:
                                        if event.key == pygame.K_SPACE:
                                                move = True
                                        elif event.key == pygame.K_LEFT:
                                                pad_left = False
                                        elif event.key == pygame.K_RIGHT:
                                                pad_right = False

                        if ((((pygame.time.get_ticks()-now)/1000)+1) % 210) == 0 and move:
                                time.sleep(0.04)
                                for brcks in self.bricks:
					for brick in brcks:
                                        	brick.top = brick.top+1

                        if move:
                                self.ball.left -= self.ball_config[1]
                                self.ball.top += self.ball_config[2]

                                if self.ball.left <= 0: 
                                        self.ball.left=0
                                        self.ball_config[1] = -self.ball_config[1]

                                elif self.ball.left >= self.screen.get_width() - 10:
                                        self.ball.left = self.screen.get_width() - 10 
                                        self.ball_config[1] = -self.ball_config[1]

                                if self.ball.top <= 10:
                                        self.ball.top = 10
                                        self.ball_config[2] = -self.ball_config[2]

                                elif self.ball.top > self.screen.get_height():
                                        self.ball_config[2] = -self.ball_config[2]
                                        move = False
                                        
					self.ball.left = 380
                                        self.ball.top = 460
                                        
					self.pad.left = 350
                                        self.pad.top = 470

					lives -= 1
					if lives != 0:
						time.sleep(0.5)
						self.msg('Try again!!', 230, 100)
						time.sleep(0.5)

					elif lives == 0:
						self.msg('Game Over', 230, 100)
						pygame.display.flip()

						self.screen.fill(self.bgcolor)
						time.sleep(2)

						lives = 4
						flag = True

					pygame.display.flip()
                                
				if self.ball.colliderect(self.pad):
                                        self.ball.top = 454
                                        self.ball_config[2] = -self.ball_config[2]

                        if pad_left:
                                self.pad.left -= 7

                                if self.pad.left <= 0:
                                        self.pad.left = 0
                                
				if self.ball.top==460 and self.pad.top==470:
                                        self.pad.left -= 7
                                        self.ball.left -= 14
                                
					if self.ball.left <= 20:
                                                self.ball.left = 20

                        if pad_right:
                                self.pad.right+=7

                                if self.pad.left >= self.screen.get_width() - self.pad.width:
                                        self.pad.left = self.screen.get_width() - self.pad.width

                                if self.ball.top==460 and self.pad.top==470:
                                        self.pad.right += 7
                                        self.ball.right += 14

                                        if self.ball.right >= 620:
                                                self.ball.left = 620

                        self.screen.fill(self.bgcolor)

                        self.clock.tick(50)
                        self.draw_components()
                        
                        if lives >= 0:
                                self.msg('Lives : {}'.format(lives), 240, 5)

                        brick_count=0 
                        for brcks in self.bricks:
				for brick in brcks:
                                	if brick.top > 0 :
                                        	brick_count += 1

                        if brick_count == 0 and lives != 0 and not flag:
                                        self.msg('You Win',230 , 100)
                                        
					pygame.display.flip()
                                        
					self.screen.fill(self.bgcolor)
                                        time.sleep(2)

                                        lives=4
					move = False

					self.ball.left=380
					self.ball.top=460

					self.pad.left=350
					self.pad.top=470
      
                        pygame.display.flip()
