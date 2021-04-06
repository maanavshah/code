# O(n) time | O(1) space
def firstNonRepeatingCharacter(string):
    hashTable = {}
    for s in string:
        if s not in hashTable:
            hashTable[s] = 0
        hashTable[s] += 1
    for i, s in enumerate(string):
        if hashTable[s] == 1:
            return i
    return -1
