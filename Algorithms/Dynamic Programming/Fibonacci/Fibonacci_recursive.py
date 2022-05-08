def fibonacci(number):
	if number < 2:
		return number
	return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(15))
print(fibonacci(20))
print(fibonacci(30))
print(fibonacci(40))