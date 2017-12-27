import pygame

def enter(player):
	if player.moving['jump']:
		player.set_state('jump')
	elif abs(player.vel.x) <= 1:
		player.set_state('stand')
	elif player.moving['left'] or player.moving['right']:
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

def collide(player, entity, type, dir):
	if type == 'tile':
		if dir == 'bottom':
			player.pos.x -= 1
	elif type == 'enemy':
		player.set_state('dead')
