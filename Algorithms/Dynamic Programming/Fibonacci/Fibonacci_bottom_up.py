def fibonacci(number):
	dp = [0, 1]

	if number < 2:
		return dp[number]

	for x in range(2, number + 1):
		dp.append(dp[x - 1] + dp[x - 2])
	return dp[number]

print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(15))
print(fibonacci(20))
print(fibonacci(30))
print(fibonacci(40))