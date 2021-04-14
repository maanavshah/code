# O(n) time | O(n) space
def minHeightBst(array):
    return minHeightBstHelper(array, 0, len(array)-1, None)


def minHeightBstHelper(array, startIdx, endIdx, root):
    if endIdx < startIdx:
        return
    mid = (endIdx + startIdx) // 2
    if root:
        if array[mid] < root.value:
            root.left = BST(array[mid])
            root = root.left
        else:
            root.right = BST(array[mid])
            root = root.right
    else:
        root = BST(array[mid])
    minHeightBstHelper(array, startIdx, mid-1, root)
    minHeightBstHelper(array, mid+1, endIdx, root)
    return root

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
