import pygame

def enter(player):
	player.vel.y = 10
	player.acc.y = -1
	player.airborne = True

def update(player):
	# TODO move to collide method
	left   = player.pos.x
	right  = left + player.size.x
	top    = player.pos.y
	bottom = top + player.size.y

	if top < player.min.y:
		player.set_state('fall')
		player.pos.y = player.min.y
		player.vel.y = -3
		player.acc.y = -1
	elif player.vel.y < 0:
		player.set_state('fall')
	elif left < player.min.x:
		player.pos.x = player.min.x
		player.vel.x = 0
		player.acc.x = 0
		player.set_state('climb')
	elif right > player.max.x:
		player.pos.x = player.max.x - player.size.x 
		player.vel.x = 0
		player.acc.x = 0
		player.set_state('climb')

def exit(player):
	pass

def keydown(player, key):
	if key == pygame.K_LEFT:
		if player.vel.x == 0:
			player.start_moving_left()
	elif key == pygame.K_RIGHT:
		if player.vel.x == 0:
			player.start_moving_right()

def keyup(player, key):
	pass
