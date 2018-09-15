import constants
import random

class Block():
	"""Describe the shape with its current orientation and position on the grid"""
	
	def __init__(self, shape = None):
		self.orientation = 0
		if shape != None:
			self.shape = shape
		else:
			self.shape = random.randint(0, 6)
		self.position = (0, 3)

	def move_block(self, direction, grid):
		"""moves a block one step in a given direction"""
		if direction == None:
			return

		if direction == constants.direction_L:
			new_position = (self.position[0], self.position[1] - 1)
		elif direction == constants.direction_R:
			new_position = (self.position[0], self.position[1] + 1)
		elif direction == constants.direction_D:
			new_position = (self.position[0] + 1, self.position[1])

		if self.is_valid_block(self.get_block_tiles(new_position, self.orientation), grid):
			self.position = new_position
			return True

		return False

	
	def rotate_block(self, direction, grid):
		"""rotates a block in a given direction"""
		if direction == None:
			return
		new_orientation = (self.orientation + 1) % 4 if direction == constants.direction_R else (self.orientation - 1) % 4
		if self.is_valid_block(self.get_block_tiles(self.position, new_orientation), grid):
			self.orientation = new_orientation
			return True

		return False

	def is_valid_block(self, block_tiles, grid):
		""""returns true if all the tiles of the block are valid i.e. on the grid and doesn't occupy already filled tiles"""
		for tile in block_tiles:
			if not(0 <=tile[0] <= 21) or not(0 <=tile[1] <= 9) or grid[tile[0]][tile[1]] != 0:
				return False
		return True

	def get_block_tiles(self, position, orientation):
		block_name = constants.shape_dict[self.shape] + '_' + constants.orientation_dict[orientation]
		block_tiles = constants.block_dict[block_name]
		return {(tile[0] + position[0], tile[1] + position[1]) for tile in block_tiles}
