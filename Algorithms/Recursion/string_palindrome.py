def palin(string):
	if len(string) < 2:
		return True

	if string[0] == string[-1]:
		return palin(string[1 : -1])
		
	return False

print(palin("nitin"))