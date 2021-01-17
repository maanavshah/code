# O(nlogn) time | O(n) space
def mergeSort(array):
    if len(array) <= 1:
        return array
    subarray = array[:]
    mergeSortHelper(array, 0, len(array)-1)
    return array


def mergeSortHelper(array, l, r):
    if l == r:
        return
    m = (l + r) // 2
    mergeSortHelper(array, l, m)
    mergeSortHelper(array, m + 1, r)
    merge(array, l, m, r)


def merge(arr, l, m, r):
    subarray = arr[:]
    i = l
    j = m + 1
    k = l
    while i <= m and j <= r:
        if subarray[i] <= subarray[j]:
            arr[k] = subarray[i]
            i += 1
        else:
            arr[k] = subarray[j]
            j += 1
        k += 1
    while i <= m:
        arr[k] = subarray[i]
        i += 1
        k += 1
    while j <= r:
        arr[k] = subarray[j]
        j += 1
        k += 1
