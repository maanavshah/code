# O(n) time | O(d) space
# d is depth of special arrays
def productSum(array, depth=1):
    total = 0
    for element in array:
        if isinstance(element, list):
            total += productSum(element, depth+1)
        else:
            total += element
    return depth * total
