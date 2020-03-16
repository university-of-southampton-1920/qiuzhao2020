"""
Name: byroncbr_24.py
Author: bangrenc
Time: 16/3/2020 10:13 AM
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = p = ListNode(0)
        dummy.next = head
        while p.next and p.next.next:
            node1 = p.next
            node2 = p.next.next
            next_n = node2.next

            node1.next = next_n
            node2.next = node1
            p.next = node2

            p = node1

        return dummy.next

