import pygame

from vector import *

def enter(player):
	player.vel.x = 0
	player.vel.y = 0
	player.acc.x = 0
	player.acc.y = 0
	player.dead_cooldown = 60

def update(player):
	player.dead_cooldown -= 1
	if player.dead_cooldown == 0:
		spawn = player.level.spawn
		player.pos.x = spawn.x
		player.pos.y = spawn.y
		player.vel.y = 0
		player.set_state('fall')
			
def exit(player):
	pass

def keydown(player, key):
	pass

def keyup(player, key):
	pass

def collide(player, entity, type, dir):
	pass
