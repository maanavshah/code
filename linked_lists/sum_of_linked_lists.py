# O(n) time | O(n) space
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def sumOfLinkedLists(linkedListOne, linkedListTwo):
    head = LinkedList(0)
    curr = head
    carry = 0
    while linkedListOne or linkedListTwo or carry != 0:
        if linkedListOne:
            carry += linkedListOne.value
            linkedListOne = linkedListOne.next
        if linkedListTwo:
            carry += linkedListTwo.value
            linkedListTwo = linkedListTwo.next
        node = LinkedList(carry % 10)
        curr.next = node
        curr = curr.next
        carry = carry // 10
    return head.next
