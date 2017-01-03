import sys

class BCodeGenerator(object):

	commands = ""
	keypad = [["1","4","7"],["2","5","8"],["3","6","9"]]

	keycode = ""
	current_key = ""
	current_position = (1,1)

	def __init__(self, commands):
		self.commands = commands
		for command in self.commands:
			self.parse_command(command)

	def move(self, direction):

		if direction == "U":
			if self.current_position[1] > 0:
				self.current_position = (self.current_position[0], self.current_position[1]-1)
		elif direction == "D":
			if self.current_position[1] < 2:
				self.current_position = (self.current_position[0], self.current_position[1]+1)
		elif direction == "L":
			if self.current_position[0] > 0:
				self.current_position = (self.current_position[0]-1, self.current_position[1])
		elif direction == "R":
			if self.current_position[0] < 2:
				self.current_position = (self.current_position[0]+1, self.current_position[1])

		self.current_key = self.keypad[self.current_position[0]][self.current_position[1]]

	def parse_command(self, command):
			if command == "\n":
				self.keycode += self.keypad[self.current_position[0]][self.current_position[1]]
				return 
			self.move(command)

inp = "".join(sys.stdin)
inp += "\n"

decoder = BCodeGenerator(inp)
print(decoder.keycode)
