class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    def readNode(l):
        nums = ''
        while l != None:
            nums += str(l.val)
            l = l.next
        return int(nums[::-1])

    s = str(readNode(l1) + readNode(l2))

    dummy_head = ListNode(0)
    current_node = dummy_head

    for char in s:  # Reverse the string to maintain the correct order
        current_node.next = ListNode(int(char))
        current_node = current_node.next

    return dummy_head.next


"""链表数据结构"""
"""如上，核心在于通过创建一个不参与后续运算的dummyhead,并在他的后面通过
   多次覆盖来展开链表，最后返回dummyhead的next来达到效果"""
