import pygame

def enter(player):
	if player.moving['left'] or player.moving['right']:
		player.set_state('run')
	else:
		player.set_state('stand')

def update(player):
	pass

def exit(player):
	pass

def keydown(player, key):
	pass

def keyup(player, key):
	pass
