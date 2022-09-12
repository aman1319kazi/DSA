class Node:
	def __init__(self, data):
		self.data = data
		self.childrens = []
		self.parent = None

	def add_children(self, child):
		child.parent = self
		self.childrens.append(child)

	def get_level(self):
		p = self.parent
		level = 0
		while p:
			level+=1
			p=p.parent
		return level


	def display_tree(self):
		spaces = ' ' * self.get_level() * 3
		print(spaces + self.data)
		if self.childrens:
			for child in self.childrens:
				child.display_tree()


root = Node("C")
program = Node("program-files")
root.add_children(program)
old = Node("old windows")
root.add_children(old)
windows32  = Node("system32")
cmd = Node("cmd")
windows32.add_children(cmd)
program.add_children(windows32)
root.display_tree()
