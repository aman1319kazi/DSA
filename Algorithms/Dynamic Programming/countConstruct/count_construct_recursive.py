def countConstruct(target, wordBank):
	if not target:
		return 1

	total = 0

	for word in wordBank:
		if target.startswith(word):
			new_target = target[len(word):]
			numWaysForRest = countConstruct(new_target, wordBank)
			total += numWaysForRest

	return total

print(countConstruct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd'])) # => 1
print(countConstruct("purple", ['purp', 'p', 'ur', 'le', 'purpl'])) # => 2
print(countConstruct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # => 0
print(countConstruct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # => 4
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) # => 0