import sys


def triangle_possible(l):
	v1 = int(l[0])
	v2 = int(l[1])
	v3 = int(l[2])
	return v1 + v2 > v3 and v2 + v3 > v1 and v1 + v3 > v2

def possible_triangles(l):
	inp = map(lambda x: filter(lambda x: x.isdigit(), x.replace("\n", "").split(" ")), l)

	sorted_nums = list(map(lambda x: sorted(x), inp))

	possibles = list(
				filter(lambda x: triangle_possible(x), sorted_nums)
				)
	return len(possibles)

print(possible_triangles(list(sys.stdin)))