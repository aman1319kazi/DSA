def allConstruct(target, wordBank, memo):
	if target in memo:
		return memo[target]

	if not target:
		return [[]]

	result = []

	for word in wordBank:
		if target.startswith(word):
			new_target = target[len(word):]
			suffixWays = allConstruct(new_target, wordBank, memo)
			targetWays = [[word] + x for x in suffixWays]
			result.extend(targetWays)

	memo[target] = result
	return result

print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], {}))
print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'], {}))
print(allConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
print(allConstruct('aaaaaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'], {}))
