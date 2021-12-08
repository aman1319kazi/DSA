def sum_of_digits(num):
	if num < 10:
		return num
	
	last_digit = num % 10
	remaining_number = num // 10
	return last_digit + sum_of_digits(remaining_number)

print(sum_of_digits(-1452))