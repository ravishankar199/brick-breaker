#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys
def menu(screen, menu, x_pos = 100, y_pos = 100, font = None,
            size = 70, distance = 1.4, fgcolor = (255,255,255),
            cursorcolor = (255,0,0)):
	

	# Draw the Menupoints
	pygame.font.init()
	if font == None:
		myfont = pygame.font.Font(None, size)
	else:
		myfont = pygame.font.SysFont(font, size)
	cursorpos = 0
	for i in menu:
		text =  myfont.render(str(cursorpos + 1)+".  " + i,
				True, fgcolor)
		textrect = text.get_rect()
		textrect = textrect.move(x_pos, 
		           ((size // distance) * cursorpos) + y_pos)
		screen.blit(text, textrect)
		pygame.display.update(textrect)
		cursorpos += 1

	# Draw the ">", the Cursor
	cursorpos = 0
	cursor = myfont.render(">", True, cursorcolor)
	cursorrect = cursor.get_rect()
	cursorrect = cursorrect.move(x_pos - (size // distance),
	             (size // distance * cursorpos) + y_pos)
	exitMenu = False
	clock = pygame.time.Clock()
	filler = pygame.Surface.copy(screen)
	fillerrect = filler.get_rect()
	while True:
		clock.tick(30)
		screen.blit(filler, fillerrect)
		pygame.display.update(cursorrect)
		cursorrect = cursor.get_rect()
		cursorrect = cursorrect.move(x_pos - (size // distance),
			             (size // distance * cursorpos) + y_pos)
		screen.blit(cursor, cursorrect)
		pygame.display.update(cursorrect)
		if exitMenu == True:
			break
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					if cursorpos == 0:
						cursorpos = len(menu) - 1
					else:
						cursorpos -= 1
				elif event.key == pygame.K_DOWN:
					if cursorpos == len(menu) - 1:
						cursorpos = 0
					else:
						cursorpos += 1
				elif event.key == pygame.K_KP_ENTER or \
				     event.key == pygame.K_RETURN:
							exitMenu = True
	
	return cursorpos
