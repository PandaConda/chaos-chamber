import pygame

def enter(player):
	player.vel.y = 0

def update(player):
	# TODO move to collide method
	left   = player.pos.x
	right  = left + player.size.x

	if left < player.min.x:
		player.pos.x = player.min.x
		player.vel.x = 0
		player.acc.x = 0
		player.set_state('lean')
	elif right > player.max.x:
		player.pos.x = player.max.x - player.size.x 
		player.vel.x = 0
		player.acc.x = 0
		player.set_state('lean')

def exit(player):
	pass

def keydown(player, key):
	if   key == pygame.K_LEFT:
		player.start_moving_left()
	elif key == pygame.K_RIGHT:
		player.start_moving_right()
	elif key == pygame.K_LSHIFT:
		player.set_state('jump')

def keyup(player, key):
	if   key == pygame.K_LEFT:
		player.stop_moving_left()
	elif key == pygame.K_RIGHT:
		player.stop_moving_right()