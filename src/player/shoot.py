import pygame

def enter(player):
	player.vel.y = 0
	player.shoot_cooldown = 20

def update(player):
	player.shoot_cooldown -= 1
	if player.shoot_cooldown == 0:
		if player.vel.x == 0:
			player.set_state('stand')
		else:
			player.set_state('run')
		return
			
def exit(player):
	pass

def keydown(player, key):
	if   key == pygame.K_LEFT:
		if player.vel.x > 0:
			player.start_moving_left()
		player.start_moving_left()
	elif key == pygame.K_RIGHT:
		if player.vel.x < 0:
			player.start_moving_right()
		player.start_moving_right()
	elif key == pygame.K_LSHIFT:
		player.set_state('jump')

def keyup(player, key):
	if   key == pygame.K_LEFT:
		if player.moving['right']:
			player.start_moving_right()
		else:
			player.set_state('stand')
	elif key == pygame.K_RIGHT:
		if player.moving['left']:
			player.start_moving_left()
		else:
			player.set_state('stand')

def collide(player, entity, type, dir):
	if type == 'enemy':
		player.set_state('dead')
