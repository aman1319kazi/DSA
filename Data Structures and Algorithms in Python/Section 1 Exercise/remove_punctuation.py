from string import punctuation
def remove_string(string):
	return "".join((x for x in string if x not in punctuation))

print(remove_string("Let's try, Mike."))
