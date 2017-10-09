from entity import *

class Level(Entity):
	@staticmethod
	def loadSprites(size):
		invisible = pygame.image.load('data/img/Level/Invisible.png')
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
			'invisible': invisible,
			'top': top,
			'bottom': bottom,
			'left': left,
			'right': right,
			'hole': hole
		}

	def __init__(self, spawn, goal, tiles, enemies):
		self.super = super(Level, self)
		super(Level, self).__init__()
		self.spawn = spawn
		self.goal = goal
		self.tiles = tiles
		self.enemies = enemies

	def update(self):
		for tile in self.tiles:
			tile.update()
		for enemy in self.enemies:
			enemy.update()

	def render(self):
		for tile in self.tiles:
			tile.render()
		for enemy in self.enemies:
			enemy.render()
