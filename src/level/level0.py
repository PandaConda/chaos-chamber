from enemy import *
from level import *
from tile import *
from vector import *

class Level0(Level):
	def __init__(self):

		spawn = Vector(300, 300)

		goal = Vector(9, 5)

		tiles = [
			# top top
			Tile(Level.tiles['invisible'], Vector( 1, 0), True),
			Tile(Level.tiles['invisible'], Vector( 2, 0), True),
			Tile(Level.tiles['invisible'], Vector( 3, 0), True),
			Tile(Level.tiles['invisible'], Vector( 4, 0), True),
			Tile(Level.tiles['invisible'], Vector( 5, 0), True),
			Tile(Level.tiles['invisible'], Vector( 6, 0), True),
			Tile(Level.tiles['invisible'], Vector( 7, 0), True),
			Tile(Level.tiles['invisible'], Vector( 8, 0), True),
			Tile(Level.tiles['invisible'], Vector( 9, 0), True),
			Tile(Level.tiles['invisible'], Vector(10, 0), True),
			Tile(Level.tiles['invisible'], Vector(11, 0), True),
			Tile(Level.tiles['invisible'], Vector(12, 0), True),
			Tile(Level.tiles['invisible'], Vector(13, 0), True),
			Tile(Level.tiles['invisible'], Vector(14, 0), True),

			# top
			Tile(Level.tiles['top'], Vector( 1, 1), False),
			Tile(Level.tiles['top'], Vector( 2, 1), False),
			Tile(Level.tiles['top'], Vector( 3, 1), False),
			Tile(Level.tiles['top'], Vector( 4, 1), False),
			Tile(Level.tiles['top'], Vector( 5, 1), False),
			Tile(Level.tiles['top'], Vector( 6, 1), False),
			Tile(Level.tiles['top'], Vector( 7, 1), False),
			Tile(Level.tiles['top'], Vector( 8, 1), False),
			Tile(Level.tiles['top'], Vector( 9, 1), False),
			Tile(Level.tiles['top'], Vector(10, 1), False),
			Tile(Level.tiles['top'], Vector(11, 1), False),
			Tile(Level.tiles['top'], Vector(12, 1), False),
			Tile(Level.tiles['top'], Vector(13, 1), False),
			Tile(Level.tiles['top'], Vector(14, 1), False),

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

		enemies = [
			Enemy(Vector(500, 450)),
		]

		super(Level0, self).__init__(spawn, goal, tiles, enemies)
