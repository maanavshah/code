# O(n * w * log(w)) time | O(n + w) space
# n is the number of words and w is the length of longest words
def groupAnagrams(words):
    anagramGroups = {}
    for w in words:
        wSorted = ''.join(sorted(w))
        if wSorted not in anagramGroups:
            anagramGroups[wSorted] = []
        anagramGroups[wSorted].append(w)
    return list(anagramGroups.values())
