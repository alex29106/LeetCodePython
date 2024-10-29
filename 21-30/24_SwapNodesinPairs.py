class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    if head.next == None:
        return head
    dummy_head = head.next
    thisnode = head
    while thisnode.next:
        nextnode = thisnode.next
        if nextnode.next.next:
            thisnode.next = nextnode.next.next
        elif nextnode.next:
            thisnode.next = nextnode.next
        else:
            thisnode.next = None
        temp = nextnode.next
        nextnode.next = thisnode
        if temp:
            thisnode = temp

    return dummy_head
