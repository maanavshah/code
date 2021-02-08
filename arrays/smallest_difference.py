# O(nlogn + mlogm)  time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    indexOne, indexTwo = 0, 0
    smallestPair = None
    minDiff = float('inf')
    while indexOne < len(arrayOne) and indexTwo < len(arrayTwo):
        firstNum = arrayOne[indexOne]
        secondNum = arrayTwo[indexTwo]
        if minDiff > abs(firstNum - secondNum):
            smallestPair = [firstNum, secondNum]
            minDiff = abs(firstNum - secondNum)
        if firstNum < secondNum:
            indexOne += 1
        else:
            indexTwo += 1
    return smallestPair
