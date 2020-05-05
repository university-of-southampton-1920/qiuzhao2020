# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = point = ListNode(0)
        values = []
        while l1:
            values.append(l1.val)
            l1 = l1.next
        while l2:
            values.append(l2.val)
            l2 = l2.next
        for l in sorted(values):
            point.next = ListNode(l)
            point = point.next
        return head.next
		
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = point = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                point.next,l1 = l1,l1.next
            else:
                point.next,l2 = l2,l2.next
            point = point.next
        point.next = l1 if l1 else l2
            
        return result.next

