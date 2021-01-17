# O(log(n)) time | O(log(n)) space <- Average
# O(log(n)) time | O(n) space <- Worst
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)
        return self

    def contains(self, value):
        if value < self.value:
            if self.left:
                return self.left.contains(value)
            else:
                return False
        elif value > self.value:
            if self.right:
                return self.right.contains(value)
            else:
                return False
        else:
            return True

    def remove(self, value, prev=None):
        curr = self
        while curr:
            if value < curr.value:
                prev = curr
                curr = curr.left
            elif value > curr.value:
                prev = curr
                curr = curr.right
            else:
                if curr.left and curr.right:
                    curr.value = curr.right.getMinValue()
                    curr.right.remove(curr.value, curr)
                elif prev is None:
                    if curr.left:
                        curr.value = curr.left.value
                        curr.right = curr.left.right
                        curr.left = curr.left.left
                    elif curr.right:
                        curr.value = curr.right.value
                        curr.left = curr.right.left
                        curr.right = curr.right.right
                elif prev.left == curr:
                    prev.left = curr.left if curr.left else curr.right
                elif prev.right == curr:
                    prev.right = curr.left if curr.left else curr.right
                break
        return self

    def getMinValue(self):
        if self.left:
            return self.left.getMinValue()
        else:
            return self.value
