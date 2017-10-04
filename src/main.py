import os
from player import *
import pygame
from pygame.locals import *
from vector import *

gameover = False;

def run():
	global gameover

	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.display.init();
	info = pygame.display.Info()
	window_size = (info.current_w / 2, info.current_h / 2)
	tile_size = Vector(window_size[0] / 32, window_size[1] / 20)
	screen = pygame.display.set_mode(window_size, DOUBLEBUF)

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
				keydown(event.key)
				player.keydown(event.key)
			elif event.type == pygame.KEYUP:
				player.keyup(event.key)
			elif event.type == pygame.QUIT:
				gameover = True
		
		# update
		player.update()

		# render

		screen.blit(background, (0, 0));
		player.render(screen)
		pygame.display.flip()

def keydown(key):
	global gameover
	if key == pygame.K_f:
		pygame.display.toggle_fullscreen()
	elif key == pygame.K_ESCAPE:
		gameover = True
