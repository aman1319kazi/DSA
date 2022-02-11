def reverse_string(string):
	if not string:
		return string

	return reverse_string(string[1:]) + string[0]

print(reverse_string("hello"))