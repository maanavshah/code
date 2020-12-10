# O(nlogn) time - sorting time | O(n) space
def twoNumberSum(array, targetSum):
    array.sort()
    leftIndex = 0
    rightIndex = len(array) - 1
    while leftIndex < rightIndex:
        currentSum = array[leftIndex] + array[rightIndex]
        if currentSum == targetSum:
            return[array[leftIndex], array[rightIndex]]
        elif currentSum < targetSum:
            leftIndex += 1
        else:
            rightIndex -= 1
    return []


# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    diffSum = dict()
    for num in array:
        if num in diffSum:
            return [num, diffSum[num]]
        diffSum[targetSum - num] = num
    return []
