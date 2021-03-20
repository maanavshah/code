# O(n) time | O(n) space
# Iterative solution 2
def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        if startRow == endRow or startCol == endCol:
            break

        for col in reversed(range(startCol, endCol)):
            result.append(array[endRow][col])

        for row in reversed(range(startRow + 1, endRow)):
            result.append(array[row][startCol])

        startRow += 1
        startCol += 1
        endRow -= 1
        endCol -= 1

    return result


# O(n) time | O(n) space
# Recursive solution
def spiralTraverse(array):
    result = []
    spiralTraverseHelper(array, 0, len(array) - 1, 0,
                         len(array[0]) - 1, result)
    return result


def spiralTraverseHelper(array, startRow, endRow, startCol, endCol, result):
    if startRow > endRow or startCol > endCol:
        return

    for col in range(startCol, endCol + 1):
        result.append(array[startRow][col])

    for row in range(startRow + 1, endRow + 1):
        result.append(array[row][endCol])

    if startRow == endRow or startCol == endCol:
        return

    for col in reversed(range(startCol, endCol)):
        result.append(array[endRow][col])

    for row in reversed(range(startRow + 1, endRow)):
        result.append(array[row][startCol])

    spiralTraverseHelper(array, startRow + 1, endRow - 1,
                         startCol + 1, endCol - 1, result)


# O(n) time | O(n) space
# Iterative solution 1
def spiralTraverse(array):
    result = []
    minRow, maxRow = 0, len(array) - 1
    min_col, max_col = 0, len(array[0]) - 1
    row, col = 0, 0

    while minRow <= maxRow and min_col <= max_col:

        while col <= max_col:
            result.append(array[row][col])
            col += 1
        minRow += 1
        row = minRow
        col = max_col

        while row <= maxRow:
            result.append(array[row][col])
            row += 1
        max_col -= 1
        col = max_col
        row = maxRow

        if not (minRow <= maxRow and min_col <= max_col):
            break

        while col >= min_col:
            result.append(array[row][col])
            col -= 1
        maxRow -= 1
        row = maxRow
        col = min_col

        while row >= minRow:
            result.append(array[row][col])
            row -= 1
        min_col += 1
        col = min_col
        row = minRow

    return result
