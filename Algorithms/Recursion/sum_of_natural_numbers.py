def sum_of_natural_numbers(num):
	if num == 0:
		return 0
	return sum_of_natural_numbers(num - 1) + num

print(sum_of_natural_numbers(10))