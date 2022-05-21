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
		if self.left:
			self.left.print_tree(li)
		print(self.data)
		if self.right:
			self.right.print_tree(li)
		return li

	def search(self, val):
		if val==self.data:
			return True

		if val<self.data:
			if self.left:
				return self.left.search(val)
			else:
				return False

		if val>self.data:
			if self.right:
				return self.right.search(val)
			else:
				return False


	def min(self):
		minimum = self.data
		while self.left:
			# print(minimum)
			minimum = self.left.data
			self.left = self.left.left
		return minimum

	def minrecur(self):
		if not self.left:
			return self.data
		return self.left.minrecur()

	def max(self):
		maximum = self.data
		while self.right:
			# print(maximum)
			maximum = self.right.data
			self.right = self.right.right
		return maximum

	def maxrecur(self):
		if not self.right:
			return self.data
		return self.right.maxrecur

	def delete(self, value):
		if value<self.data:
			if self.left:
				self.left = self.left.delete(value)

		elif value>self.data:
			if self.right:
				self.right = self.right.delete(value)

		else:

			if self.left is None and self.right is None:
				return None

			if self.left is None:
				return self.right

			if self.right is None:
				return self.left

			minval = self.right.minrecur()
			self.data = minval
			self.right = self.right.delete(minval)

		return self


def build(elements):
	root = BST(elements[0])
	for x in range(1, len(elements)):
		root.add_child(elements[x])

	return root

tree = build([7, 8, 9, 10, 11, 12, 13])
print(tree.print_tree())
print(tree.min())
print(tree.max())