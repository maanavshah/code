# O(logn) time | O(1) space
def shiftedBinarySearch(array, target):
    l = 0
    r = len(array) - 1
    while l <= r:
        mid = (l + r) // 2
        if array[mid] == target:
            return mid
        if array[l] <= array[mid]:
            # left half is sorted
            if array[l] <= target < array[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            # right half is sorted
            if array[mid] < target <= array[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1
