# # O(n^3) time | O(n) space
def longestPalindromicSubstring(string):
    currentLongestPalindrome = ''
    for i in range(len(string)):
        for j in range(len(string)):
            substring = string[i:j+1]
            if isPalindrome(substring) and len(currentLongestPalindrome) < len(substring):
                currentLongestPalindrome = substring
    return currentLongestPalindrome
def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string)-1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True

# # O(n^2) time | O(n) space
def longestPalindromicSubstring(string):
    maxLength = -1
    palindromicSubstring = None
    for i in range(len(string)):
        oddCount, oddLongest = getPalindromeCount(string, i, i)
        evenCount, evenLongest = getPalindromeCount(string, i, i+1)
        if oddCount > evenCount:
            if maxLength < oddCount:
                maxLength = oddCount
                palindromicSubstring = oddLongest
        else:
            if maxLength < evenCount:
                maxLength = evenCount
                palindromicSubstring = evenLongest
    return palindromicSubstring
def getPalindromeCount(string, leftIdx, rightIdx):
    count = -1
    while leftIdx > -1 and rightIdx < len(string) and string[leftIdx] == string[rightIdx]:
        count = rightIdx - leftIdx
        leftIdx -= 1
        rightIdx += 1
    return count, string[leftIdx+1: rightIdx]


# # O(n^2) time | O(n) space
def longestPalindromicSubstring(string):
    currentLongest = [0, 1]
    for i in range(len(string)-1):
        odd = checkPalindrome(string, i-1, i+1)
        even = checkPalindrome(string, i, i+1)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currentLongest = max(currentLongest, longest,key=lambda x: x[1] - x[0])
    return string[currentLongest[0]: currentLongest[1]]
def checkPalindrome(string, leftIdx, rightIdx):
    while leftIdx > -1 and rightIdx < len(string) and string[leftIdx] == string[rightIdx]:
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx+1, rightIdx]
