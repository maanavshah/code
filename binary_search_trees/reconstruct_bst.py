# O(n^2) time | O(n) space
def reconstructBst(array):
    if len(array) == 0:
        return None
    
    currValue = array[0]
    rightSubTreeIdx = len(array)

    for idx in range(1, len(array)):
        value = array[idx]
        if value >= currValue:
            rightSubTreeIdx = idx
            break
    
    leftSubTree = reconstructBst(array[1:rightSubTreeIdx])
    rightSubTree = reconstructBst(array[rightSubTreeIdx:])
    return BST(currValue, leftSubTree, rightSubTree)
