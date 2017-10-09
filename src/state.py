class State:
	def __init__(self, state, sprite):
		self.enter = state.enter
		self.update = state.update
		self.exit = state.exit
		self.keydown = state.keydown
		self.keyup = state.keyup
		self.collide = state.collide
		self.sprite = sprite
