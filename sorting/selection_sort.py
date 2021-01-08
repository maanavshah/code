# O(n^2) time | O(1) space  <-  worst, avg, best case
def selectionSort(array):
    for currIdx in range(len(array) - 1):
        smallestIdx = currIdx
        for i in range(currIdx + 1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
        swap(currIdx, smallestIdx, array)
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]