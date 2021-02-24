# O(n) time | O(1) space
def breadthFirstSearch(self, array):
    q = [self]
    while len(q) > 0:
        node = q.pop(0)
        array.append(node.name)
        for child in node.children:
            q.append(child)
    return array
