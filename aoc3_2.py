import sys

def format_input(l):
	return list(map(lambda x: list(filter(lambda x: x.isdigit(), x.replace("\n", "").split(" "))), l))

inp = format_input(list(sys.stdin))

for item in inp:
	print(item)