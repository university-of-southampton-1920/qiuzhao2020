# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        helper = ListNode(0)
        pre = helper
        current = head
        while current != None:
            pre = helper
            while pre.next != None and pre.next.val < current.val:
                pre = pre.next
            nextnode = current.next
            current.next = pre.next
            pre.next = current
            current = nextnode
        return helper.next