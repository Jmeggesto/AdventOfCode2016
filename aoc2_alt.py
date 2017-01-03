import sys

"""
	keypad:

		1
	  2 3 4
	5 6 7 8 9
	  A B C
	    D
"""

# up(), down(), right(), and left() predictably 
# return the next state given an input. 
# next_char() just determines which function to use
# to return the state.

def up(char):

	if char == "3":
		return "1"
	elif char == "6":
		return "2"
	elif char == "7":
		return "3"
	elif char == "8":
		return "4"
	elif char == "A":
		return "6"
	elif char == "B":
		return "7"
	elif char == "C":
		return "8"
	elif char == "D":
		return "B"
	return char
def down(char):

	if char == "1":
		return "3"
	elif char == "2":
		return "6"
	elif char == "3":
		return "7"
	elif char == "4":
		return "8"
	elif char == "6":
		return "A"
	elif char == "7":
		return "B"
	elif char == "8":
		return "C"
	elif char == "B":
		return "D"
	return char
def left(char):
	if char == "3":
		return "2"
	elif char == "4":
		return "3"
	elif char == "6":
		return "5"
	elif char == "7":
		return "6"
	elif char == "8":
		return "7"
	elif char == "9":
		return "8"
	elif char == "B":
		return "A"
	elif char == "C":
		return "B"
	return char
def right(char):
	if char == "2":
		return "3"
	elif char == "3":
		return "4"
	elif char == "5":
		return "6"
	elif char == "6":
		return "7"
	elif char == "7":
		return "8"
	elif char == "8":
		return "9"
	elif char == "A":
		return "B"
	elif char == "B":
		return "C"
	return char
def next_char(char, d):
	if d == "U":
		return up(char)
	elif d == "D":
		return down(char)
	elif d == "L":
		return left(char)
	elif d == "R":
		return right(char)
	elif d == "\n":
		return char
# given a line of input and 
# an initial state, reduce 
# the list to determine the 
# state for each command in the line.
# I add the character to the beginning of 
# the list for simplicity's sake in reducing.
def eval_list(char, list):
	return reduce(next_char, char + list)

# evaluate one line given an initial state, then pass
# the result to the next line of commands,
# building the string as you go
def eval_lines(begin_char, lines, string = ""):
	if not lines:
		return string
	code = eval_list(begin_char, lines[0])
	return eval_lines(code, lines[1:], string+code)

inp = list(sys.stdin)
code = eval_lines("5", inp)
print(code)
