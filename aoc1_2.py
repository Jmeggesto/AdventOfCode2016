import sys

NORTH = 1
SOUTH = 2
EAST = 3
WEST = 4

def direction_to_string(direction):
		if direction is NORTH:
			return "NORTH"
		if direction is SOUTH:
			return "SOUTH"
		if direction is EAST:
			return "EAST"
		if direction is WEST:
			return "WEST"

class EBHQFinder(object):

	instructions = []

	current_direction = 0
	position = (0,0)
	visited = []

	def __init__(self, inst):
		self.instructions = inst
		self.current_direction = NORTH

	def change_direction(self, turn):
		if turn == "R":
			if self.current_direction is NORTH:
				self.current_direction = EAST
			elif self.current_direction is SOUTH:
				self.current_direction = WEST
			elif self.current_direction is EAST:
				self.current_direction = SOUTH
			elif self.current_direction is WEST:
				self.current_direction = NORTH
		elif turn == "L":
			if self.current_direction is NORTH:
				self.current_direction = WEST
			elif self.current_direction is SOUTH:
				self.current_direction = EAST
			elif self.current_direction is EAST:
				self.current_direction = NORTH
			elif self.current_direction is WEST:
				self.current_direction = SOUTH

	def visit(self, coord):
		if coord in self.visited:
			return coord
		else:
			self.visited.append(coord)

	def move(self, value):
		for i in range(0, value):
			if self.current_direction is NORTH:
				self.position = (self.position[0], self.position[1]+1)
			if self.current_direction is SOUTH:
				self.position = (self.position[0], self.position[1]-1)
			if self.current_direction is EAST:
				self.position = (self.position[0]+1, self.position[1])
			if self.current_direction is WEST:
				self.position = (self.position[0]-1, self.position[1])
			hq_location = self.visit(self.position)
			if hq_location:
				return hq_location

	def parse_instruction(self, instruction):
		turn = instruction[0]
		value = int(instruction[1:])
		self.change_direction(turn)
		return self.move(value)

	def find_hq(self):
		for instruction in self.instructions:
			location = self.parse_instruction(instruction)
			if location:
				return location


inp = ""
for line in sys.stdin:
	inp += line.replace("\n", "").replace(" ", "")

instructions = inp.split(",")

finder = EBHQFinder(instructions)
print(finder.find_hq())
