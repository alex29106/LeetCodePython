class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    def nodelength(list):
        length = 0
        while list != None:
            length += 1
            list = list.next
        return length
    nToRemove = nodelength(head) - n
    index = 0
    lis = head
    while True:
        if index == nToRemove-1:
            if n == 1:
                lis.next 
            lis.next = lis.next.next
            return head
        else:
            lis = lis.next
            index += 1
