import pygame
from entity import *
from sprite import *
from state import *
from vector import *

# player state functions (in player/*)
import climb
import crawl
import crouch
import fall
import hang
import jump
import land
import roll
import run
import stand
import turn

class Player(Sprite):

	@staticmethod
	def loadStates():
		climb_image  = pygame.image.load('data/img/player/climb.png' )
		crawl_image  = pygame.image.load('data/img/player/crawl.png' )
		crouch_image = pygame.image.load('data/img/player/crouch.png')
		dead_image   = pygame.image.load('data/img/player/dead.png'  )
		fall_image   = pygame.image.load('data/img/player/fall.png'  )
		hang_image   = pygame.image.load('data/img/player/hang.png'  )
		hurt_image   = pygame.image.load('data/img/player/hurt.png'  )
		jump_image   = pygame.image.load('data/img/player/jump.png'  )
		land_image   = pygame.image.load('data/img/player/land.png'  )
		lean_image   = pygame.image.load('data/img/player/lean.png'  )
		roll_image   = pygame.image.load('data/img/player/roll.png'  )
		run_image    = pygame.image.load('data/img/player/run.png'   )
		stand_image  = pygame.image.load('data/img/player/stand.png' )
		turn_image   = pygame.image.load('data/img/player/turn.png'  )

		Player.states = {
			'climb' : State(climb , Sprite(climb_image , Vector(0, 0))),
			'crawl' : State(crawl , Sprite(crawl_image , Vector(0, 0))),
			'crouch': State(crouch, Sprite(crouch_image, Vector(0, 0))),
			'dead'  : State(stand , Sprite(dead_image  , Vector(0, 0))), # TODO
			'fall'  : State(fall  , Sprite(fall_image  , Vector(0, 0))),
			'hang'  : State(hang  , Sprite(hang_image  , Vector(0, 0))),
			'hurt'  : State(stand , Sprite(hurt_image  , Vector(0, 0))), # TODO
			'jump'  : State(jump  , Sprite(jump_image  , Vector(0, 0))),
			'land'  : State(land  , Sprite(land_image  , Vector(0, 0))),
			'lean'  : State(stand , Sprite(lean_image  , Vector(0, 0))), # TODO
			'roll'  : State(roll  , Sprite(roll_image  , Vector(0, 0))),
			'run'   : State(run   , Sprite(run_image   , Vector(0, 0))),
			'stand' : State(stand , Sprite(stand_image , Vector(0, 0))),
			'turn'  : State(turn  , Sprite(turn_image  , Vector(0, 0)))
		}

	def __init__(self, x, y, screen, scale):
		self.entities = []
		self.max_vel = Vector(8 * scale.x, 16 * scale.y)
		self.pos = Vector(x * scale.x, y * scale.y)
		self.spawn = self.pos
		self.vel = Vector(0, -10)
		self.acc = Vector(0, 0)
		self.min = Vector(75 * scale.x, 75 * scale.y)
		self.max = Vector(725 * scale.x, 425 * scale.y)
		for state in Player.states:
			Player.states[state].sprite.pos = self.pos
		self.state = Player.states['fall']
		self.state.enter(self)
		print '[player] fall'
		size = self.state.sprite.get_size()
		self.size = Vector(size[0], size[1])
		self.scale = scale
		self.aiming = {
			'up'   : False,
			'left' : False,
			'down' : False,
			'right': False
		}
		self.moving = {
			'up'   : False,
			'left' : False,
			'down' : False,
			'right': False,
			'jump' : False
		}

	def set_level(level):
		self.level = level

	def set_tiles(tiles):
		self.tiles = tiles

	def set_state(self, name):
		state = Player.states[name]
		if state != self.state:
			print '[player] ' + name
			self.state.exit(self)
			self.state = state
			self.state.enter(self)

	def update(self):
		# update x position
		self.pos.x += self.vel.x * self.scale.x
		self.state.pos = self.pos

		if self.vel.x < -self.max_vel.x:
			self.vel.x = -self.max_vel.x
			if self.acc.x < 0:
				self.acc.x = 0
		elif self.vel.x > self.max_vel.x:
			self.vel.x = self.max_vel.x
			if self.acc.x > 0:
				self.acc.x = 0
		else:
			self.vel.x += self.acc.x * self.scale.x

		# update y position
		self.pos.y -= self.vel.y * self.scale.y
		if self.vel.y < -self.max_vel.y:
			self.vel.y = -self.max_vel.y
			if self.acc.y < 0:
				self.acc.y = 0
		elif self.vel.y > self.max_vel.y:
			self.vel.y = self.max_vel.y
			if self.acc.y > 0:
				self.acc.y = 0
		else:
			self.vel.y += self.acc.y * self.scale.y

		self.state.update(self)

	def render(self):
		self.state.sprite.render()

	def start_moving_left(self):
		self.moving['left'] = True
		self.vel.x = -2
		self.acc.x = -1
		if not self.airborne:
			self.set_state('run')

	def start_moving_right(self):
		self.moving['right'] = True
		self.vel.x = 2
		self.acc.x = 1
		if not self.airborne:
			self.set_state('run')

	def stop_moving_left(self):
		self.moving['left'] = False
		if self.moving['right']:
			self.start_moving_right()
		elif not self.airborne:
			self.set_state('stand')
		
	def stop_moving_right(self):
		self.moving['right'] = False
		if self.moving['left']:
			self.start_moving_left()
		elif not self.airborne:
			self.set_state('stand')

	def start_moving(self, dir):
		self.move[dir] = True

	def stop_moving(self, dir):
		self.move[dir] = False

	def start_aiming(self, dir):
		self.aim[dir] = True;

	def stop_aiming(self, dir):
		self.aim[dir] = False

	def keydown(self, key):
		if key == pygame.K_LEFT:
			self.moving['left'] = True
		elif key == pygame.K_RIGHT:
			self.moving['right'] = True
		elif key == pygame.K_UP:
			self.moving['up'] = True
		elif key == pygame.K_DOWN:
			self.moving['down'] = True
		elif key == pygame.K_LSHIFT:
			self.moving['jump'] = True

		self.state.keydown(self, key)

	def keyup(self, key):
		if key == pygame.K_LEFT:
			self.moving['left'] = False
		elif key == pygame.K_RIGHT:
			self.moving['right'] = False
		elif key == pygame.K_UP:
			self.moving['up'] = False
		elif key == pygame.K_DOWN:
			self.moving['down'] = False
		elif key == pygame.K_LSHIFT:
			self.moving['jump'] = False

		self.state.keyup(self, key)
