def fibonacci(number, memo):
	if number in memo:
		return memo[number]

	if number < 2 and number > -1:
		memo[number] = number
		return number

	memo[number] =  fibonacci(number - 1, memo) + fibonacci(number - 2, memo)
	return memo[number]

print(fibonacci(5, {}))
print(fibonacci(10, {}))
print(fibonacci(15, {}))
print(fibonacci(20, {}))
print(fibonacci(30, {}))
print(fibonacci(40, {}))
