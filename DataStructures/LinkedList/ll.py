class node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class linkedlist:
	def __init__(self):
		self.head = None

	#add node at first location
	def insert_at_beginning(self, data):
		self.head = node(data, self.head)

