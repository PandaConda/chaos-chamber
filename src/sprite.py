import pygame

from entity import *
from vector import *

class Sprite(Entity):

	@staticmethod
	def set(screen, scale):
		print "setting scale to " + str(scale.x) + ", " + str(scale.y)
		print
		Sprite.screen = screen
		Sprite.scale = scale

	def __init__(self, sheet, num_frames = 1, pos = None, start = Vector(0, 0), size = None, x_offset = None):
		super(Sprite, self).__init__()

		screensize = self.screen.get_size()
		screensize = Vector(screensize[0], screensize[1])

		self.sheet = sheet
		self.num_frames = num_frames
		self.cur_frame = 0

		start.x *= self.scale.x
		start.y *= self.scale.y

		if size == None:
			size = screensize
		self.size = size

		if pos == None:
			pos = Vector(screensize.x / 2 - self.size.x / 2, screensize.y / 2 - self.size.y / 2)
		self.pos = pos

		if x_offset == None:
			x_offset = self.size.x
		x_offset *= self.scale.x

		self.frames = []
		for i in xrange(num_frames):
			self.frames.append((start.x + x_offset * i, start.y, size.x, size.y))

	def get_size(self):
		return self.image.get_size()

	def render(self):
		self.screen.blit(self.sheet, (self.pos.x, self.pos.y), self.frames[self.cur_frame])
		#self.frame_tick = (self.frame_tick + 1) % self.ticks_per_frame
		#if self.frame_tick == 0:
		self.cur_frame = (self.cur_frame + 1) % self.num_frames
