# O(n) time | O(n) space
def branchSums(root):
    sums = []
    preorderTraversal(root, 0, sums)
    return sums

# Recursive
def preorderTraversal(root, runningSum, sums):
    if root:
        if root.left or root.right:
            preorderTraversal(root.left, runningSum + root.value, sums)
            preorderTraversal(root.right, runningSum + root.value, sums)
        else:
            sums.append(runningSum + root.value)


# O(n) time | O(1) space
# Iterative
def branchSums(root):
    stack = []
    sums = []
    root.currSum = 0
    stack.append(root)
    while stack:
        root = stack.pop()
        if root.left or root.right:
            if root.right :
                root.right.currSum = root.currSum + root.value
                stack.append(root.right)
            if root.left:
                root.left.currSum = root.currSum + root.value
                stack.append(root.left)
        else:
            sums.append(root.currSum + root.value)
    return sums
