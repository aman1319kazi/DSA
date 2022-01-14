class node:
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

class ll:
	def __init__(self):
		self.head = None


	def insert_at_beg(self, data):
		if not self.head:
			self.head = node(data)
			return

		temp = node(data, self.head)
		self.head = temp


	def insert_at_pos(self, pos, data):
		counter = 0
		temp = self.head
		if counter == pos:
			self.insert_at_beg(data)
			return

		while counter < pos - 1:
			counter += 1
			temp = temp.next

		t = node(data, temp.next)
		temp.next = t
		return


	def insert_at_end(self, data):
		if not self.head:
			self.insert_at_beg(data)
			return
		temp = self.head
		while temp.next:
			temp = temp.next

		temp.next = node(data)


	def traverse(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next

	def delete_at_beg(self):
		if not self.head:
			return
		self.head = self.head.next

	# def traverse(self, head):
	# 	if not head:
	# 		return
	# 	print(head.data)
	# 	self.traverse(head.next)

	def generate_ll(self, li):
		if not li: return ll()
		temp = ll()
		for x in li:
			temp.insert_at_end(x)

		return temp

linked = ll()
linked.insert_at_beg('e')
linked.insert_at_beg('d')
linked.insert_at_beg('c')
linked.insert_at_beg('a')
linked.traverse()
linked.insert_at_pos(1, 'b')
print()
linked.insert_at_end('f')
li = [1, 2, 3, 4, 5]
ans = linked.generate_ll(li)
ans.traverse()