import pygame
from sprite import *
from vector import *

class Player:
	state = {
		'climb' : Sprite('player/climb.png' , 1),
		'crawl' : Sprite('player/crawl.png' , 1),
		'crouch': Sprite('player/crouch.png', 1),
		'dead'  : Sprite('player/dead.png'  , 1),
		'fall'  : Sprite('player/fall.png'  , 1),
		'hang'  : Sprite('player/hang.png'  , 1),
		'hurt'  : Sprite('player/hurt.png'  , 1),
		'jump'  : Sprite('player/jump.png'  , 1),
		'land'  : Sprite('player/land.png'  , 1),
		'lean'  : Sprite('player/lean.png'  , 1),
		'roll'  : Sprite('player/roll.png'  , 1),
		'run'   : Sprite('player/run.png'   , 1),
		'stand' : Sprite('player/stand.png' , 1),
		'turn'  : Sprite('player/turn.png'  , 1)
	}

	def __init__(self, x, y, scale):
		self.pos = Vector(x * scale.x, y * scale.y)
		self.vel = Vector(0, 0)
		self.min = Vector(75 * scale.x, 75 * scale.y)
		self.max = Vector(725 * scale.x, 425 * scale.y)
		self.state = Player.state['fall']
		size = self.state.get_size()
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
			'right': False
		}

	def update(self):
		if self.state == Player.state['stand']:
			pass
		elif self.state == Player.state['run']:
			# TODO account for dtime to fix ghosting
			self.pos.x += self.vel.x * self.scale.x
			self.pos.y -= self.vel.y * self.scale.x

			# TODO move to collide method
			left   = self.pos.x
			right  = left + self.size.x

			if left < self.min.x:
				self.state = Player.state['lean']
				self.pos.x = self.min.x
				self.vel.x = 0
			elif right >= self.max.x:
				self.state = Player.state['lean']
				self.pos.x = self.max.x - self.size.x
				self.vel.x = 0

		elif self.state == Player.state['fall']:
			self.pos.x += self.vel.x * self.scale.x
			self.pos.y -= self.vel.y * self.scale.x
			
			# TODO move to collide method
			top    = self.pos.y
			bottom = top + self.size.y

			if bottom >= self.max.y:
				if self.vel.x == 0:
					self.state = Player.state['stand']
				else:
					self.state = Player.state['run']
				self.pos.y = self.max.y - self.size.y
				self.vel.y = 0
			else:
				self.state = Player.state['fall']
				self.vel.y = -10
				if top < self.min.y:
					self.pos.y = self.min.y

		else:
			pass

	def render(self, screen):
		self.state.render(screen, self.pos.list())

	def start_running_left(self):
		print "run left"
		self.state = Player.state['run']
		self.moving['left'] = True
		self.vel.x = -6

	def start_running_right(self):
		print "run right"
		self.state = Player.state['run']
		self.moving['right'] = True
		self.vel.x = 6

	def stop_running(self):
		print "stop running"
		self.state = Player.state['stand']
		self.vel.x = 0

	def stop_running_left(self):
		self.moving['left'] = False
		if self.moving['right']:
			self.start_running_right()
		else:
			self.stop_running()

	def stop_running_right(self):
		self.moving['right'] = False
		if self.moving['left']:
			self.start_running_left()
		else:
			self.stop_running()

	def start_aiming_up(self):
		self.aiming['up'] = True;

	def start_aiming_left(self):
		self.aiming['left'] = True;

	def start_aiming_down(self):
		self.aiming['down'] = True;

	def start_aiming_right(self):
		self.aiming['right'] = True;

	def stop_aiming_up(self):
		self.aiming['up'] = False;

	def stop_aiming_left(self):
		self.aiming['left'] = False;

	def stop_aiming_down(self):
		self.aiming['down'] = False;

	def stop_aiming_right(self):
		self.aiming['right'] = False;
