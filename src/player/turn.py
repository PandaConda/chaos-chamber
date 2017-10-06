import pygame

def enter(player):
	if player.vel.x < 0:
		player.acc.x = 1
		player.set_state('run')
	elif player.vel.x > 0:
		player.acc.x = -1
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
