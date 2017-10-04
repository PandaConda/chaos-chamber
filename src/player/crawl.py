import pygame

def enter(player):
	pass

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
		player.set_state('run')
