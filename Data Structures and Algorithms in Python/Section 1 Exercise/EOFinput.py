li = []
while True:
	try:
		li.append(input())
	except EOFError:
		print(*list(reversed(li)), end="\n")
		break