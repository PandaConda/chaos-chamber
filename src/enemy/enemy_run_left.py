def enter(enemy):
	enemy.facing_right = False
	enemy.vel.x = -1
	enemy.vel.y = 0
	enemy.acc.x = 0
	enemy.acc.y = 0

def update(enemy):
	pass

def exit(enemy):
	pass

def keydown():
	pass
	
def keyup():
	pass

def collide(self, entity, type, dir):
	if type == "tile" and dir == "left":
		self.set_state("run_right")
