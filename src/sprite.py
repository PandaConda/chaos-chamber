import pygame

class Sprite:
	def __init__(self, name, num_frames):
		self.image = pygame.image.load('data/img/' + name)
		frame_width  = self.image.get_width() / num_frames
		frame_height = self.image.get_height()
		self.frame = []
		for i in xrange(num_frames):
			self.frame.append((frame_width * i, 0, frame_width * (i + 1), frame_height))
		self.num_frames = num_frames
		self.reset()

	def reset(self):
		self.cur_frame = 0

	def get_size(self):
		return self.image.get_size()

	def render(self, screen, pos):
		screen.blit(self.image, pos, self.frame[self.cur_frame])
		self.cur_frame = (self.cur_frame + 1) % self.num_frames
