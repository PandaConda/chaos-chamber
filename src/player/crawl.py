import pygame

def enter(player):
	if player.moving['left']:
		player.vel.x = -3
		player.acc.x = 0
	elif player.moving['right']:
		player.vel.x = 3
		player.acc.x = 0
	else:
		player.set_state('crouch')

def update(player):
	pass

def exit(player):
	pass

def keydown(player, key):
	if key == pygame.K_LSHIFT:
		player.set_state('jump')

def keyup(player, key):
	if key == pygame.K_LEFT:
		player.set_state('crouch')
	elif key == pygame.K_RIGHT:
		player.set_state('crouch')
	elif key == pygame.K_DOWN:
		if player.moving['left']:
			player.start_moving_left()
		elif player.moving['right']:
			player.start_moving_right()
		else:
			player.set_state('crouch')
