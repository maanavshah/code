# # O(n) time | O(n) space
def longestSubstringWithoutDuplication(string):
    currentChars = {}
    currentSubstring = []
    longestSubstring = []
    maxLongest = 0
    i = 0
    while i < len(string):
        if string[i] in currentChars:
            if maxLongest < len(currentSubstring):
                maxLongest = len(currentSubstring)
                longestSubstring = currentSubstring
            index = currentChars[string[i]] + 1
            currentChars = {string[index]: index}
            currentSubstring = [string[index]]
            i = index
        else:
            currentChars[string[i]] = i
            currentSubstring.append(string[i])
        i += 1
    if maxLongest < len(currentSubstring):
        longestSubstring = currentSubstring
    return ''.join(longestSubstring)


def longestSubstringWithoutDuplication(string):
    startIdx = 0
    longest = [0, 1]
    lastSeen = dict()
    for idx, s in enumerate(string):
        if s in lastSeen:
            startIdx = max(startIdx, lastSeen[s] + 1)
        if longest[1] - longest[0] < idx + 1 - startIdx:
            longest[0] = startIdx
            longest[1] = idx + 1
        lastSeen[s] = idx
    return string[longest[0]: longest[1]]
