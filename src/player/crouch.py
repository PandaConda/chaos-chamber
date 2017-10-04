import pygame

def enter(player):
	player.vel.x = 0
	player.vel.y = 0
	player.acc.x = 0
	player.acc.y = 0

def update(player):
	pass

def exit(player):
	pass

def keydown(player, key):
	if key == pygame.K_LEFT:
		player.set_state('crawl')
	if key == pygame.K_RIGHT:
		player.set_state('crawl')
	elif key == pygame.K_LSHIFT:
		player.set_state('jump')

def keyup(player, key):
	if key == pygame.K_DOWN:
		player.set_state('stand')
