import pygame

def enter(player):
	player.vel.x = 0
	if player.moving['up']:
		player.vel.y = 3
	elif player.moving['down']:
		player.vel.y = -3
	else:
		player.vel.y = 0
	player.acc.x = 0
	player.acc.y = 0

def update(player):
	pass

def exit(player):
	pass

def keydown(player, key):
	if key == pygame.K_UP:
		player.acc.y = 1
	elif key == pygame.K_DOWN:
		player.acc.y = -1
	elif key == pygame.K_LEFT:
		player.set_state('hang')
	elif key == pygame.K_RIGHT:
		player.set_state('hang')
	elif key == pygame.K_LSHIFT:
		player.set_state('jump')

def keyup(player, key):
	if key == pygame.K_UP:
		player.vel.y = 0
		player.acc.y = 0
	elif key == pygame.K_DOWN:
		player.vel.y = 0
		player.acc.y = 0
