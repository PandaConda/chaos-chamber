import pygame
from vector import *

class Player:
	def __init__(self, x, y, scale):
		self.pos = Vector(x * scale.x, y * scale.y)
		self.vel = Vector(0, 0)
		self.min = Vector(75 * scale.x, 75 * scale.y)
		self.max = Vector(725 * scale.x, 425 * scale.y)
		self.sprite = pygame.image.load('data/img/player.png')
		size = self.sprite.get_size()
		self.size = Vector(size[0], size[1])
		self.scale = scale

	def update(self):
		self.pos.x += self.vel.x * self.scale.x
		self.pos.y -= self.vel.y * self.scale.x

		left   = self.pos.x
		right  = left + self.size.x
		top    = self.pos.y
		bottom = top + self.size.y

		if left < self.min.x:
			self.pos.x = self.min.x
			self.vel.x = 0
		elif right >= self.max.x:
			self.pos.x = self.max.x - self.size.x
			self.vel.x = 0

		if bottom >= self.max.y:
			self.pos.y = self.max.y - self.size.y
			self.vel.y = 0
		else:
			self.vel.y = -10
			if top < self.min.y:
				self.pos.y = self.min.y

	def render(self, screen):
		pygame.draw.rect(screen, (255, 0, 0), (self.min.x, self.min.y, self.max.x - self.min.x, self.max.y - self.min.y), 4)
		screen.blit(self.sprite, self.pos.list());

	def moveLeft(self):
		self.vel.x = -6

	def moveRight(self):
		self.vel.x = 6

	def stopMoving(self):
		self.vel.x = 0
