import pygame

import enemy_dead
import enemy_fall
import enemy_jump
import enemy_run_left
import enemy_run_right
import enemy_stand

from sprite import *
from state import *
from vector import *

class Enemy(Sprite):

	@staticmethod
	def loadStates():
		w = int(50 * Sprite.scale.x)
		h = int(50 * Sprite.scale.y)

		dead_animation = pygame.image.load('data/img/enemy/dead.png')
		dead_animation = pygame.transform.scale(dead_animation, (w * 16, h))

		jump_animation = pygame.image.load('data/img/enemy/jump.png')
		jump_animation = pygame.transform.scale(jump_animation, (w * 16, h))

		dead_sprite = Sprite(dead_animation, Vector(0, 0), 9)
		jump_sprite = Sprite(jump_animation, Vector(0, 0), 11)

		Enemy.states = {
			'dead'     : State(enemy_dead     , dead_sprite),
			'fall'     : State(enemy_fall     , jump_sprite), 
			'jump'     : State(enemy_jump     , jump_sprite),
			'run_left' : State(enemy_run_left , jump_sprite),
			'run_right': State(enemy_run_right, jump_sprite),
			'stand'    : State(enemy_stand    , jump_sprite),
		}

	def __init__(self, spawn):
		self.pos = spawn
		self.vel = Vector(0, 0)
		self.acc = Vector(0, 0)
		self.spawn = spawn
		self.state = self.states['run_left']
		for state in self.states:
			self.states[state].sprite.pos = self.pos
		self.state.enter(self)
		self.facing_right = False
		self.respawn()

	def set_level(self, level):
		self.level = level

	def get_size(self):
		size = self.state.sprite.get_size()
		w = size[0] / self.state.sprite.num_frames / 2
		h = size[1]
		return Vector(w, h)

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
		self.vel.y += self.acc.x

		self.state.pos = self.pos
		self.state.update(self)


	def render(self):
		self.state.sprite.render(self.facing_right)

	def collide(self, entity, type, dir):
		if type == 'bullet':
			self.set_state('dead')

	def respawn(self):
		self.pos = self.spawn
		self.set_state('run_left')
	
	def set_state(self, name):
		print "[enemy] " + name
		state = Enemy.states[name]
		if state != self.state:
			self.state.exit(self)
			self.state = state
			self.state.enter(self)
			state.sprite.cur_frame = 0
			state.sprite.cur_subframe = 0
