# O(n) time | O(n) space
def arrayOfProducts(array):
    arrayProduct = []

    leftProduct = 1
    for idx in range(len(array)):
        arrayProduct.append(leftProduct)
        leftProduct *= array[idx]

    rightProduct = 1
    for idx in reversed(range(len(array))):
        arrayProduct[idx] *= rightProduct
        rightProduct *= array[idx]
    return arrayProduct

# O(n) time | O(n) space
def arrayOfProducts(array):
    zeroCount = 0
    product = 1
    for element in array:
        if element == 0:
            zeroCount += 1
        else:
            product *= element
    if zeroCount > 1:
        return [0 for _ in array]
    elif zeroCount == 1:
        for idx, element in enumerate(array):
            if element == 0:
                array[idx] = product
            else:
                array[idx] = 0
        return array
    else:
        for idx, element in enumerate(array):
            array[idx] = product / element
        return array
