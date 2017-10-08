import level
import os
import pygame

from color import *
from entity import *
from level0 import *
from move import *
from pygame.locals import *
from sprite import *
from tile import *
from vector import *

gameover = False
screen = None

class Game(Entity):
	def __init__(self, screen, scale):
		super(Game, self).__init__()
		self.screen = screen

		screensize = screen.get_size()

		# load sprites
		background = pygame.image.load('data/img/Level/LabBackground.png')
		background = pygame.transform.scale(background, screensize)

		self.levels = [
			Level0()
		]
		self.current_level = 0

		# entities
		self.entities.append(Sprite(background, Vector(screensize[0] / 2, screensize[1] / 2)))
		self.entities.append(self.levels[self.current_level])
		#self.entities.append(Player(300, 300))

	def keydown(self, key):
		if key == pygame.K_f:
			pygame.display.toggle_fullscreen()
		elif key == pygame.K_ESCAPE:
			global gameover
			gameover = True

	def quit(self):
		global gameover
		gameover = True

	def prerender(self):
		self.screen.fill(BLACK)

	def render(self):
		pygame.display.flip()


def run():
	global gameover

	# window
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.display.init();
	pygame.display.set_caption("Chaos Chamber")
	info = pygame.display.Info()
	window_size = (info.current_w / 2, info.current_h / 2)
	tile_size = Vector(window_size[0] / 32, window_size[1] / 20)
	screen = pygame.display.set_mode(window_size, DOUBLEBUF)
	scale = Vector(window_size[0] / 800.0, window_size[1] / 500.0)

	Sprite.set(screen, scale)
	Level.loadSprites((window_size[0] / 16 + 5, window_size[1] / 10))

	game = Game(screen, scale)
	clock = pygame.time.Clock()

	while not gameover:
		clock.tick(60)
		game.tick(pygame.event.get())
