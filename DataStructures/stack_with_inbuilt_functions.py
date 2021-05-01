class stack():
	def __init__(self, size):
		self.size = size
		self.arr = []

	def full(self):
		if len(self.arr) == self.size:
			return True
		return False 

	def empty(self):
		if len(self.arr) == 0:
			return True
		return False

	def push(self, data):
		if self.full():
			print("Stack is overflow")
		else:
			self.arr.append(data)

	def pop(self):
		if self.empty():
			print("Stack is underflow")
		else:
			popped = self.arr.pop()
			return popped

	def peek(self):
		if self.empty():
			print("Stack is underflow")
		else:
			print(self.arr[-1])

	def display(self):
		print(self.arr[::-1])

s = stack(5)
s.push(5)
s.push(10)
s.push(15)
s.display()
s.pop()
s.display()