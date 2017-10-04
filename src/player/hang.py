import pygame

def enter(player):
	pass

def update(player):
	pass

def exit(player):
	pass

def keydown(player, key):
	if key == pygame.K_UP:
		player.set_state('climb')
	elif key == pygame.K_DOWN:
		player.set_state('climb')
	elif key == pygame.K_LSHIFT:
		if player.moving['left']:
			player.start_moving_left()
		elif player.moving['right']:
			player.start_moving_right()
		player.set_state('jump')

def keyup(player, key):
	if key == pygame.K_LEFT:
		player.set_state('climb')
	elif key == pygame.K_RIGHT:
		player.set_state('climb')
