# O(n+m) time | O(n+m) space
def generateDocument(characters, document):
    charDict = {}
    for ch in characters:
        if ch not in charDict:
            charDict[ch] = 0
        charDict[ch] += 1
    for ch in document:
        if ch not in charDict or charDict[ch] == 0:
            return False
        charDict[ch] -= 1
    return True
