# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return None
        a = head
        b = head
        for i in range(k):
            if b == None: return head
            b = b.next
        newhead = self.reverse(a,b)
        a.next = self.reverseKGroup(b, k)
        return newhead


    def reverse(self, a, b):
        prev = ListNode(None)
        curr = a
        next = a
        while curr != b:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev