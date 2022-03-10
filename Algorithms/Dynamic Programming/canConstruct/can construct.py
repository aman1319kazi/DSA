def canConstruct(target, wordBank): 
    if not target: 
        return True 
     
    for word in wordBank: 
        if target.startswith(word): 
            newtarget = target[len(word):] 
            if canConstruct(newtarget, wordBank): 
                return True 
    return False 
 
print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))#True
print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))#False
print(canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  #True
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) #False
