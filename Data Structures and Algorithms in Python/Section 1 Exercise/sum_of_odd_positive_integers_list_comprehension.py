n = int(input("Enter any positive integer: "))

def sum_of_odd_positive_integers(num):
	return sum([x**2 for x in range(1,num,2)])