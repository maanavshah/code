# O(n) time | O(n) space
def nodeDepths(root):
    depth = []
    root.depth = 0
    preorderTraversal(root, depth)
    return sum(depth)


def preorderTraversal(root, depth):
    depth.append(root.depth)
    if root.left:
        root.left.depth = root.depth + 1
        preorderTraversal(root.left, depth)
    if root.right:
        root.right.depth = root.depth + 1
        preorderTraversal(root.right, depth)
