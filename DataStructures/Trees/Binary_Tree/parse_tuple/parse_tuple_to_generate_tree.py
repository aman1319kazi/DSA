class TreeNode:
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right

def parse_tuple(data):
	if isinstance(data, tuple) and len(data) == 3:
		node = TreeNode(data[1])
		node.left = parse_tuple(data[0])
		node.right = parse_tuple(data[2])

	elif data is None:
		node = None

	else:
		node = TreeNode(data)

	return node

tup = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
parse_tuple(tup)