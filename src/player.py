import pygame
from entity import *
from sprite import *
from state import *
from vector import *

# player state functions (in player/*)
import climb
import crouch
import dead
import fall
import jump
import land
import run
import shoot
import stand

class Player(Sprite):

	@staticmethod
	def loadStates():
		w = int(50 * Sprite.scale.x)
		h = int(100 * Sprite.scale.y)

		climb_animation = pygame.image.load('data/img/player/climb.png')
		climb_animation = pygame.transform.scale(climb_animation, (w * 8, h))

		crouch_animation = pygame.image.load('data/img/player/crouch.png')
		crouch_animation = pygame.transform.scale(crouch_animation, (w * 7, h))

		dead_animation = pygame.image.load('data/img/player/dead.png')
		dead_animation = pygame.transform.scale(dead_animation, (w * 16, h))

		fall_animation = pygame.image.load('data/img/player/fall.png')
		fall_animation = pygame.transform.scale(fall_animation, (w * 6, h))

		jump_animation = pygame.image.load('data/img/player/jump.png')
		jump_animation = pygame.transform.scale(jump_animation, (w * 16, h))

		land_animation = pygame.image.load('data/img/player/land.png')
		land_animation = pygame.transform.scale(land_animation, (w * 8, h))

		run_animation = pygame.image.load('data/img/player/run.png')
		run_animation = pygame.transform.scale(run_animation, (w * 16, h))

		shoot_animation = pygame.image.load('data/img/player/shoot.png')
		shoot_animation = pygame.transform.scale(shoot_animation, (w * 9, h))

		stand_animation = pygame.image.load('data/img/player/stand.png')
		stand_animation = pygame.transform.scale(stand_animation, (w * 5, h))

		Player.states = {
			'climb' : State(climb , Sprite(climb_animation , Vector(0, 0), 8)),
			'crouch': State(crouch, Sprite(crouch_animation, Vector(0, 0), 6)),
			'dead'  : State(dead  , Sprite(dead_animation  , Vector(0, 0), 10)),
			'fall'  : State(fall  , Sprite(fall_animation  , Vector(0, 0), 6)),
			'jump'  : State(jump  , Sprite(jump_animation  , Vector(0, 0), 10, 120)),
			'land'  : State(land  , Sprite(land_animation  , Vector(0, 0), 8)),
			'run'   : State(run   , Sprite(run_animation   , Vector(0, 0), 12)),
			'shoot' : State(shoot , Sprite(shoot_animation , Vector(0, 0), 8, 20)),
			'stand' : State(stand , Sprite(stand_animation , Vector(0, 0), 5)),
		}

	def __init__(self, pos, screen, scale):
		self.entities = []
		self.max_vel = Vector(8 * scale.x, 16 * scale.y)
		self.pos = Vector(pos.x * scale.x, pos.y * scale.y)
		self.spawn = self.pos
		self.vel = Vector(0, -10)
		self.acc = Vector(0, 0)
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

		self.facing_right = False

	def set_level(self, level):
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
			state.sprite.cur_frame = 0
			state.sprite.cur_subframe = 0

	def update(self):

		size = self.state.sprite.get_size()
		w = size[0] / self.state.sprite.num_frames / 2
		h = size[1] / 2

		left   = self.pos.x - w
		right  = self.pos.x + w
		top    = self.pos.y - h
		bottom = self.pos.y + h

		for tile in self.level.tiles:
			if tile.solid:
				tile_left   = tile.pos.x - tile.size.x / 2
				tile_right  = tile.pos.x + tile.size.x / 2
				tile_top    = tile.pos.y - tile.size.y / 2
				tile_bottom = tile.pos.y + tile.size.y / 2

				l = left >= tile_left and left <= tile_right
				r = right >= tile_left and right <= tile_right
				t = top >= tile_top and top <= tile_bottom
				b = bottom >= tile_top and bottom <= tile_bottom

				if t and l:
					if tile_right - left < tile_bottom - top:
						dir = 'left'
					else:
						dir = 'top'
					self.state.collide(self, tile, 'tile', dir)
					break
				elif t and r:
					if right - tile_left < tile_bottom - top:
						dir = 'right'
					else:
						dir = 'top'
					self.state.collide(self, tile, 'tile', dir)
					break
				elif b and l:
					if tile_right - left < bottom - tile_top:
						dir = 'left'
					else:
						dir = 'bottom'
					self.state.collide(self, tile, 'tile', dir)
					break
				elif b and r:
					if right - tile_left < bottom - tile_top:
						dir = 'right'
					else:
						dir = 'bottom'
					self.state.collide(self, tile, 'tile', dir)
					break

		self.pos.x += self.vel.x * self.scale.x
		self.pos.y -= self.vel.y * self.scale.y
		self.vel.x += self.acc.x
		self.vel.y += self.acc.y

		self.state.pos = self.pos
		self.state.update(self)

		if self.pos.x < 0 or self.pos.x > 800 * Sprite.scale.x or self.pos.y < 0 or self.pos.y > 500 * Sprite.scale.y:
			self.set_state('dead')

	def render(self):
		self.state.sprite.render(self.facing_right)

	def start_moving_left(self):
		self.facing_right = False
		self.moving['left'] = True
		self.vel.x = -5
		self.acc.x = 0
		if not self.airborne:
			self.set_state('run')

	def start_moving_right(self):
		self.facing_right = True 
		self.moving['right'] = True
		self.vel.x = 5
		self.acc.x = 0
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
