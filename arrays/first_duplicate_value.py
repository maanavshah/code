# O(n) time | O(n) space
def firstDuplicateValue(array):
    seenElements = {}
    for idx, element in enumerate(array):
        if element in seenElements:
            return element
        else:
            seenElements[element] = idx
    return -1

# O(n) time | O(1) space
def firstDuplicateValue(array):
    for element in array:
        absValue = abs(element)
        if array[absValue - 1] < 0:
            return absValue
        else:
            array[absValue - 1] *= -1
    return -1
