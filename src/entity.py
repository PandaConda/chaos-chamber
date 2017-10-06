import pygame

class Entity(object):
	def __init__(self):
		self.entities = []
		
	def tick(self, events):
		# pre
		for event in events:
			self.prehandle(event)
		self.preupdate()
		self.prerender()

		# children
		for entity in self.entities:
			entity.tick(events)

		# post
		for event in events:
			self.handle(event)
		self.update()
		self.render()

	def prehandle(self, event):
		if event.type == pygame.KEYDOWN:
			self.prekeydown(event.key)
		elif event.type == pygame.KEYUP:
			self.prekeyup(event.key)
		elif event.type == pygame.QUIT:
			self.prequit()

	def handle(self, event):
		if event.type == pygame.KEYDOWN:
			self.keydown(event.key)
		elif event.type == pygame.KEYUP:
			self.keyup(event.key)
		elif event.type == pygame.QUIT:
			self.quit()

	def prekeydown(self, event):
		pass

	def keydown(self, event):
		pass

	def prekeyup(self, event):
		pass

	def keyup(self, event):
		pass

	def prequit(self):
		pass

	def quit(self):
		pass

	def preupdate(self):
		pass

	def update(self):
		pass

	def prerender(self):
		pass

	def render(self):
		pass
