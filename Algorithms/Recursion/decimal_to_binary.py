def dec_to_bin(num):
	if num == 0:
		return ''
	return dec_to_bin(num // 2) + str(num % 2)

print(dec_to_bin(8))

