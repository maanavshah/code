# O(n) time | O(n) space
def reverseWordsInString(string):
    words = []
    startOfWord = 0
    for i in range(len(string)):
        char = string[i]

        if char == ' ':
            words.append(string[startOfWord:i])
            startOfWord = i
        elif string[startOfWord] == ' ':
            words.append(' ')
            startOfWord = i
    
    words.append(string[startOfWord:])

    reverseList(words)

    return ''.join(words)

def reverseList(list):
    start, end = 0, len(list) - 1
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1
