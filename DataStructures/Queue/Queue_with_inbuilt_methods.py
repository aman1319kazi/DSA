class Queue:
	def __init__(self, size):
		self.size = size
		self.elements = []

	def full(self):
		if len(self.elements) == self.size:
			return True
		return False

	def empty(self):
		if len(self.elements) == 0:
			return True
		return False

	def enqueue(self, data):
		if self.full():
			print("Queue is full")
			return
		self.elements.append(data)

	def dequeue(self):
		if self.empty():
			print("Queue is empty")
			return
		return self.elements.pop(0)

	def display(self):
		print(self.elements)
		return

	def __str__(self):
		self.display()
		return ""

queue = Queue(5)
queue.enqueue(5)
queue.enqueue(15)
a = queue.dequeue()
print(a)
queue.display()
print(queue)