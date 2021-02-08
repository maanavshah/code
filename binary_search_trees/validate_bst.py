# O(n) time | O(d) space
# d is depth(height) of tree
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBstHelper(tree, float('-inf'), float('inf'))


def validateBstHelper(tree, minValue, maxValue):
    if tree:
        if tree.value < minValue or tree.value >= maxValue:
            return False
        leftValid = validateBstHelper(tree.left, minValue, tree.value)
        rightValid = validateBstHelper(tree.right, tree.value, maxValue)
        return leftValid and rightValid
    return True
