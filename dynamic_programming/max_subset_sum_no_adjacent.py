# O(n) time | O(n) space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    maxSums = [array[0]]
    maxSums.append(max(array[0], array[1]))
    for i in range(2, len(array)):
        maxSums.append(max(maxSums[i-2] + array[i], maxSums[i-1]))
    return maxSums[-1]


# O(n) time | O(1) space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    first = array[0]
    second = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSum = max(second, first + array[i])
        first = second
        second = maxSum
    return second
