# O(n^2) time | O(n^2) space - Average case
# O(n^3) time - Worst case
def fourNumberSum(array, targetSum):
    remainingPairSums = {}
    quadruplets = []
    for i in range(1, len(array) - 1):
        for j in range(i+1, len(array)):
            if array[i] + array[j] in remainingPairSums:
                for pair in remainingPairSums[array[i] + array[j]]:
                    quadruplets.append(pair + [array[i], array[j]])
        for j in range(0, i):
            currSum = targetSum - array[i] - array[j]
            if currSum not in remainingPairSums:
                remainingPairSums[currSum] = []
            remainingPairSums[currSum].append([array[i], array[j]])
    return quadruplets
