# O(n) time | O(1) space
def moveElementToEnd(array, toMove):
    currIdx = 0
    moveIdx = 0
    while currIdx < len(array):
        if array[currIdx] != toMove:
            array[currIdx], array[moveIdx] = array[moveIdx], array[currIdx]
            moveIdx += 1
        currIdx += 1
    return array
