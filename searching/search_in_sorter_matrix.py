# O(m + n) time | O(1) space
# m is row and n is col
def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col > -1:
        if target == matrix[row][col]:
            return [row, col]
        if target > matrix[row][col]:
            row += 1
        else:
            col -= 1
    return [-1, -1]
