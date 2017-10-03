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
					player.start_running_left()
				elif event.key == K_RIGHT:
					player.start_running_right()
				elif event.key == K_f:
					pygame.display.toggle_fullscreen()
				elif event.key == K_w:
					player.start_aiming_up()
				elif event.key == K_a:
					player.start_aiming_left()
				elif event.key == K_s:
					player.start_aiming_down()
				elif event.key == K_d:
					player.start_aiming_right()
				elif event.key == K_ESCAPE:
					gameover = True
			elif event.type == pygame.KEYUP:
				if event.key == K_LEFT:
					player.stop_running_left()
				elif event.key == K_RIGHT:
					player.stop_running_right()
				elif event.key == K_w:
					player.stop_aiming_up()
				elif event.key == K_a:
					player.stop_aiming_left()
				elif event.key == K_s:
					player.stop_aiming_down()
				elif event.key == K_d:
					player.stop_aiming_right()
			elif event.type == pygame.QUIT:
				gameover = True
		
		# update
		player.update()

		# render

		screen.blit(background, (0, 0));
		player.render(screen)
		pygame.display.flip()
