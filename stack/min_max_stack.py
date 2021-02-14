# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        self.maxStack = []

    # O(1) time | O(1) space
    def peek(self):
        return self.stack[-1]

    # O(1) time | O(1) space
    def pop(self):
        self.minStack.pop()
        self.maxStack.pop()
        return self.stack.pop()

    # O(1) time | O(1) space
    def push(self, number):
        if self.stack:
            self.minStack.append(min(self.minStack[-1], number))
            self.maxStack.append(max(self.maxStack[-1], number))
        else:
            self.minStack.append(number)
            self.maxStack.append(number)
        self.stack.append(number)

    # O(1) time | O(1) space
    def getMin(self):
        return self.minStack[-1]

    # O(1) time | O(1) space
    def getMax(self):
        return self.maxStack[-1]
