# O(log(n)) time | O(log(n)) space
def findTarget(array, target, low, high):
    if low > high:
        return -1
    mid = low + high // 2
    if array[mid] == target:
        return mid
    if target < array[mid]:
        return findTarget(array, target, low, mid-1)
    else:
        return findTarget(array, target, mid+1, high)


def binarySearch(array, target):
    return findTarget(array, target, 0, len(array)-1)


# O(log(n)) time | O(1) space
def binarySearch(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
