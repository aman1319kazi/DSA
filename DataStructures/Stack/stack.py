class Stack:
	def __init__(self, size):
		self.size = size
		self.elements = [None] * self.size
		self.top = -1

	def full(self):
		if self.top == self.size-1:
			return True
		return False

	def empty(self):
		if self.top == -1:
			return True
		return False

	def push(self, data):
		if self.full():
			print("Stack is overflow")
		else:
			self.top+=1
			self.elements[self.top] = data

	def pop(self):
		if self.empty():
			print("Stack is underflow")
		else:
			p = self.elements[self.top] 
			self.top -= 1
			return p

	def peek(self):
		if self.empty():
			print("Stack is underflow")
			return 
		return self.elements[self.top]

	def display(self):
		if self.empty():
			print("Stack is underflow")
			return
		print(self.elements[self.top::-1])
		return


s = Stack(5)
s.push(5)
s.push(10)
s.push(15)
s.display()
s.pop()
s.display()
