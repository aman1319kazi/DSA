n = int(input("Enter any positive integer: "))
def sum_odd_positive(num):
	return (num * ((2*num) + 1) * ((2*num) - 1)) // 3

print(sum_odd_positive(n//2))