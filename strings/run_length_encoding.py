# O(n) time | O(n) space
def runLengthEncoding(string):
    encodedString = []
    currentRun = 1
    for i in range(1, len(string)):
        prevChar = string[i-1]
        currChar = string[i]
        if prevChar != currChar or currentRun == 9:
            encodedString.append(str(currentRun))
            encodedString.append(prevChar)
            currentRun = 0
        currentRun += 1

    encodedString.append(str(currentRun))
    encodedString.append(string[len(string)-1])
    return ''.join(encodedString)
