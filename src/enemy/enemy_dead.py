def enter(enemy):
	enemy.vel.x *= -0.5
	enemy.dead_cooldown = 60

def update(enemy):
	enemy.dead_cooldown -= 1
	if enemy.dead_cooldown == 0:
		enemy.respawn()
		enemy.set_state('run_left')

def exit(enemy):
	pass

def keydown():
	pass
	
def keyup():
	pass

def collide(self, entity, type, dir):
	pass
