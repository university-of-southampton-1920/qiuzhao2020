# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#https://leetcode.com/problems/reverse-linked-list-ii/discuss/30709/Talk-is-cheap-show-me-the-code-(and-DRAWING)
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None: return head
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        for i in range(m-1):
            pre = pre.next
        start = pre.next
        then = start.next
        for i in range(n-m):
            start.next = then.next #a)
            then.next = pre.next # b)
            pre.next = then #c)
            then = start.next #d)
        return dummy.next
#         if not head or m == n: return head
#         p = dummy = ListNode(None)
#         dummy.next = head
#         for i in range(m-1): p = p.next
#         tail = p.next
#         for i in range(n-m):
#             tmp = p.next                  # a)
#             p.next = tail.next            # b)
#             tail.next = tail.next.next    # c)
#             p.next.next = tmp             # d)
#         return dummy.next