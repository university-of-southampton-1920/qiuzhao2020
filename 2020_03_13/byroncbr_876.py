"""
Name: byroncbr_876.py
Author: bangrenc
Time: 13/3/2020 10:51 AM
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next: #判断fast下一个值或者下下个值，是否为null
            slow = slow.next #slow是一步一步的走
            fast = fast.next.next #fast是两步两步的走，相当于fast走到终点，slow才走到一半。

        return slow




