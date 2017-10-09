import pygame

def enter(player):
	player.airborne = True
	if player.vel.y == 0:
		print 'test'
		player.vel.y = -1
		player.acc.y = -1

def update(player):
	pass

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
	if type == 'tile':
		print 'tile collision: ' + dir
		if dir == 'bottom':
			player.airborne = False
			player.pos.x -= 2
			player.vel.y = 0
			player.acc.y = 0
			player.set_state('land')
		elif dir == 'left' or dir == 'right':
			player.vel.x = 0
			player.acc.x = 0
			player.set_state('climb')	
