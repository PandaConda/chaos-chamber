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

	state = {
		'climb' : State(climb , Sprite('player/climb.png' , 1)),
		'crawl' : State(crawl , Sprite('player/crawl.png' , 1)),
		'crouch': State(crouch, Sprite('player/crouch.png', 1)),
		'dead'  : State(stand , Sprite('player/dead.png'  , 1)), # TODO
		'fall'  : State(fall  , Sprite('player/fall.png'  , 1)),
		'hang'  : State(hang  , Sprite('player/hang.png'  , 1)),
		'hurt'  : State(stand , Sprite('player/hurt.png'  , 1)), # TODO
		'jump'  : State(jump  , Sprite('player/jump.png'  , 1)),
		'land'  : State(land  , Sprite('player/land.png'  , 1)),
		'lean'  : State(stand , Sprite('player/lean.png'  , 1)), # TODO
		'roll'  : State(roll  , Sprite('player/roll.png'  , 1)),
		'run'   : State(run   , Sprite('player/run.png'   , 1)),
		'stand' : State(stand , Sprite('player/stand.png' , 1)),
		'turn'  : State(turn  , Sprite('player/turn.png'  , 1))
	}

	def __init__(self, x, y, screen, scale):
		self.max_vel = Vector(8 * scale.x, 16 * scale.y)
		self.pos = Vector(x * scale.x, y * scale.y)
		self.spawn = self.pos
		self.vel = Vector(0, -10)
		self.acc = Vector(0, 0)
		self.min = Vector(75 * scale.x, 75 * scale.y)
		self.max = Vector(725 * scale.x, 425 * scale.y)
		self.state = Player.state['fall']
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

	def set_state(self, name):
		state = Player.state[name]
		if state != self.state:
			print '[player] ' + name
			self.state.exit(self)
			self.state = state
			self.state.enter(self)

	def update(self):
		self.state.update(self)

		# TODO account for dtime to fix ghosting

		# update x position
		self.pos.x += self.vel.x * self.scale.x
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


	def render(self, screen):
		self.state.sprite.render(screen, self.pos.list())

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
