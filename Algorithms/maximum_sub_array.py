# li = [13,-3,-25,20,-3,-16,-23,18      ,      20,-7,12,-5,-22,15,-4,7]
li = [100,200,-1000,100     ,    50,30,-60,10]
low = 0
high = 7

maxsum = 0
maxlist = 0

for x in range(len(li)):
	for y in range(x+1,len(li)): 
		if sum(li[x:y]) > maxsum: 
			maxsum = sum(li[x:y]) 
			maxlist = li[x:y] 
print(maxsum,maxlist)