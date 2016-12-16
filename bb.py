import pygame
import sys
import time
import random
screen=640,480
b_width=30
b_height=20
dia=16
rad=dia/2
pad_width=60
pad_height=10
green=(0,255,0)
black=(0,0,0)
red=(201,41,76)
gold=(255,215,0)
padmax_x=screen[0]-pad_width
screen1=pygame.display.set_mode(screen,0,32)
#ball=pygame.Rect(340,452,rad,0)
b_vel = [3, -3]
pad=pygame.Rect(350,470,pad_width,pad_height)

class brick:
	ball=pygame.Rect(380,460,rad,0)
	clock = pygame.time.Clock()
	def create_bricks(self,s,e):
		y=-120
   		self.bricks=[]
   		for i in range(s):
     			x=5
     			for j in range(e):
       				self.bricks.append(pygame.Rect(x,y,b_width,b_height))
       				x= x+b_width+10
     			y=y+b_height+5
   		self.new=[]
   		self.new=random.sample(self.bricks,15)
 

 	def draw_rect(self):
    		for brick in self.bricks:
     			if brick in self.new:
      				pygame.draw.rect(screen1,gold,brick)
     			else:
      				pygame.draw.rect(screen1,red,brick)
     			if self.ball.colliderect (brick):  
           			b_vel[1] = -b_vel[1]
           			if brick in self.new:
             				pygame.draw.rect(screen1,red,brick)
             				self.new.remove(brick)
           			else:
             				self.bricks.remove(brick)

      
 	def msg(self,message,x,y):
     		if self.font:
       			#font = pygame.font.Font(None, 115)
       			text = self.font.render(message, 1, (255, 255, 255))
       			textpos = (x,y)
       			#textpos.centerx = background.get_rect().centerx
       			screen1.blit(text, textpos)
 
 	def main(self):
   		pygame.init()
   		move=0
   		pad_left=0
   		pad_right=0
   		self.font = pygame.font.Font(None, 50)
   		life=3
   		q=random.randint(6,11)
   		r=16
   		now=pygame.time.get_ticks()
   		self.create_bricks(q,r)
   		while True:
      			for event in pygame.event.get():
        			if event.type == pygame.QUIT:
	   				return
				elif event.type  == pygame.KEYDOWN:
           				if event.key == pygame.K_LEFT:
              					pad_left = True
	   				elif event.key == pygame.K_RIGHT:
              					pad_right = True

				elif event.type == pygame.KEYUP:
	   				if event.key == pygame.K_SPACE:
	      					move = True
   	   				elif event.key == pygame.K_LEFT:
              					pad_left = 0
   	   				elif event.key == pygame.K_RIGHT:
              					pad_right = 0
      			'''print (((pygame.time.get_ticks()-now) / 1000)+1)%10'''
      			if ((((pygame.time.get_ticks()-now)/1000)+1) % 210) == 0 and move:
          			time.sleep(0.04)
          			for brick in self.bricks:
              				brick.top=brick.top+1
	  			'''x=5
	  			for j in range(16):
	       				self.bricks.insert(0,pygame.Rect(x,45,b_width,0))
	       				x= x+b_width+10'''
	       
      			if move:
          			self.ball.left-=b_vel[0]
          			self.ball.top+=b_vel[1]
          			if self.ball.left<=0: 
             				self.ball.left=0
             				b_vel[0]=-b_vel[0]
          			elif self.ball.left>=630:
             				self.ball.left=630 
             				b_vel[0]=-b_vel[0] 
          			if self.ball.top<=10:
             				self.ball.top=10
             				b_vel[1]=-b_vel[1]
          			elif self.ball.top>480: 
             				self.ball.top=470
             				b_vel[1]=-b_vel[1]
             				move = False
             				self.ball.left=380
             				self.ball.top =460
             				pad.left=350
             				pad.top=470             
          			if self.ball.colliderect (pad):
           				self.ball.top = 454
           				b_vel[1] = -b_vel[1]

      			if pad_left:
	  			pad.left-=7
	  			if pad.left<=0:
	    				pad.left=0
          			if(self.ball.top ==460 and pad.top==470):
	    				pad.left-=7
	    				self.ball.left-=14
	    				if(self.ball.left <= 20):
						self.ball.left = 20

      			if pad_right:
	  			pad.right+=7
          			if pad.left>=640-pad_width:
	    				pad.left=640-pad_width
	  			if(self.ball.top ==460 and pad.top==470):
            				pad.right+=7
            				self.ball.right+=14
	    				if(self.ball.right >= 620):
                				self.ball.left = 620

      			screen1.fill(black)
      			self.clock.tick(50)
      			self.draw_rect()
      			pygame.draw.rect(screen1,green,pad)
      			pygame.draw.circle(screen1,(255,255,255),(self.ball.left,self.ball.top),rad)
      			if life >= 0:
         			self.msg('Lives : ' + str(life),240,5)
      			if self.ball.top>=475:
	 			if(life != 0) :
          				time.sleep(0.5) 
	  				self.msg('Try again!!',230,100)
	  				time.sleep(0.5)
         			elif(life == 0) :
          				self.msg('Game Over', 230 , 100)
	  				pygame.display.flip()
	  				screen1.fill(black)
	  				self.create_bricks(random.randint(6,11),16)
	  				time.sleep(2)
	  				self.draw_rect()
	  				life = 4
					flag=1
	 			if self.ball.top >= 478:
	    				life-=1 
	    				pygame.display.flip()
			count=0	
			for brick in self.bricks:
				if brick.top > 0 :
					count=count+1
			if count == 0 and life != 0 and flag != 1:
         				self.msg('You Win',230 , 100)
         				pygame.display.flip()
         				screen1.fill(black)
	 				self.create_bricks(random.randint(6,11),16)
	 				time.sleep(2)
	 				self.draw_rect()
	 				life=4	     	   
      
      			pygame.display.flip()
     

brick().main()
