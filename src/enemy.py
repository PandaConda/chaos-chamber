import pygame

import enemy_dead
import enemy_fall
import enemy_jump
import enemy_run
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
			'dead' : State(enemy_dead , dead_sprite),
			'fall' : State(enemy_fall,  jump_sprite), 
			'jump' : State(enemy_jump , jump_sprite),
			'run'  : State(enemy_run  , jump_sprite),
			'stand': State(enemy_stand, jump_sprite),
		}

	def __init__(self, spawn):
		self.pos = spawn
		self.vel = Vector(0, 0)
		self.acc = Vector(0, 0)
		self.spawn = spawn
		self.state = self.states['stand']
		for state in self.states:
			self.states[state].sprite.pos = self.pos
		self.state.enter(self)
		self.facing_right = False
		self.respawn()

	def update(self):
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
		self.set_state('stand')
	
	def set_state(self, name):
		state = Enemy.states[name]
		if state != self.state:
			self.state.exit(self)
			self.state = state
			self.state.enter(self)
			state.sprite.cur_frame = 0
			state.sprite.cur_subframe = 0
