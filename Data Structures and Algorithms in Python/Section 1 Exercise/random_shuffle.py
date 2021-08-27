import random
def shuffle(li):
	for x in range(len(li)):
		temp = random.randint(0, x)
		li[temp] , li[x] = li[x], li[temp]

li = [53,47,20,10]
shuffle(li)
print(li)