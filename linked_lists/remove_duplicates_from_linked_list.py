# O(n) time | O(1) space
def removeDuplicatesFromLinkedList(linkedList):
    head = linkedList
    while linkedList:
        if linkedList.next and linkedList.value == linkedList.next.value:
            linkedList.next = linkedList.next.next
        else:
            linkedList = linkedList.next
    return head
