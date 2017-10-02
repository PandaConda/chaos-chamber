import os
from player import *
import pygame
from pygame.locals import *
from vector import *

def run():
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.display.init();
	info = pygame.display.Info()
	window_size = (info.current_w / 2, info.current_h / 2)
	tile_size = Vector(window_size[0] / 32, window_size[1] / 20)
	screen = pygame.display.set_mode(window_size, DOUBLEBUF)

	stage_left = 3 * tile_size.x
	stage_top = 3 * tile_size.y
	stage_width = 26 * tile_size.x
	stage_height = 14 * tile_size.y

	BLACK = (0, 0, 0)

	gameover = False;
	clock = pygame.time.Clock()

	background = pygame.image.load('data/img/background.png')
	scale = Vector(window_size[0] / 800.0, window_size[1] / 500.0)
	player = Player(300, 300, scale)
	background = pygame.transform.scale(background, window_size)

	while not gameover:
		clock.tick(30)

		# user input
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == K_LEFT:
					player.moveLeft()
				elif event.key == K_RIGHT:
					player.moveRight()
				elif event.key == K_f:
					pygame.display.toggle_fullscreen()
				elif event.key == K_ESCAPE:
					gameover = True
			elif event.type == pygame.KEYUP:
				if event.key == K_LEFT:
					player.stopMoving()
				elif event.key == K_RIGHT:
					player.stopMoving()
		
		# update
		player.update()

		# render

		screen.blit(background, (0, 0));
		player.render(screen)
#pygame.draw.rect(screen, (255, 0, 0), (75 * scale.x, 75 * scale.y, 725 * scale.x, 425 * scale.y), 4)
#pygame.draw.rect(screen, (255, 0, 0), (stage_left, stage_top, stage_width, stage_height), 4)
		pygame.display.flip()
