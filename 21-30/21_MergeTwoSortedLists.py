class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    def readNode(l):
        nums = []
        while l != None:
            nums.append(l.val)
            l = l.next
        return nums

    nums = readNode(list1)
    nums.extend(readNode(list2))
    nums.sort()

    dummy_head = ListNode(0)
    current_node = dummy_head

    for i in nums:
        current_node.next = ListNode(i)
        current_node = current_node.next

    return dummy_head.next

"""链表"""
"""链表复习，自己看"""