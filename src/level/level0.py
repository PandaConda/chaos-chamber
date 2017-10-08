from level import *
from tile import *
from vector import *

class Level0(Level):
	def __init__(self):

		start = Vector(5, 5)

		goal = Vector(9, 5)

		tiles = [
			# top
			Tile(Level.tiles['top'], Vector( 1, 1), True),
			Tile(Level.tiles['top'], Vector( 2, 1), True),
			Tile(Level.tiles['top'], Vector( 3, 1), True),
			Tile(Level.tiles['top'], Vector( 4, 1), True),
			Tile(Level.tiles['top'], Vector( 5, 1), True),
			Tile(Level.tiles['top'], Vector( 6, 1), True),
			Tile(Level.tiles['top'], Vector( 7, 1), True),
			Tile(Level.tiles['top'], Vector( 8, 1), True),
			Tile(Level.tiles['top'], Vector( 9, 1), True),
			Tile(Level.tiles['top'], Vector(10, 1), True),
			Tile(Level.tiles['top'], Vector(11, 1), True),
			Tile(Level.tiles['top'], Vector(12, 1), True),
			Tile(Level.tiles['top'], Vector(13, 1), True),
			Tile(Level.tiles['top'], Vector(14, 1), True),

			# bottom
			Tile(Level.tiles['bottom'], Vector( 1, 9), True),
			Tile(Level.tiles['bottom'], Vector( 2, 9), True),
			Tile(Level.tiles['bottom'], Vector( 3, 9), True),
			Tile(Level.tiles['bottom'], Vector( 4, 9), True),
			Tile(Level.tiles['bottom'], Vector( 5, 9), True),
			Tile(Level.tiles['bottom'], Vector( 6, 9), True),
			Tile(Level.tiles['bottom'], Vector( 7, 9), True),
			Tile(Level.tiles['bottom'], Vector( 8, 9), True),
			Tile(Level.tiles['bottom'], Vector( 9, 9), True),
			Tile(Level.tiles['bottom'], Vector(10, 9), True),
			Tile(Level.tiles['bottom'], Vector(11, 9), True),
			Tile(Level.tiles['bottom'], Vector(12, 9), True),
			Tile(Level.tiles['bottom'], Vector(13, 9), True),
			Tile(Level.tiles['bottom'], Vector(14, 9), True),

			# left 
			Tile(Level.tiles['left'], Vector(0, 1), True),
			Tile(Level.tiles['left'], Vector(0, 2), True),
			Tile(Level.tiles['left'], Vector(0, 3), True),
			Tile(Level.tiles['left'], Vector(0, 4), True),
			Tile(Level.tiles['left'], Vector(0, 5), True),
			Tile(Level.tiles['left'], Vector(0, 6), True),
			Tile(Level.tiles['left'], Vector(0, 7), True),
			Tile(Level.tiles['left'], Vector(0, 8), True),
			Tile(Level.tiles['left'], Vector(0, 9), True),

			# right
			Tile(Level.tiles['right'], Vector(15, 1), True),
			Tile(Level.tiles['right'], Vector(15, 2), True),
			Tile(Level.tiles['right'], Vector(15, 3), True),
			Tile(Level.tiles['right'], Vector(15, 4), True),
			Tile(Level.tiles['right'], Vector(15, 5), True),
			Tile(Level.tiles['right'], Vector(15, 6), True),
			Tile(Level.tiles['right'], Vector(15, 7), True),
			Tile(Level.tiles['right'], Vector(15, 8), True),
			Tile(Level.tiles['right'], Vector(15, 9), True),
		]

		enemies = []

		super(Level0, self).__init__(start, goal, tiles, enemies)
