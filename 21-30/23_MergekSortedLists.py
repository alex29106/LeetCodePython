class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    def readNode(l):
        nums = []
        while l is not None:
            nums.append(l.val)
            l = l.next
        return nums

    nums = []
    for i in lists:
        temp = readNode(i)
        nums.extend(temp)
    nums.sort()
    dummy_head = ListNode(0)
    current_node = dummy_head

    for i in nums:
        current_node.next = ListNode(i)
        current_node = current_node.next

    return dummy_head.next


"""链表"""
"""没啥好说的，21改一改就是"""
