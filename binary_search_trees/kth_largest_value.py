# O(n) time | O(n) space
def findKthLargestValueInBst(tree, k):
    return traversalHelper(tree, [])[k-1]

def traversalHelper(root, array):
    if root:
        traversalHelper(root.right, array)
        array.append(root.value)
        traversalHelper(root.left, array)
        return array
