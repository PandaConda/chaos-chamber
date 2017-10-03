class Tile:
	# TODO make set and map static class vars

	@staticmethod
	def load_set():
		return pygame.image.load("img/tileset.png")

	@staticmethod
	def load_map():
		return {
			'middle'     : Tile((  0, 0), (50, 50), 0, 1),
			'topleft'    : Tile(( 50, 0), (75, 75), 0, 1),
			'topright'   : Tile((125, 0), (75, 75), 0, 1),
			'bottomleft' : Tile((200, 0), (75, 75), 0, 1),
			'bottomright': Tile((275, 0), (75, 75), 0, 1),
			'top'        : Tile((350, 0), (50, 75), 0, 1),
			'bottom'     : Tile((425, 0), (50, 75), 0, 1),
			'left'       : Tile((500, 0), (75, 50), 0, 1),
			'right'      : Tile((550, 0), (75, 50), 0, 1)
		}

	def __init__(self, (pos), (size), start_frame, num_frames):
		self.size = size
		self.frame = start_frame % num_frames
		# TODO use map function or something similar to do in 1 loc
		self.frames = []
		for i in xrange(num_frames):
			self.frames.append((pos.x + size.x * i, pos.y, pos.x + size.x * (i + 1), pos.y + size.y))

	def render(self, screen, tileset, pos):
		screen.blit(tileset, pos, this.frames[frame])
		frame = (frame + 1) % self.num_frames
