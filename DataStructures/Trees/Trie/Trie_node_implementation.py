class node:
	def __init__(self, alphabet):
		self.alphabet = alphabet
		self.children = {}
		self.ends = False
		
class Trie:
	def __init__(self):
		self.root = node("*")

	def add_word(self, word):
		current_node = self.root
		for letter in word:
			if letter not in current_node.children:
				current_node.children[letter] = node(letter)
			current_node = current_node.children[letter]
		current_node.ends = True


	def search_word(self, word):
		current_node = self.root
		for letter in word:
			if letter not in current_node.children:
				return False
			current_node = current_node.children[letter]
		return current_node.ends

words = ["hello", "hell", "man", "aman"]
root = Trie()
for word in words:
	root.add_word(word)

print(root.search_word("hello"))