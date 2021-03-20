def longestPeak(array):
    i = 1
    maxPeak = 0
    while i < len(array) - 1:
        isPeak = array[i-1] < array[i] > array[i+1]

        if isPeak:
            leftIdx = i - 2
            while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
                leftIdx -= 1
            rightIdx = i + 2
            while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
                rightIdx += 1

            currPeak = rightIdx - leftIdx - 1
            maxPeak = max(currPeak, maxPeak)

            i = rightIdx
        else:
            i += 1
    return maxPeak
