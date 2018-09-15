import pyxel
import block
import constants

class App:

	def __init__(self):
		pyxel.init(120, 220, fps = 60)
		pyxel.image(0).load(0, 0, 'block.png')
		self.reset()
		pyxel.run(self.update, self.draw)
		
	def reset(self):
		self.frame_count_on_last_move = pyxel.frame_count
		self.score = 0
		self.grid = []
		for row in range(22):
			self.grid.append([0] * 10)
		self.block = block.Block() #spawn some random block

	def update(self):
		if pyxel.btnp(pyxel.constants.KEY_Q):
			pyxel.quit()

		if pyxel.btnp(pyxel.constants.KEY_R):
			self.reset()
			return

		move_direction = None
		rotate_direction = None
		if pyxel.btnp(pyxel.constants.KEY_LEFT, 20, 10):
			move_direction = constants.direction_L
		elif pyxel.btnp(pyxel.constants.KEY_RIGHT ,20, 10):
			move_direction = constants.direction_R
		elif pyxel.btnp(pyxel.constants.KEY_DOWN ,20, 1):
			move_direction = constants.direction_D
		# elif pyxel.btn(pyxel.constants.KEY_UP):
		# 	move_direction = constants.direction_D
		elif pyxel.btnp(pyxel.constants.KEY_Z ,20, 20):
			rotate_direction = constants.direction_L
		elif pyxel.btnp(pyxel.constants.KEY_X ,20, 20):
			rotate_direction = constants.direction_R

		if  self.block.move_block(move_direction, self.grid):
			#if direction is down and move down was successful; reset the frames count on last move
			if move_direction == constants.direction_D:
				self.frame_count_on_last_move = pyxel.frame_count

		self.block.rotate_block(rotate_direction, self.grid)

		#check if X numbers of frames have elapsed. Then move down if possible, else freeze the block (spawn new block) and reset the frame elapsed
		if (pyxel.frame_count - self.frame_count_on_last_move == 45):
			if not(self.block.move_block(constants.direction_D, self.grid)):
				if self.is_game_over():
					self.reset()
					return
				self.freeze_block()
				self.clear_rows()
				self.block = block.Block()
			self.frame_count_on_last_move = pyxel.frame_count

	def draw(self):
		self.draw_grid()
		pyxel.text(40, 190, "SCORE: ", 10)
		pyxel.text(70, 190, str(self.score), 12)
		pyxel.text(22, 200, "Q: quit", 8)
		pyxel.text(62, 200, "R: restart", 11)

	def draw_grid(self):
		pyxel.cls(0)
		current_block_tiles = self.block.get_block_tiles(self.block.position, self.block.orientation)

		pyxel.rectb(20, 20, 101, 181, 4)
		for tile in current_block_tiles:
			if 2 <= tile[0] <= 21:
				pyxel.blt(tile[1] * 8 + 21, 173 - (21 - tile[0]) * 8, 0, 0, 0, 8, 8)
		
		for row in range(2, 22):
			for column in range(10):
				if self.grid[row][column] == 1:
					pyxel.blt(21 + column * 8, 21 + (row - 2) * 8, 0, 0, 0, 8, 8)					

	def freeze_block(self):
		"""freezes the block to the grid"""
		for tile in self.block.get_block_tiles(self.block.position, self.block.orientation):
			self.grid[tile[0]][tile[1]] = 1

	def clear_rows(self):
		rows_to_clear = []
		for row in range(2,22):
			if sum(self.grid[row]) == 10:
				rows_to_clear.append(row)
		if len(rows_to_clear) < 4:
			self.score += (100 * len(rows_to_clear))
		else:
			self.score += 800
		for row in rows_to_clear:
			for r in range(row, 1, -1):
				self.grid[r] = [x for x in self.grid[r - 1]]

	def is_game_over(self):
		if self.block.position[0] == 0:
			return True
		return False

if __name__ == '__main__':
	App()