import pyxel
import block
import constants

class Tetris:

	def __init__(self):
		pyxel.init(120, 220, fps = 60)
		pyxel.image(0).load(0, 0, 'blocks_8x56.png')
		self.reset()
		pyxel.run(self.update, self.draw)
		
	def reset(self):
		self.state = 'resumed'
		self.frame_count_from_last_move = 0
		self.score = 0
		self.grid = []
		self.grid_tile_colors = []
		for row in range(22):
			self.grid.append([0] * 10)
			self.grid_tile_colors.append([-1] * 10)
		self.block = block.Block() #spawn some random block

	def update(self):
		if pyxel.btnp(pyxel.constants.KEY_Q):
			pyxel.quit()

		if pyxel.btnp(pyxel.constants.KEY_R):
			self.reset()
			return

		if pyxel.btnp(pyxel.constants.KEY_P):
			if self.state == 'resumed':
				self.state = 'paused'
			else:
				self.state = 'resumed'
		
		if self.state == 'paused':
			return

		move_direction = None
		rotate_direction = None
		if pyxel.btnp(pyxel.constants.KEY_LEFT, 12, 2):
			move_direction = constants.direction_L
		elif pyxel.btnp(pyxel.constants.KEY_RIGHT ,12, 2):
			move_direction = constants.direction_R
		elif pyxel.btnp(pyxel.constants.KEY_DOWN ,12, 2):
			move_direction = constants.direction_D
		elif pyxel.btnp(pyxel.constants.KEY_Z ,12, 20):
			rotate_direction = constants.direction_L
		elif pyxel.btnp(pyxel.constants.KEY_X ,12, 20):
			rotate_direction = constants.direction_R

		if  self.block.move_block(move_direction, self.grid):
			#if direction is down and move down was successful; reset the frames count from last move
			if move_direction == constants.direction_D:
				self.frame_count_from_last_move = 0

		self.block.rotate_block(rotate_direction, self.grid)

		#check if X numbers of frames have elapsed. Then move down if possible, else freeze the block (spawn new block) and reset the frame elapsed
		if (self.frame_count_from_last_move == 45):
			self.frame_count_from_last_move = 0
			if not(self.block.move_block(constants.direction_D, self.grid)):
				if self.is_game_over():
					self.reset()
					return
				self.freeze_block()
				self.clear_rows()
				self.block = block.Block()

		self.frame_count_from_last_move += 1

	def draw(self):
		self.draw_grid()
		pyxel.text(40, 190, "SCORE: ", 10)
		pyxel.text(70, 190, str(self.score), 12)
		pyxel.text(6, 200, "Q:quit", 8)
		pyxel.text(40, 200, "P:pause", 9)
		pyxel.text(76, 200, "R:restart", 11)

	def draw_grid(self):
		pyxel.cls(0)
		current_block_tiles = self.block.get_block_tiles(self.block.position, self.block.orientation)

		#draw block
		pyxel.rectb(20, 20, 101, 181, 3)
		for tile in current_block_tiles:
			if 2 <= tile[0] <= 21:
				pyxel.blt(tile[1] * 8 + 21, 21 + (tile[0] - 2) * 8, 0, self.block.shape * 8, 0, 8, 8, 0)
		
		#frozen grid
		for row in range(2, 22):
			for column in range(10):
				if self.grid[row][column] == 1:
					pyxel.blt(21 + column * 8, 21 + (row - 2) * 8, 0, self.grid_tile_colors[row][column] * 8, 0, 8, 8, 0)					

	def freeze_block(self):
		"""freezes the block to the grid"""
		for tile in self.block.get_block_tiles(self.block.position, self.block.orientation):
			self.grid[tile[0]][tile[1]] = 1
			self.grid_tile_colors[tile[0]][tile[1]] = self.block.shape

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
				self.grid_tile_colors[r] = [x for x in self.grid_tile_colors[r - 1]]

	def is_game_over(self):
		if self.block.position[0] == 0:
			return True
		return False

if __name__ == '__main__':
	Tetris()