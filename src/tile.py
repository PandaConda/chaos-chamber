from move import *
from sprite import *

class Tile(Sprite):

	def __init__(self, sprite, pos, x_offset = 0, solid = True, moves = [], reverse = False):
		size = Vector(Sprite.screen.get_width() / 16, Sprite.screen.get_height() / 10)

		pos.x = pos.x * size.x + (size.x / 2)
		pos.y = pos.y * size.y + (size.y / 2)

		super(Tile, self).__init__(sprite, pos)

		self.solid = solid
		self.reverse = reverse
		self.reversing = False
		self.moving = len(moves) > 0

		if self.moving:
			self.moveframe = 0
			self.moves = []
			if self.reverse:
				self.moves.append(Move(pos.x, pos.y, 0))
				self.current_move = 1
			else:
				self.current_move = 0

			for move in moves:
				move.x = move.x * size.x + (size.x / 2)
				move.y = move.y * size.y + (size.y / 2)
				self.moves.append(move)

			dst = self.moves[self.current_move]
			self.dir = Vector((dst.x - self.pos.x) / dst.t, (dst.y - self.pos.y) / dst.t)


	def update(self):
		if self.moving:
			self.moveframe += 1
			self.pos.x += self.dir.x
			self.pos.y += self.dir.y
			if self.moveframe == self.moves[self.current_move].t:
				self.moveframe = 0
				if self.reversing and self.current_move > 0:
					self.current_move -= 1
				elif self.current_move < len(self.moves) - 1:
					self.current_move += 1
				if self.current_move == 0 and self.reversing:
					self.current_move = 1
					self.reversing = False
				elif self.current_move == len(self.moves) - 1:
					if self.reverse and not self.reversing:
						self.reversing = True
					else:
						self.moving = false
						return
					
				dst = self.moves[self.current_move]
				if self.reversing:
					dst_x = self.moves[self.current_move - 1].x
					dst_y = self.moves[self.current_move - 1].y
				else:
					dst_x = dst.x
					dst_y = dst.y
				self.dir = Vector((dst_x - self.pos.x) / dst.t, (dst_y - self.pos.y) / dst.t)
