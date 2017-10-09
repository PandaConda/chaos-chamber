import pygame

def enter(player):
	player.vel.y = 0

def update(player):
	# TODO move to collide method
	left   = player.pos.x
	right  = left + player.size.x

def exit(player):
	pass

def keydown(player, key):
	if   key == pygame.K_LEFT:
		if player.vel.x > 0:
			player.start_moving_left()
		player.start_moving_left()
	elif key == pygame.K_RIGHT:
		if player.vel.x < 0:
			player.start_moving_right()
		player.start_moving_right()
	elif key == pygame.K_LSHIFT:
		player.set_state('jump')
	elif key == pygame.K_SPACE:
		player.set_state('shoot')

def keyup(player, key):
	if   key == pygame.K_LEFT:
		if player.moving['right']:
			player.start_moving_right()
		else:
			player.set_state('stand')
	elif key == pygame.K_RIGHT:
		if player.moving['left']:
			player.start_moving_left()
		else:
			player.set_state('stand')

def collide(player, entity, type, dir):
	if type == 'tile':
		if dir == 'left':
			player.pos.x += 4
			player.vel.x = 0
			player.set_state('stand')
		elif dir == 'right':
			player.pos.x -= 4
			player.vel.x = 0
			player.set_state('stand')
		elif dir == 'bottom':
			player.pos.y -= 2
	elif type == 'enemy':
		player.set_state('dead')
