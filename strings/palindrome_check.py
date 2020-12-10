# O(n) time | O(n) space
def isPalindrome(string):
    return string == string[::-1]


# O(n) time | O(n) space
def isPalindrome(string, i=0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome(string, i+1)


# O(n) time | O(1) space
def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True


# O(n) time | O(1) space
def isPalindrome(string):
    n = len(string)
    for i in range(n // 2):
        if string[i] != string[n - i - 1]:
            return False
    return True
