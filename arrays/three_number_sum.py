def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for idx, element in enumerate(array):
        left = idx + 1
        right = len(array) - 1
        while left < right:
            currentSum = element + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([element, array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            else: 
                right -= 1
    return triplets
