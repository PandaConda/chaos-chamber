import pygame
from sprite import *
from vector import *

class Player:
	def __init__(self, x, y, scale):
		self.max_vel = Vector(8 * scale.x, 8 * scale.y)
		self.pos = Vector(x * scale.x, y * scale.y)
		self.vel = Vector(0, -10)
		self.acc = Vector(0, 0)
		self.min = Vector(75 * scale.x, 75 * scale.y)
		self.max = Vector(725 * scale.x, 425 * scale.y)
		self.state = Player.state['fall']
		self.state['enter'](self)
		print 'fall'
		size = self.state['sprite'].get_size()
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

	def set_state(self, name):
		state = Player.state[name]
		if state != self.state:
			print name
			self.state['exit'](self)
			self.state = state
			self.state['enter'](self)

	def update(self):
		self.state['update'](self)

		# TODO account for dtime to fix ghosting

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
		self.state['sprite'].render(screen, self.pos.list())


	# stand
	def enter_stand(self):
		# TODO move to collide method
		self.vel.x = 0
		self.vel.y = 0
		self.acc.x = 0
		self.acc.y = 0

	def update_stand(self):

		pass

	def exit_stand(self):
		pass

	# run
	def enter_run(self):
		self.vel.y = 0

	def update_run(self):
		# TODO move to collide method
		left   = self.pos.x
		right  = left + self.size.x

		if left < self.min.x:
			self.pos.x = self.min.x
			self.vel.x = 0
			self.acc.x = 0
			self.set_state('lean')
		elif right > self.max.x:
			self.pos.x = self.max.x - self.size.x 
			self.vel.x = 0
			self.acc.x = 0
			self.set_state('lean')

	def exit_run(self):
		pass

	# jump
	def enter_jump(self):
		self.vel.y = 10
		self.acc.y = -1
		self.airborne = True

	def update_jump(self):
		# TODO move to collide method
		top    = self.pos.y
		bottom = top + self.size.y

		if top < self.min.y:
			self.set_state('fall')
			self.pos.y = self.min.y
			self.vel.y = -3
			self.acc.y = -1
		elif self.vel.y < 0:
			self.set_state('fall')
	
	def exit_jump(self):
		pass

	# fall
	def enter_fall(self):
		self.airborne = True

	def update_fall(self):
		# TODO move to collide method
		top    = self.pos.y
		bottom = top + self.size.y

		if bottom >= self.max.y:
			self.airborne = False
			self.pos.y = self.max.y - self.size.y
			self.vel.y = 0
			self.acc.y = 0
			if self.moving['left'] or self.moving['right']:
				self.set_state('run')
			else:
				self.set_state('stand')

	def exit_fall(self):
		pass

	# TODO replace with single keyhandler
	def start_running_left(self):
		self.moving['left'] = True
		self.vel.x = -2
		self.acc.x = -1
		if not self.airborne:
			self.set_state('run')

	def start_running_right(self):
		self.moving['right'] = True
		self.vel.x = 2
		self.acc.x = 1
		if not self.airborne:
			self.set_state('run')

	def stop_running_left(self):
		self.moving['left'] = False
		if self.moving['right']:
			self.start_running_right()
		elif not self.airborne:
			self.set_state('stand')
		
	def stop_running_right(self):
		self.moving['right'] = False
		if self.moving['left']:
			self.start_running_left()
		elif not self.airborne:
			self.set_state('stand')

	def jump(self):
		if self.vel.y == 0:
			self.state = Player.state['jump']

	def land(self):
		self.vel.y = 0
		self.acc.y = 0

	def jump(self):
		self.set_state('jump')

	def start_moving(self, dir):
		self.move[dir] = True

	def stop_moving(self, dir):
		self.move[dir] = False

	def start_aiming(self, dir):
		self.aim[dir] = True;

	def stop_aiming(self, dir):
		self.aim[dir] = False

	def keydown(self, key):
		if   key == pygame.K_LEFT:
			self.start_running_left()
		elif key == pygame.K_RIGHT:
			self.start_running_right()
		elif key == pygame.K_LSHIFT:
			self.jump()

	def keyup(self, key):
		if   key == pygame.K_LEFT:
			self.stop_running_left()
		elif key == pygame.K_RIGHT:
			self.stop_running_right()

	state = {
		'climb' : {'enter': enter_stand, 'update': update_stand, 'exit' : exit_stand, 'sprite': Sprite('player/climb.png' , 1)},
		'crawl' : {'enter': enter_run  , 'update': update_run  , 'exit' : exit_run  , 'sprite': Sprite('player/crawl.png' , 1)},
		'crouch': {'enter': enter_stand, 'update': update_stand, 'exit' : exit_stand, 'sprite': Sprite('player/crouch.png', 1)},
		'dead'  : {'enter': enter_stand, 'update': update_stand, 'exit' : exit_stand, 'sprite': Sprite('player/dead.png'  , 1)},
		'fall'  : {'enter': enter_fall , 'update': update_fall , 'exit' : exit_fall , 'sprite': Sprite('player/fall.png'  , 1)},
		'hang'  : {'enter': enter_stand, 'update': update_stand, 'exit' : exit_stand, 'sprite': Sprite('player/hang.png'  , 1)},
		'hurt'  : {'enter': enter_stand, 'update': update_stand, 'exit' : exit_stand, 'sprite': Sprite('player/hurt.png'  , 1)},
		'jump'  : {'enter': enter_jump , 'update': update_jump , 'exit' : exit_jump , 'sprite': Sprite('player/jump.png'  , 1)},
		'land'  : {'enter': enter_stand, 'update': update_stand, 'exit' : exit_stand, 'sprite': Sprite('player/land.png'  , 1)},
		'lean'  : {'enter': enter_stand, 'update': update_stand, 'exit' : exit_stand, 'sprite': Sprite('player/lean.png'  , 1)},
		'roll'  : {'enter': enter_run  , 'update': update_run  , 'exit' : exit_run  , 'sprite': Sprite('player/roll.png'  , 1)},
		'run'   : {'enter': enter_run  , 'update': update_run  , 'exit' : exit_run  , 'sprite': Sprite('player/run.png'   , 1)},
		'stand' : {'enter': enter_stand, 'update': update_stand, 'exit' : exit_stand, 'sprite': Sprite('player/stand.png' , 1)},
		'turn'  : {'enter': enter_run  , 'update': update_run  , 'exit' : exit_run  , 'sprite': Sprite('player/turn.png'  , 1)}
	}
