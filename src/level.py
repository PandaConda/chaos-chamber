from entity import *

class Level(Entity):
	@staticmethod
	def loadSprites(size):
		top = pygame.image.load('data/img/Level/BottomAndTopTile.png')
		top = pygame.transform.scale(top, size)
		bottom = top
		left = pygame.image.load('data/img/Level/LeftSideTile.png')
		left = pygame.transform.scale(left, size)
		right = pygame.image.load('data/img/Level/RightSideTile.png')
		right = pygame.transform.scale(right, size)
		hole = pygame.image.load('data/img/Level/HoleInBackground.png')
		hole = pygame.transform.scale(hole, size)

		Level.tiles = {
			'top': top,
			'bottom': bottom,
			'left': left,
			'right': right,
			'hole': hole
		}

	def __init__(self, start, goal, tiles, enemies):
		self.super = super(Level, self)
		super(Level, self).__init__()
		self.start = start
		self.goal = goal
		self.tiles = tiles
		self.enemies = enemies

	def start(self, player):
		player.spawn = self.start

	def update(self):
		for tile in self.tiles:
			tile.update()
		for enemy in self.enemies:
			enemy.update()

	def render(self):
		for tile in self.tiles:
			tile.render()
		for enemy in self.enemies:
			enemy.update()
