class BST:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def add_child(self, data):
		if self.data == data:
			return
		elif data<self.data:
			if self.left:
				self.left.add_child(data)
			else:
				self.left = BST(data)
		else:
			if self.right:
				self.right.add_child(data)
			else:
				self.right = BST(data)

	def print_tree(self, li=[]):
		li.append(self.data)

		if self.left:
			self.left.print_tree(li)
		if self.right:
			self.right.print_tree(li)
		return li


t = BST(17)
# t.add_child(2)
# t.add_child(3)
# t.add_child(4)
# t.add_child(5)
t.add_child(4)
t.add_child(1)
t.add_child(20)
t.add_child(9)
t.add_child(23)
t.add_child(18)
t.add_child(34)
print(t.print_tree())