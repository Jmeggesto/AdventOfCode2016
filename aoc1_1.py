import sys

inp = ""
instructions = []

coordinate = (0,0)

NORTH = 1
SOUTH = 2
EAST = 3
WEST = 4

current_direction = NORTH

def direction_to_string(direction):
		if direction is NORTH:
			return "NORTH"
		if direction is SOUTH:
			return "SOUTH"
		if direction is EAST:
			return "EAST"
		if direction is WEST:
			return "WEST"

def direction_for_turn(turn, direction):

	if turn == "R":
		if direction is NORTH:
			return EAST
		if direction is SOUTH:
			return WEST
		if direction is EAST:
			return SOUTH
		if direction is WEST:
			return NORTH
	elif turn == "L":
		if direction is NORTH:
			return WEST
		if direction is SOUTH:
			return EAST
		if direction is EAST:
			return NORTH
		if direction is WEST:
			return SOUTH

def translate_coordinate(coord, direction, value):
	if direction is NORTH:
		return (coord[0], coord[1]+value)
	if direction is SOUTH:
		return (coord[0], coord[1]-value)
	if direction is EAST:
		return (coord[0]+value, coord[1])
	if direction is WEST:
		return (coord[0]-value, coord[1])


def parse_instruction(instruction):
	global current_direction
	global coordinate
	global coord_set
	turn = instruction[0]
	value = int(instruction[1:])
	current_direction = direction_for_turn(turn, current_direction)
	coordinate = translate_coordinate(coordinate, current_direction, value)



for line in sys.stdin:
	inp += line.replace("\n", "").replace(" ", "")

instructions = inp.split(",")

answer = ()

for instruction in instructions:
	parse_instruction(instruction)

