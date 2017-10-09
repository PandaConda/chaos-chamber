import pygame

from entity import *
from vector import *

class Sprite(Entity):

	@staticmethod
	def set(screen, scale):
		Sprite.screen = screen
		Sprite.scale = scale

	def __init__(self, image, pos, num_frames = 1, anim_len = 60):
		super(Sprite, self).__init__()

		self.image = image
		self.pos = pos

		size = image.get_rect().size
		width = size[0] / num_frames
		height = size[1]
		self.size = Vector(width, height)

		self.num_frames = num_frames
		self.cur_frame = 0
		self.num_subframes = anim_len / num_frames
		self.cur_subframe = 0

		self.frames = []
		for i in xrange(num_frames):
			self.frames.append((self.size.x * i, 0, self.size.x, self.size.y))

	def get_size(self):
		return self.image.get_size()

	def render(self, flip = False):
		if flip:
			image = pygame.transform.flip(self.image, True, False)
			pos = (self.pos.x - (self.size.x / 2), self.pos.y - (self.size.y / 2))
			frame = self.frames[len(self.frames) - self.cur_frame - 1]
		else:
			image = self.image
			pos = (self.pos.x - (self.size.x / 2), self.pos.y - (self.size.y / 2))
			frame = self.frames[self.cur_frame]

		self.screen.blit(image, pos, frame)
		self.cur_subframe = (self.cur_subframe + 1) % self.num_subframes
		if self.cur_subframe == 0:
			self.cur_frame = (self.cur_frame + 1) % self.num_frames
