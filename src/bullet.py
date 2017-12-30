import color
import pygame
from entity import *
from sprite import *
from state import *
from vector import *

class Bullet(Entity):

	def __init__(self, parent):
		self.super = super(Bullet, self)
		super(Bullet, self).__init__()
		self.parent = parent
		self.pos = Vector(int(parent.pos.x), int(parent.pos.y))
		if parent.facing_right:
			self.xvel = 4
		else:
			self.xvel = -4
		self.radius = 5

	def update(self):
		self.pos.x += self.xvel

		# check collisions with AABBS for now
		# (works ok as long as bullet isn't too big)
		left   = self.pos.x - self.radius
		right  = self.pos.x + self.radius
		top    = self.pos.y - self.radius
		bottom = self.pos.y + self.radius

		for tile in self.parent.level.tiles:
			tile_left   = tile.pos.x - tile.size.x / 2
			tile_right  = tile.pos.x + tile.size.x / 2
			tile_top    = tile.pos.y - tile.size.y / 2
			tile_bottom = tile.pos.y + tile.size.y / 2

			l = left >= tile_left and left <= tile_right
			r = right >= tile_left and right <= tile_right
			t = top >= tile_top and top <= tile_bottom
			b = bottom >= tile_top and bottom <= tile_bottom
			
			if (l or r) and (t or b):
				self.parent.entities.remove(self)
				break


		for enemy in self.parent.level.enemies:
			enemy_size   = enemy.get_size()
			enemy_left   = enemy.pos.x - enemy_size.x / 2
			enemy_right  = enemy.pos.x + enemy_size.x / 2
			enemy_top    = enemy.pos.y - enemy_size.y / 2
			enemy_bottom = enemy.pos.y + enemy_size.y / 2

			l = left >= enemy_left and left <= enemy_right
			r = right >= enemy_left and right <= enemy_right
			t = top >= enemy_top and top <= enemy_bottom
			b = bottom >= enemy_top and bottom <= enemy_bottom
			
			if (l or r) and (t or b):
				enemy.set_state('dead')
				self.parent.entities.remove(self)
				break

	def render(self):
		pygame.draw.circle(self.parent.screen, color.BLACK, self.pos.list(), self.radius)
