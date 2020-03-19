# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        begin = ListNode(0)
        if head is None or head.next is None or k == 1:
            return head
        dummyhead = ListNode(0)
        dummyhead.next = head
        begin = dummyhead
        i = 0
        while head != None:
            i += 1
            if i % k == 0:
                begin = self.reverse(begin, head.next)
                head = begin.next
            else:
                head = head.next
        return dummyhead.next

    def reverse(self, begin, end):
        current = ListNode(0)
        current = begin.next
        nextNode = ListNode(0)
        first = ListNode(0)
        prev = ListNode(begin)
        first = current
        while current != end:
            nextNode = current.next
            current.next = prev
            prev = current
            current = next

        begin.next = prev
        first.next = current
        return first







