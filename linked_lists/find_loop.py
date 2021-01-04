# O(n) time | O(1) space
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    slow = head.next
    fast = head.next.next
    while fast != slow:
        slow = slow.next
        fast = fast.next.next
    fast = head
    while fast != slow:
        slow = slow.next
        fast = fast.next
    return fast
