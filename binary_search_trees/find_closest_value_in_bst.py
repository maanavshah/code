# O(log(n)) time | O(log(n)) space
def findClosestValue(tree, target, closestValue):
    if not tree:
        return closestValue
    if abs(tree.value - target) < minDiff:
        closestValue = tree.value
    if target < tree.value:
        return findClosestValue(tree.left, target, closestValue)
    else:
        return findClosestValue(tree.right, target, closestValue)
      
def findClosestValueInBst(tree, target):
    return findClosestValue(tree, target, abs(tree.value - target), tree.value)


# O(log(n)) time | O(1) space
def findClosestValueInBst(tree, target):
    closest = tree.value
    while tree:
        if abs(tree.value - target) < abs(closest - target):
            closest = tree.value
        if target < tree.value:
            tree = tree.left
        elif target > tree.value:
            tree = tree.right
        else:
           break
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
