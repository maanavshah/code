# O(n) time | O(d) space
# where d is depth(height) of binary tree
def invertBinaryTree(tree):
    if tree:
        tree.left, tree.right = tree.right, tree.left
        invertBinaryTree(tree.left)
        invertBinaryTree(tree.right)

# O(n) time | O(n) space
def invertBinaryTree(root):
    queue = [root]
    while queue:
        tree = queue.pop(0)
        if tree:
            tree.left, tree.right = tree.right, tree.left
            queue.append(tree.left)
            queue.append(tree.right)
    return root
