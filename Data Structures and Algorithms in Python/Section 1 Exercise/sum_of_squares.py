n = int(input("Enter any positive integer: "))
def sum_of_squares(num):
	return (n * (n+1) * ((2*n)+1)) // 6

print(sum_of_squares(10))