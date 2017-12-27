import pygame

def enter(player):
	player.vel.y = 15
	player.acc.y = -1
	player.airborne = True

def update(player):
	if player.vel.y < 0:
		player.set_state('fall')

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

def collide(player, entity, type, dir):
	if type == 'enemy':
		print 'player killed by enemy'
		player.set_state('dead')
