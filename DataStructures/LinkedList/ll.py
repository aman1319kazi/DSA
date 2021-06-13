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

	#add node at last location
	def insert_at_end(self, data):
		if not self.head:
			self.insert_at_beginning(data)
			return

		temp = self.head
		while temp.next:
			temp = temp.next

		temp.next = node(data)

	#add node at any location
	def insert_at_index(self, index, data):
		if not self.head or index==0:
			self.insert_at_beginning(data)
			return

		if index < 0 :
			if -(index) <= self.get_length()+1:	
				index = self.get_length()-(-(index)) + 1 
			else:
				self.insert_at_beginning(data)
				return

		if index>=1 and index<=self.get_length():
			temp = self.head
			counter = 0
			while temp:
				if counter == index-1:
					Node = node(data, temp.next)
					temp.next = Node
					return
				counter+=1
				temp = temp.next

		else:
			self.insert_at_end(data)